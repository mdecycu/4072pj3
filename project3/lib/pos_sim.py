import numpy as np
from pyslvs import *
import matplotlib.pyplot as plt

########################
p0 = (0, 0)
p1 = (-41.52, -5.1)
p2 = (-397.41, -42.50)
p3 = (17.68, 111.69)
p4 = (-3.2, 154.98)
p5 = (89, 201.72)
theta = 187
########################


def distance(pp1, pp2):
        return np.sqrt((pp1[0]-pp2[0])**2 + (pp1[1]-pp2[1])**2)


class pos(object):
    def __init__(self, p0, p1, p2, p3, p4, p5, theta):
        self.p0 = Coord(p0[0], p0[1])
        self.p1 = Coord(p1[0], p1[1])
        self.p2 = Coord(p2[0], p2[1])
        self.p3 = Coord(p3[0], p3[1])
        self.p4 = Coord(p4[0], p4[1])
        self.p5 = Coord(p5[0], p5[1])
        self.r01 = distance(p0, p1)
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
        a0v = (self.r24**2 - self.r12**2 - self.r14**2) / (-2*self.r12*self.r14)
        if a0v>1:
            a0v -= 2
        elif a0v<-1:
            a0v += 2
        # randians
        a0r = np.arccos(a0v)
        a0d = a0r * 180/np.pi
        print(a0d)
        self.p2 = plap(self.p1, self.r12, a0r, self.p4)
        
        """
        print(
            "p0: ", self.p0, "\n"
            "P1: ", self.p1, "\n"
            "p2: ", self.p2, "\n"
            "p3: ", self.p3, "\n"
            "p4: ", self.p4, "\n"
            "p5: ", self.p5, "\n"
        )"""
        
    def result(self):
        posf = [
            (self.p0.x, self.p0.y),
            (self.p1.x, self.p1.y),
            (self.p2.x, self.p2.y),
            (self.p3.x, self.p3.y),
            (self.p4.x, self.p4.y),
            (self.p5.x, self.p5.y),
        ]
        return posf


if __name__ == "__main__":
    pos = pos(p0, p1, p2, p3, p4, p5, theta)
    # pos.ppos()
    # print(type(pos.p2))
    # print(pos.p2.x)
    print(pos.result())



