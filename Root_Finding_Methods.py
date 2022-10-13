import prettytable
import sympy

res = ''
roots = prettytable.PrettyTable(['Method', 'Root', 'Total Iteration'])

# get value of a function f(x) for value = x
def f(E,x):
    return eval(E)

# returns mid value for bisection
def bisection(a,b):
    return (a+b)/2

# returns mid value for regular falsi
def falsi(a,b,E):
    return (b*f(E,a) - a*f(E,b) ) / (f(E,a)-f(E,b))

# takes four parameter ,, and return root for the given Expression(E)
# since falsi and bisection are same. just different procedure of determining Xmid.
# I merged them in one function
def bracketing_method(method,a,b,E,acerror):
    global roots
    print('\n'+method+' method iteration table :')
    table = prettytable.PrettyTable(['low', 'high', 'mid', 'error(%)', 'f(mid)'])

    if (f(E,a) * f(E,b) >= 0):
        print("Root cannot be found for given [a,b] interval\n")
        return

    # initial Xmid 
    if method == 'Regular Falsi':
        ini = falsi(a,b,E)
    else:
        ini = bisection(a,b)

    fini = f(E,ini)
    table.add_row(["%.8f"%a,"%.8f"%b,"%.8f"%ini,"-------------","%.8f"%fini])
    steps = 1
    
    while True:

        if method == 'Regular Falsi':
            oldmid = falsi(a,b,E)
        else:
            oldmid = bisection(a,b)

        if f(E,a)*f(E,oldmid) < 0:
            b = oldmid
        else:
            a = oldmid    
        
        if method == 'Regular Falsi':
            newmid = falsi(a,b,E)
        else:
            newmid = bisection(a,b)

        error = (abs(newmid-oldmid)/newmid)*100
        res = newmid
        table.add_row(["%.8f"%a,"%.8f"%b,"%.8f"%oldmid,"%.8f"%error, "%.8f"%f(E,newmid)])
        steps =steps+1

        if error <= acerror or f(E,oldmid) == 0.0:
            break
    
    print(table)
    roots.add_row([method, "%.9f"%res, steps])

def newton_raphson_method( a, E, deriE, acerror):
    global roots

    print('\nNewton Raphson Method :')
    val = f(E,a)
    table = prettytable.PrettyTable(['Xi', 'error(%)', 'f(Xi)'])
    table.add_row(["%.8f"%a , "-----------" , "%.8f"%val])
    
    steps = 0
    newa = 0
    while True:
        check = f(deriE,a)
        while check == 0.0:
            print("For initial value "+str(a)+" f'("+str(a)+') = 0. Which causes division by zero error')
            a = float(input('Enter another initial value = '))
            check = f(deriE,a)

        newa = a - (f(E,a)/check)

        error = ( (abs(newa-a)/newa) * 100) 
        val = f(E,newa)
        table.add_row(["%.8f"%newa, "%.8f"%error, "%.8f"%val])
        a = newa
        steps = steps + 1
        if error < acerror:
            break
            
    print(table)
    roots.add_row(["Newton Raphson", "%.9f"%newa, steps])
	
def secant_method(x0, x1, E, acerror):
    global roots

    print('\nSecant Method :')
    val = f(E,x0)
    table = prettytable.PrettyTable(['Xi', 'error(%)', 'f(Xi)'])
    table.add_row(["%.8f"%x0 , "-----------" , "%.8f"%val])
    val = f(E,x1)
    table.add_row(["%.8f"%x1 , "-----------" , "%.8f"%val])
    
    steps = 0
    while True:
        check = f(E,x1)-f(E,x0)
        while check == 0.0:
            print(x1," ",x0,'Causes division by zero error')
            a = float(input('Enter a initial value X0 = '))
            check = f(E,x1)-f(E,x0)

        x2 = x1 -  ( f(E,x1) * (x1-x0) ) /  (f(E,x1)-f(E,x0))

        error = ( (abs(x2-x1)/x2) * 100) 
        
        val = f(E,x2)
        table.add_row(["%.8f"%x2, "%.8f"%error, "%.8f"%val])
        x0 = x1
        x1 = x2
        steps = steps + 1
        if error < acerror:
            break
            
    print(table)
    roots.add_row(["Secant", "%.9f"%x2, steps])

# ------------------- code starts from here --------------------------
func = input("Enter the function , f(x) = ")
a = float(input("Enter lower limit = "))
b = float(input("Enter upper limit = "))
acerror = float(input("Enter error acceptance (%) = "))

# get function's derivative
symbol = sympy.symbols('x')
derifunc = str(sympy.diff(func,symbol))

bracketing_method("Bisection",a, b, func, acerror)
bracketing_method("Regular Falsi",a, b, func, acerror)
newton_raphson_method(a, func, derifunc, acerror)
secant_method(a, b, func, acerror)
print(roots)