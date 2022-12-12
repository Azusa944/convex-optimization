import numpy as np

def fun(x):
    """
    定义一个函数，返回在某点的函数值\n
    传入参数介绍：\n
    x:  函数在某点的坐标,例如 x = [1, 2]\n
    """
    return (x[0] + 1) ** 2 + (x[1] - 7) ** 2


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


def armijo_rule(fun, g_fun, var_x):
    """
        利用armijo准则求解每一次迭代的最优搜索步长

    """
    alpha0 = 1
    alpha = alpha0
    gamma = 0.9
    sigma = 0.4
    num = 0
    grad_f_arr = np.array(g_fun(var_x))
    var_x_arr = np.array(var_x)
    d_vec = -grad_f_arr
    for index in range(0, 10000):
        var_x_arr_new = var_x_arr + alpha * d_vec
        num1 = fun(var_x_arr_new.tolist())
        num2 = fun(var_x)
        num3 = sigma * alpha * np.dot(grad_f_arr, d_vec)
        if num1 > num2 + num3:
            alpha = gamma * alpha
            num += 1
        else:
            break
    print("迭代次数为" + str(num))
    return alpha





def armijo_goldstein_rule(fun, g_fun, var_x):
    """
        利用Armijo_Goldstein_rule求解每一次迭代的最优搜索步长

    """
    alpha0 = 1
    alpha = alpha0
    gamma = 0.9
    sigma = 0.4
    num = 0
    grad_f_arr = np.array(g_fun(var_x))
    var_x_arr = np.array(var_x)
    d_vec = -grad_f_arr
    for index in range(0, 10000):
        var_x_arr_new = var_x_arr + alpha * d_vec
        num1 = fun(var_x_arr_new.tolist())
        num2 = fun(var_x)
        num3 = np.dot(grad_f_arr, d_vec)
        if num1 > num2 + sigma * alpha * num3:
            if num1 < num2 + (1 - sigma) * alpha * num3:
                alpha = gamma * alpha
            num += 1
        else:
            break
    print("迭代次数为" + str(num))
    return alpha


# var_x = [10, 10]
# # alpha2 = armijo_rule(fun, var_x)
# print("初始解为" + str(var_x))
# print("初始解处梯度向量为" + str(g_fun(var_x)))
# alpha1 = armijo_rule(fun, g_fun, [10, 10])
# print("使用armijo准则得到的最优的alpha为" + str(alpha1))
# alpha2 = armijo_goldstein_rule(fun, g_fun, [10, 10])
# print("使用armijo-goldstein准则得到的最优的alpha为" + str(alpha2))
