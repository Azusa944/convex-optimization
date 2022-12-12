def f(x):
    """定义一个一元的函数"""
    return x ** 2 + 2 * x + 1


def gradient_x(f, x):
    """求函数关于x的导数"""
    h = 1e-6
    gradient = (f(x + h) - f(x)) / h
    if gradient < 1e-5:
        gradient = 0.0
    return gradient


def Armijo_alpha(f, x0):
    """利用Armijo_alpha准则确定搜索步长α"""
    gamma = 0.5
    c = 0.5
    alpha = 5
    while f(x0 - alpha) > f(x0) + c * alpha *gradient_x(f, x0) * (-1):
        alpha = gamma * alpha
    return alpha


def gradient_search(f, x0):
    """使用梯度下降算法求解最优解"""
    x = [x0]
    index = 0
    gamma = 0.5
    c = 0.5
    alpha = 5
    while f(x0 - alpha) > f(x0) + c * alpha * gradient_x(f, x0) * (-1):
        alpha = gamma * alpha
    # 确定迭代方法

    #  x[index + 1] = x[index] - alpha * gradient_x(f, x[index])
    x[1] = x[0] - alpha * gradient_x(f, x[0])
    for index in range(1, 1000):

        while f(x[index] - alpha) > f(x[index]) + c * alpha * gradient_x(f, x[index]) * (-1):
            alpha = gamma * alpha
        if abs(f[x[index] - f(x[index-1])]) >= 1e-5:
            x[index + 1] = x[index] - alpha * gradient_x(f, x[index])
    return x
    # 确定退出条件


gradient_search(f, 5)
