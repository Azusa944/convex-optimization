import numpy as np

from gadient.Armijo_rule import *
import matplotlib.pyplot as plt


def fun(x):
    """
    定义一个函数，返回在某点的函数值\n
    传入参数介绍：\n
    x:  函数在某点的坐标,例如 x = [1, 2]\n
    """
    return ((x[0] - 1)**2 - 4) + ((x[1] - 3)**2 - 9)


def g_fun(var_x):
    """
        计算函数在某点的梯度，返回一个列表，列表每一个元素为函数在某点对应坐标轴方向的偏导数
        传入参数介绍：\n
        var_x: 函数在某点的坐标,例如 x = [1, 2]\n
    """
    length = len(var_x)  # 得到变量个数
    grad_f = [0] * length
    delta = 1e-5
    for index in range(0, length):  # 对每个变量求偏导
        temp = var_x[index]
        var_x[index] = temp + delta  # f(x + h, y)
        d_fun1 = fun(var_x)
        var_x[index] = temp - delta  # f(x - h, y)
        d_fun2 = fun(var_x)
        grad_f[index] = (d_fun1 - d_fun2) / (2 * delta)  # 对(f(x + h, y) - f(x - h, y)) / 2h取极限
        var_x[index] = temp
    return grad_f


# var_x = [1, 2]
# alpha = 0.6
# grad_f = g_fun(fun, var_x)
# temp_x1 = var_x[0]
# var_x[0] = var_x[0] - alpha * grad_f[0]
# temp_x2 = var_x[1]
# var_x[1] = var_x[1] - alpha * grad_f[1]
# num = 0
#
# for index in range(0, 10000):
#     if abs(var_x[0] - temp_x1) >= 1e-5 or abs(var_x[1] - temp_x2) >= 1e-5:
#         temp_x1 = var_x[0]
#         var_x[0] = var_x[0] - alpha * grad_f[0]
#         grad_f = g_fun(fun, var_x)
#         temp_x2 = var_x[1]
#         var_x[1] = var_x[1] - alpha * grad_f[1]
#         grad_f = g_fun(fun, var_x)
#         num += 1
#     else:
#         break
# print("一共迭代了" + str(num) + "次")
# print(var_x)


def gradient_descent(var_x):
    """
    梯度法求解最优解\n
    传入参数介绍：\n
    var_x:  \t初始解，例如var_x = [1, 2]\n
    alpha:  \t迭代步长，例如alpha = 0.6
    """
    var_x_0 = []
    var_x_1 = []
    num = 0
    grad_f = g_fun(var_x)
    alpha = armijo_rule(fun, g_fun, var_x)
    for index in range(0, 10000):

        # 对点的每个坐标进行迭代
        true_num = 0  # 用来记录迭代后满足收敛条件的点坐标的分量的数量
        temp_x = [0] * len(var_x)
        for item in range(0, len(var_x)):
            temp_x[item] = var_x[item]  # 记录更改之前的坐标分量的值
            var_x[item] = var_x[item] - alpha * grad_f[item]  # 更新坐标分量的值，更新方法为梯度下降
            grad_f = g_fun(var_x)  # 计算函数在新点的梯度
        num += 1
        print("第" + str(num) + "次迭代")
        print("迭代结果为" + str(var_x))

        # var_x_0.append(var_x[0])
        # var_x_1.append(var_x[1])
        print()

        # 设置收敛条件并判断是否终止迭代
        for item in range(0, len(var_x)):
            if abs(var_x[item] - temp_x[item]) < 1e-5:
                true_num += 1
        if true_num == len(var_x):
            break
        # if abs(var_x[0] - temp_x[0]) < 1e-5 and abs(var_x[1] - temp_x[1]) <= 1e-5:
        #     break

    print("一共迭代了" + str(num) + "次")
    print("迭代结果为" + str(var_x))
    # plt.plot(np.array(var_x_0), var_x_1, c="r", marker='o', mfc='b', mec='b')
    # for a, b in zip(var_x_0, var_x_1):
    #     plt.text(a, b, (round(a, 3), round(b, 3)), ha='center', va='bottom', fontsize=10)

    # plt.show()


# # 案例 1
# var_x = [4, 4]
# alpha = 0.001
# # alpha2 = armijo_rule(fun, var_x)
# #     return (x[0]**2 + x[1] - 11) ** 2 + (x[0] + x[1]**2 - 7) ** 2
# print("初始解为" + str(var_x))
# print("初始解处梯度向量为" + str(g_fun(var_x)))
# gradient_descent(var_x, alpha)
# print("最优点处函数梯度向量为" + str(g_fun(var_x)))


