def egg(M, To=20, Ty=70):
    """
    How to cook the perfect egg.
    M   : Mass of the egg
    To  : The original temperature
    Ty  : The yolk coagulatation temperature
    """
    from math import log, pi

    ro = 1.038  # gr.cm^-3      density
    c = 3.7     # J.gr^-1.K^-1  specific heat capacity
    K = 5.4e-3  # W.cm^-1.K^-1  Thermal conductivity
    Tw = 100    # degree of C   Temperature of boiling water

    t = (((M**(2/3))*c*(ro**(1/3))) / (K*(pi**2)*((4*pi/3)**(2/3)))) * log(0.76 * ((To - Tw)/(Ty - Tw))) 
    
    return t

def table():
    M = [47, 67]    # small and large egg
    Ty = [63, 70]   # soft and hard boiled egg temperature
    To = [4, 25]    # original temperatures

    for m in M:
        for ty in Ty:
            for to in To:
                print("It would take %3.1f s for a %d gr egg to %d C 2coagulate boilling starting from %2d C" % (egg(m, to, ty), m, ty, to))

table()


