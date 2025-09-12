from math import sin, pi

def H_epsilon(x, eps=0.01):
    """The smoothed Heaviside function"""
    if x < -eps:
        return 0
    elif -eps <= x <= eps: 
        return 0.5 + (x/(2*eps)) + sin(pi*x / eps) / (2*pi)
    elif x > eps:
        return 1



def test_H_epsilon():
    eps = 0.01
    x_list = [eps - 0.1, -eps, 0, eps, eps + 0.1]
    print(f"The smoothed Heaviside function with eps {eps} for x = %.2f, %.2f, %.2f, %.2f, %.2f" % tuple(x_list))
    for i in range(len(x_list)):
        print("H_eps(%5.2f) = %5.2f" %(x_list[i], H_epsilon(x_list[i], eps)))

test_H_epsilon()
