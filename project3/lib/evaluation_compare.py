import numpy as np
from pyslvs import *
from sympy import *
import matplotlib.pyplot as plt
import os.path


def import_test():
    filename = os.path.basename(__file__)
    return filename + " import successfully !"


def distance(pp1: tuple, pp2: tuple):
    return np.sqrt((pp1[0]-pp2[0])**2 + (pp1[1]-pp2[1])**2)


class Pos(object):
    def __init__(self, p0, p1, p2, p3, p4, p5, theta):
        self.p0 = Coord(p0[0], p0[1])
        self.p1 = Coord(p1[0], p1[1])
        self.p2 = Coord(p2[0], p2[1])
        self.p3 = Coord(p3[0], p3[1])
        self.p4 = Coord(p4[0], p4[1])
        self.p5 = Coord(p5[0], p5[1])
        self.r01 = distance(p0, p1)
        self.r02 = distance(p0, p2)
        self.r03 = distance(p0, p3)
        self.r12 = distance(p1, p2)
        self.r14 = distance(p1, p4)
        self.r24 = distance(p2, p4)
        self.r34 = distance(p3, p4)
        self.theta = theta
        
    def ppos(self):
        p1x = self.r01 * np.cos(np.radians(self.theta))
        p1y = self.r01 * np.sin(np.radians(self.theta))
        self.p1 = Coord(p1x, p1y)
        
        self.p4 = pllp(self.p1, self.r14, self.r34, self.p3)
        # calculate the plap function parameter "a0"
        a0v = (self.r24**2 - self.r12**2 - self.r14**2) / (-2*self.r12*self.r14)
        if a0v>1:
            a0v -= 2
        elif a0v<-1:
            a0v += 2
        # randians
        a0r = np.arccos(a0v)
        a0d = a0r * 180/np.pi
        self.p2 = plap(self.p1, self.r12, a0r, self.p4)
        
        posf = [
            (self.p0.x, self.p0.y),
            (self.p1.x, self.p1.y),
            (self.p2.x, self.p2.y),
            (self.p3.x, self.p3.y),
            (self.p4.x, self.p4.y),
            (self.p5.x, self.p5.y),
        ]
        return posf
    
    def theta1(self):
        # for r01, r02 theta
        cos_val = (self.r12**2 - self.r01**2 - self.r02**2) / (-2*self.r01*self.r02)

        if cos_val>1:
            cos_val -= 2
        elif cos_val<-1:
            cos_val += 2
        # randians
        r01r02_r = np.arccos(cos_val)
        r01r02_d = r01r02_r * 180/np.pi
        print("r01r02_d: ", r01r02_d)
        
        # for r02, horizental line theta
        
        r02h_r = abs(np.arctan(p2y/p2x))
        if r02h_r>1:
            r02h_r -= 2
        elif r02h_r<-1:
            r02h_r += 2
        r02h_d = r02h_r * 180/np.pi
        print("r02h_d: ", r02h_d)
        
        # decide add or subtract
        if p2[1] >= 0:
            theta_tot = (180 - r01r02_d - r02h_d)
        else:
            theta_tot = (180 + r01r02_d + r02h_d)
        # print(theta_tot)
        
        return theta_tot
        
        
        

def line_func(point1: tuple, point2: tuple):
    # ax + b = y
    A = np.array([
        [point1[0], 1],
        [point2[0], 1]
    ])
    
    B = np.array([point1[1], point2[1]]).reshape(2, 1)
    A_inv = np.linalg.inv(A)
    ans = A_inv.dot(B)
    lcoe = (ans[0][0], ans[1][0])
    # a = lcoe[0][0], b = lcoe[1][0]
    return lcoe
    
    
def quadratic_func(point1: tuple, point2: tuple, point3:tuple):
    #y =ax^2 + bx +c
    A = np.array([
        [point1[0]**2, point1[0], 1],
        [point2[0]**2, point2[0], 1],
        [point3[0]**2, point3[0], 1]
    ])
    B = np.array([point1[1], point2[1], point3[1]]).reshape(3, 1)
    A_inv = np.linalg.inv(A)
    ans = A_inv.dot(B)
    # print("ans: ", ans)
    lcoe = (ans[0][0], ans[1][0], ans[2][0])
    # a = lcoe[0][0], b = lcoe[1][0], c = lcoe[2][0]
    return lcoe
    
    
def intersection(p1: tuple, p2: tuple, p3=None, p4=None, lcoe=None):
    # ax - y = -b
    l1 = line_func(p1, p2)
    if p3 != None and p4 != None:
        # l1 = line_func(p1, p2)
        l2 = line_func(p3, p4)
    elif lcoe != None:
        # l1 = line_func(p1, p2)
        l2 = lcoe
    A = np.array([
        [l1[0], -1],
        [l2[0], -1]
    ]) 
    B = np.array([-l1[1], -l2[1]]).reshape(2, 1)
    A_inv = np.linalg.inv(A)
    ans = A_inv.dot(B)
    p_ans = (ans[0][0], ans[1][0])
    # print(p_ans)
    return p_ans


def out_tanglin(p1: tuple, p2: tuple, r1: float, r2: float):
    k, b = symbols("k, b")
    func_c1 = (p1[1] - k*p1[0] - b) + r1*(1+k**2)**0.5
    func_c2 = -(p2[1] - k*p2[0] - b) - r2*(1+k**2)**0.5
    tang = solve([func_c1, func_c2], [k, b])
    # print(tang[0][1])
    p_tang = (float(tang[0][0]), float(tang[0][1]))
    # print(p_tang)
    return p_tang


def anti_squat(rear_pline_pos: tuple, IFC: tuple, h1: float, origin2front):
    h2l_coe = line_func(rear_pline_pos, IFC)
    o_h2 = h2l_coe[0] * origin2front + h2l_coe[1]
    # 2-D plane
    h2 = (o_h2 - rear_pline_pos[1])
    h2_percent = (h2/h1) * 100
    return h2_percent
    
    
def anti_rise(rear_pline_pos: tuple, IC: tuple, h1: float, origin2front):
    h2l_coe = line_func(rear_pline_pos, IC)
    o_h2 = h2l_coe[0] * origin2front + h2l_coe[1]
    # 2-D plane
    h2 = (o_h2 - rear_pline_pos[1])
    h2_percent = (h2/h1) * 100
    return h2_percent
    
    
def _img(type, h1, rear_pline_pos, theta, travel_step=10):
    wheel_travel = [i for i in range(0, 160, travel_step)]

    
    
    if type == "Twin-link suspension (Firebird)":
        # theta_list = [194.04, 190.06, 186.29, 182.75, 179.46, 176.44, 173.72, 171.31, 169.25, 167.56, 166.29, 165.46, 165.16, 165.48, 166.68, 169.39]
        pass
        
        # theta_list = [191.35, 187.67, 184.24, 181.05, 178.15, 175.55, 173.27, 171.34, 169.79, 168.65, 167.97, 167.85, 168.4, 169.93, 173.43, 175.53]
        
    elif type =="Horst-link suspension (RDO)":
        dtheta_list = [0, 3.17, 3.09, 3.0223, 2.9428, 2.8634, 2.7809, 2.6942, 2.602, 2.5036, 2.3974, 2.2824, 2.1573, 2.0207, 1.8711, 1.7067]
        
    for i in range(4):
        p0 = (0, 0-i)
        p1 = (-40, -10)
        p2 = (-390, -40)
        p3 = (20, 120)
        p4 = (-5, 150)
        p5 = (89, 201.72)
        theta = 194.04
        
        # theta_list = [194.04, 190.06, 186.29, 182.75, 179.46, 176.44, 173.72, 171.31+i, 169.25+i, 167.56+i, 166.29+i, 165.46+i, 165.16+i, 165.48+i, 166.68+i, 169.39+i]
        theta_list = [194.04+i, 190.06+i, 186.29+i, 182.75+i, 179.46+i, 176.44+i, 173.72+i, 171.31+i, 169.25+i, 167.56+i, 166.29+i, 165.46+i, 165.16+i, 165.48+i, 166.68+i, 169.39+i]
        
        as_list1 = []
        ar_list1 = []
        for index, step in enumerate(wheel_travel):
            theta = theta_list[index]
            
            # p2 = (p2[0], p2[1]+step)
            pos = Pos(p0, p1, p2, p3, p4, p5, theta)
            
            
            print(index, step, pos.ppos(), "\n")
            IC = intersection(pos.ppos()[0], pos.ppos()[1], pos.ppos()[3], pos.ppos()[4])
            print("IC: ", IC)
            otl = out_tanglin(lf, pos.ppos()[2], lf_r, p2_r)
            IFC = intersection(pos.ppos()[2], IC, lcoe=otl)
            # print("IFC: ", IFC)
            h2_as = anti_squat((rear_pline_pos[0], rear_pline_pos[1]+step), IFC, h1, origin2front)
            h2_ar = anti_rise((rear_pline_pos[0], rear_pline_pos[1]+step), IC, h1, origin2front)
            
            # print("h2_as: ", h2_as)
            as_list1.append(h2_as)
            ar_list1.append(h2_ar)
            
        # show the anti-rise graph now
        if i == 0:
            plt.plot(wheel_travel, ar_list1, label=p0)
        else:
            plt.plot(wheel_travel, ar_list1, linestyle="--", label=p0)
    
    
    """------------------------------------------------------------------------------"""
        
        
    # plt.plot(wheel_travel, as_list, label="Anti squat")
    # plt.plot(wheel_travel, ar_list, label="Anti rise")
    
    
    plt.xlabel("wheel travel")
    plt.ylabel("%")
    # plt.xlim(0, 170)
    # plt.ylim(-100, 160,)
    # plt.legend(loc="best")
    plt.title("p0")
    plt.grid(True, linewidth="0.5")
    plt.show()
        
    

    

if __name__ == "__main__":
    ########### Joint configuration ###########
    
    # Firebird
    p0 = (0, 0)
    p1 = (-40, -10)
    p2 = (-390, -40)
    p3 = (20, 120)
    p4 = (-5, 150)
    p5 = (89, 201.72)
    theta = 194.04
    
    
    # lf = lower frame
    lf = (-12.72, -63.05)
    lf_r = 105.16/2
    p2_r = 85.56/2
    
    # other essential config
    h1 = 1057
    origin2front = 670
    rear_pline_pos = (p2[0], -408.3)
    
    
    """
    # RDO
    p0 = (0, 0)
    p1 = (-73, -44)
    p2 = (-474, 61.3)
    p3 = (-27.53, 241.43)
    # p4 = (-121.02, 282.65)
    p4 = (-136.02, 294.46)    # test the point from different algorithm
    p5 = (80.94, 242.93)
    theta = 209.15

    # lf = lower frame
    lf = (-27.5, 24.0354)
    lf_r = 124.3426/2
    p2_r = 60/2
    
    h1 = 1037
    rear_pline_pos = (-474.4089, -307)
    origin2front = 684.45
    """
    
    
    ########### Joint configuration ###########
    # _img("Horst-link suspension (RDO)", h1, rear_pline_pos, theta)
    _img("Twin-link suspension (Firebird)", h1, rear_pline_pos, theta)
    
    # pos = Pos(p0, p1, p2, p3, p4, p5, theta)
    
    