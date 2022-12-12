from gadient.gradient import *


if __name__ == "__main__":
    # 案例 1
    var_x = [4, 4]
    print("初始解为" + str(var_x))
    print("初始解处梯度向量为" + str(g_fun(var_x)))
    gradient_descent(var_x)
    print("最优点处函数梯度向量为" + str(g_fun(var_x)))
    # hhh
