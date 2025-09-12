

def kinematics(x, i, dt=1E-6):
    t = [(i-1)*dt, i*dt, (i+1)*dt]
    vi = (x[i+1] - x[i-1]) / (t[2]-t[0])
    ai = 2*( ((x[i+1]-x[i])/(t[2]-t[1])) - ((x[i]-x[i-1])/(t[1]-t[0])) ) / ((t[2]-t[0]))

    return vi, ai

def my_kinematics(x, i, t):
    vi = (x[i+1] - x[i-1]) / (t[i+1]-t[i-1])
    ai = 2*( ((x[i+1]-x[i])/(t[i+1]-t[i])) - ((x[i]-x[i-1])/(t[i]-t[i-1])) ) / ((t[i+1]-t[i-1]))

    return vi, ai


def test_kinematics():
    V = 10
    t = [0, 0.5, 1.5, 2.2]
    x = []
    for i in range(len(t)):
        x.append(V*t[i])

    print(my_kinematics(x, 1, t))
    print(my_kinematics(x, 2, t))

test_kinematics()
