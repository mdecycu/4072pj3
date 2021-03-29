import numpy as np
from sympy import *


def func_UpChain(pp):
    # function => y - ax = b
    a = symbols("a")
    b = symbols("b")
    
    func1 = pp[0][1] - a*pp[0][0] - b
    func2 = pp[1][1] - a*pp[1][0] - b
    
    coefficient = solve([func1, func2], [a, b])
    print(f"y = ({coefficient[a]})x + {coefficient[b]}")
    # print("test the function: y =", -0.025*-332 + 85.21)
    return coefficient


def func_RearAxle(pp):
    # function => y = ax^2 + bx + c
    a, b ,c = symbols("a, b, c")
    # b = Symbol("b")
    # c = Symbol("c")

    
    func1 = a*pp[0][0]**2 + b*pp[0][0] + c - pp[0][1]
    func2 = a*pp[1][0]**2 + b*pp[1][0] + c - pp[1][1]
    func3 = a*pp[2][0]**2 + b*pp[2][0] + c - pp[2][1]
    
    result = solve([func1, func2, func3], [a, b, c])
    # print(result)
    print(f"y = ({result[a]})x^2 + ({result[b]})x + ({result[c]})")
    return result
    
    # print(result.keys())
    # print(result[b])
    
    
def anti_squat(rg, ic, wheel_travel=0):
    #function => y - ax = b
    a, b = symbols("a, b")
    func1 = (rg[1] + wheel_travel) - a*rg[0] - b
    func2 = ic[1] - a*ic[0] - b
    coe_gic= solve([func1, func2], [a, b])
    print(f"func_gic:   y = ({coe_gic[a]})x + {coe_gic[b]}")
    # print(coe_gic[a] * 845.1551 + coe_gic[b])
    
    x, y = symbols("x, y")
    func_gic = coe_gic[a]*x + coe_gic[b] - y
    
    
    # COGy = 1106.0524 - y
    fwgl = 1160 - x
    intersection = solve([func_gic, fwgl], [x, y])
    print(intersection)

    

# result = func_RearAxle([(-476, 67.1), (-476.05, 104.69), (-466.05, 163.6)])
# func = (76.149849246) * (-476.05)**2 + (71746.6639748) * (-476.05) + (16897750.9092261)
# print(func)



# func_RearAxle([(-476, 67.1), (-476.05, 104.69), (-466.05, 163.6)])
# func_UpChain([(-474.46, 97), (-40, 86.2)])
anti_squat((0, 0), (422.4587, 392.1147), 100)
