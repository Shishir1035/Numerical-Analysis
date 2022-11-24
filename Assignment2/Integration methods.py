from math import log, sin, cos, tan, e, pi
import prettytable as pt

solutions = pt.PrettyTable(['Segment','Trapezoidal','Simpson'])

def f(func,x):
    return eval(func)

def trape(func,up,lp,seg):  
    h = (up - lp) / seg    
    result = f(func,lp) + f(func,up)
    for i in range(1, seg):
        result += 2 * f(func, lp + i*h)
    result *= (up-lp) / (2*seg)
    return result

def simpson(func,up,lp,seg):
    h = (up-lp) / seg
    result = f(func,up)+ f(func,lp)
    for i in range(1, seg, 2):
        result += 4 * f(func, lp + i*h)
    for i in range(2, seg-1, 2):
        result += 2 * f(func, lp + i*h)
    result *= (up-lp)/(3*seg)
    return result


# ------------------------- code starts from here ----------------------------
func = input("Enter the integrand here , f(x) = ")
up = float(input('upper limit = '))
lp = float(input('lower limit = '))
seg = int(input('segment upto = '))

for i in range (1,seg+1):
    anstrap = trape(func,up,lp,i)
    anssimp = simpson(func,up,lp,i)
    solutions.add_row(["%d"%i, "%.8f"%anstrap, "%.8f"%anssimp])
print(solutions)
