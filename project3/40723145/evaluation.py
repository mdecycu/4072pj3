import numpy as np
from sympy import *
import matplotlib.pyplot as plt


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
    
    
def test_Firebird(COGy):
    wheel_travel = [i for i in range(0, 160, 10)]
    h2 = [1389.3537, 1328.70, 1282.04, 1248.82, 1228.1094, 1218.5712, 1218.4187, 1225.4416, 1237.00, 1250, 1260.72, 1264.5, 1254.91, 1221.5628, 1144.2291, 970.9124]
    as_list = []
    # h1 = 1133.6821
    for j in h2:
        a = (j/COGy) *100
        as_list.append(a)
    plt.xlim(0, 160)
    plt.ylim(-60, 140)
    plt.xlabel("wheel travel")
    plt.ylabel("AS%")
    plt.grid(True, linewidth="0.5")
    plt.plot(wheel_travel, as_list, color="orange", label="Firebird")
    plt.legend(loc="lower right")
    plt.show()


def test_RDO(COGy):
    wheel_travel = [i for i in range(0, 160, 10)]
    h2 = [1408.28, 1172.4695, 942.3872, 718.1976, 500.1066, 288.3392, 83.1073, -115.4366, -307.2646, -492.5643, -671.86, -846.1753, -1017.2479, -1187.8199, -1362.0397, -1546.048]
    as_list = []
    h1 = 1057
    for j in h2:
        a = (j/h1) *100
        as_list.append(a)
    plt.xlim(0, 160)
    plt.ylim(-160, 140)
    plt.xlabel("wheel travel")
    plt.ylabel("AS%")
    plt.grid(True, linewidth="0.5")
    plt.plot(wheel_travel, as_list, color="orange", label="RDO 29ㄋ")
    plt.legend(loc="upper right")
    plt.show()
    

if __name__ == "__main__":
    # func_RearAxle([(-476, 67.1), (-476.05, 104.69), (-466.05, 163.6)])
    # func_UpChain([(-474.46, 97), (-40, 86.2)])
    # anti_squat((0, 0), (422.4587, 392.1147), 100)
    test_Firebird(COGy=1133.6821)
    test_RDO(COGy=1057)
