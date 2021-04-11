import numpy as np
from sympy import *

points = {
    "p0": (0, 0), 
    "p1": (-41.6, -4.5),
    "p2": (-397.41, -40),
    "p3": (-2.38, 154.98),
    "p4": (17.6674, 111.69),
    "p5": (89, 201.72)
}


print(points["p4"][1])


def func():
    # function => y - ax = b
    a01, b01 = symbols("a01, b01")
    # p0, p1
    func_p0 = points["p0"][1] - a01*points["p0"][0] - b01
    func_p1 = points["p1"][1] - a01*points["p1"][0] - b01
    coe_p0p1 = solve([func_p0, func_p1], [a01, b01])
    print(f"y = ({coe_p0p1[a01]})x + {coe_p0p1[b01]}")
    
    a34, b34 = symbols("a34, b34")
    func_p3 = points["p3"][1] - a34*points["p3"][0] - b34
    func_p4 = points["p4"][1] - a34*points["p4"][0] - b34
    coe_p3p4 = solve([func_p3, func_p4], [a34, b34])
    print(f"y = ({coe_p3p4[a34]})x + {coe_p3p4[b34]}")
    
    x, y = symbols("x, y") 
    func_01 = coe_p0p1[a01]*x + coe_p0p1[b01] - y
    func_34 = coe_p3p4[a34]*x + coe_p3p4[b34] - y
    ic = solve([func_01, func_34], [x, y])
    print(ic[x], ic[y])
    
    # return coefficient
    
    
func()