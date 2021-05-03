import numpy as np
from sympy import *


p0 = (0, 0)
p1 = (-41.52, -5.1)
p2 = (-397.41, -42.50)
p3 = (17.68, 111.69)
p4 = (-3.2, 154.98)
p5 = (89, 201.72)

# lf = lower frame
lf = (-12.72, -63.05)
lf_r = 105.16/2
p2_r = 85.56/2


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
    print(p_tang)
    """
    ttt = tang[0][0] * (-396) + tang[0][1]
    print(ttt)
    """
    return p_tang


def anti_squat(rear_pline_pos, IFC):
    origin2front = 662.88
    rear2rearpath = -413.68
    
    h2l_coe = line_func(rear_pline_pos, IFC)
    o_h2 = h2l_coe[0] * origin2front + h2l_coe[1]
    h2 = o_h2 - rear2rearpath
    # print(h2 -  rear2rearpath)
    return h2
    

def _img(travel_step, h1):
    import matplotlib.pyplot as plt
    wheel_travel = [i for i in range(0, 160, travel_step)]
    as_list = []
    for j in wheel_travel:
        h2 = anti_squat((-397.12, -413.68+j), IFC)
        as_list.append(h2)
    plt.plot(wheel_travel, as_list)
    plt.show()


if __name__ == "__main__":
    IC = intersection(p0, p1, p3, p4)
    otl = out_tanglin(lf, p2, lf_r, p2_r)
    IFC = intersection(p2, IC, lcoe=otl)
    # print(IFC)
    # anti_squat((-397.12, -413.68), IFC)
    # _img(10, 1133.68)
    
    qfunc = quadratic_func(p2, (-399.43, 7.1047), (-395.3689, 57.1047))
    # print(qfunc)
    
    test_p = (-399.43, 7.1047)
    # test_qfunc = 18.063160*test_p[0]**2 + 14368.8922148*test_p[0] + 2857498.93
    a = 18.063160731140137
    b = 14368.892214823521
    c =  2857498.9376570154
    test_qfunc = (-b - np.sqrt(b**2 - 4*a*(c-test_p[1]))) / 2*a
    # print(test_qfunc)