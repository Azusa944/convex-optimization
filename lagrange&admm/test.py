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


print(gradient_x(f, 0))


def Armijo_alpha(f, x0):
    """利用Armijo_alpha准则确定搜索步长α"""
    gamma = 0.5
    c = 0.5
    alpha = 5
    while f(x0 - alpha) > f(x0) + c * alpha * gradient_x(f, x0) * (-1):
        alpha = gamma * alpha
        print(alpha)
    return alpha


print(Armijo_alpha(f, 30))
