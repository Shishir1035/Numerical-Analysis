import prettytable as pt

solutions = pt.PrettyTable(['Step Size','Euler','Heun', 'Midpoint', 'Ralston'])
def f(E,x,y):
    return eval(E)

def euler (func,x0,y0,xn,n):
    h = (xn-x0)/n

    for i in range(n):
        slope = f(func, x0, y0)
        yn = y0 + h * slope
        y0 = yn
        x0 = x0+h
    return yn

def runge(func,x0,y0,xn,n,a1,a2,p1,q11):

    h = (xn - x0) / n
    for i in range(n):
        k1 = f(func,x0, y0)
        k2 = f(func, x0 + p1*h , y0 + q11*k1*h )                        
        yn = y0 + (a1*k1 + a2*k2)*h
        y0 = yn
        x0 = x0 + h   
    return yn

def heun(func,x0,y0,xn,n):
    a2,a1,p1,q11 = 0.5,0.5,1,1
    return runge(func,x0,y0,xn,n,a1,a2,p1,q11)

def midpoint(func,x0,y0,xn,n):
    a2,a1,p1,q11 = 1,0,0.5,0.5
    return runge(func,x0,y0,xn,n,a1,a2,p1,q11)

def ralston(func,x0,y0,xn,n):
    a2,a1,p1,q11 = 2/3,1/3,3/4,3/4
    return runge(func,x0,y0,xn,n,a1,a2,p1,q11)

# ------------------------- code starts from here ----------------------------
func = input("Enter the ODE here , f(x,y) = ")
x0 = float(input('x0 = '))
y0 = float(input('y0 = '))
xn = float(input('xn = '))

for i in range(1,11):
    eu = euler(func,x0,y0,xn,i)
    he = heun(func,x0,y0,xn,i)
    mid = midpoint(func,x0,y0,xn,i)
    ral = ralston(func,x0,y0,xn,i)
    solutions.add_row(["%.8f"%((xn-x0)/i), "%.8f"%eu,"%.8f"%he,"%.8f"%mid,"%.8f"%ral])

print(solutions)