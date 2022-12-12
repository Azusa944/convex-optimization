from sympy import *


def lagrange(x_vars):
    """利用拉格朗日乘子法求解极值问题"""
    x1 = x_vars[0]
    x2 = x_vars[1]
    k = symbols("k")
    # 构造目标函数
    f = (60 - 10 * x1 - 4 * x2 + x1 ** 2
         + x2 ** 2 - x1 * x2)
    print("目标函数f = " + str(f))

    # 构造约束函数
    g = x1 + x2 - 8
    print("约束函数g = " + str(g))

    # 构造lagrange等式
    l = f - k * g
    print("Lagrange函数l = " + str(l))

    # 求导，构造KKT条件
    dx1 = diff(l, x1)
    print("dx1 = ", dx1)
    dx2 = diff(l, x2)
    print("dx2 = ", dx2)
    dk = diff(l, k)
    print("dk = ", dk)

    res = solve([dx1, dx2, dk], [x1, x2, k])
    x1 = res[x1]
    x2 = res[x2]
    k = res[k]
    print(res)
    f = (60 - 10 * x1 - 4 * x2 + x1 ** 2
         + x2 ** 2 - x1 * x2)
    print("方程的极小值是", f)
