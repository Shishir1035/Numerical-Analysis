# import sympy
# dd = sympy.symbols('x')
# func = '3*x**3 + 2*x'
# deri = str(sympy.diff(func,dd))

# def f(E,x):
#     return eval(E)

# print((func)," -----------> ",(deri))

# print(type(func)," -----------> ",type(deri))
# print(f(func,2), "---------------> ", f(deri,3))

from prettytable import PrettyTable

res = ''
roots = PrettyTable(['METHOD', 'ROOT'])
def f(x):
    global chrnt
    sum = 0
    for p in chrnt:
        a = chrnt[p]
        sum += a*(x**p)
    return sum
def derivFunc( x ):
    global chrnt
    sum = 0
    for p in chrnt:
        a = chrnt[p]*p
        p = p - 1
        sum += a*(x**p)
    return sum


def bisection_method(a,b, E):
    global res
    global roots
    res += 'Bisection method : \n'
    table = PrettyTable(['a', 'b', 'root', 'error'])

    if (f(a) * f(b) >= 0):
        print("You have not assumed right a and b\n")
        return

    mid = a
    error = b-a
    while True:
        table.add_row(["%.9f"%a,"%.9f"%b,"%.9f"%mid,"%.9f"%error])
        if error <= E:
            break
        
        mid = (a+b)/2

        if f(mid) == 0.0:
            break

        if f(mid)*f(a) < 0:
            b = mid
        else:
            a = mid
        error = b-a
    root = mid
    res += str(table)
    res += '\nRoot : %.18f\n\n'%root
    roots.add_row(['Bisection', "%.18f"%root])

MAX_ITER = 100000
def false_position_method(a,b,E):
    global res, roots
    res += 'False Position Method :\n'
    table = PrettyTable(['a', 'b', 'root', 'error'])
    condition = True
    root = -1
    error = 123
    while error > E:
        root = (a*f(b) - b * f(a))/( f(b) - f(a) )

        if f(a) * f(root) < 0:
            a = root
        else:
            b = root

        error = abs(f(root))
        table.add_row(["%.9f"%a,"%.9f"%b,"%.9f"%root,"%.9f"%error])
    
    res += str(table)
    res += '\nRoot : %.18f\n\n' % root
    roots.add_row(['False Position', "%.18f"%root])


def newton_raphson_method( root, E ):
    global res, roots
    res += '\nNewton Raphson Method :\n'
    table = PrettyTable(['root', 'error'])

    error = f(root) / derivFunc(root)
    while abs(error) >= E:
        error = f(root)/derivFunc(root)
        root = root - error

        table.add_row(["%.18f"%root, "%.18f"%error])

    res += str(table)

    res += '\nRoot: '+ "%.20f"%root + '\n\n'
    roots.add_row(['Newton Raphson', "%.18f"%root])
	

 
def secant(x1, x2, E):
    global res, roots
    table = PrettyTable(['a', 'b/root', 'error'])
    res += 'Secant Method\n'
    print('Secant Method:\n')
    n = 0; xm = 0; root = 0; c = 0;
    if (f(x1) * f(x2) < 0):
        while True:
            prev_root = root
            root = ((x1 * f(x2) - x2 * f(x1)) /
                            (f(x2) - f(x1)));
 
            if f(x1) * f(root)==0:
                break

            x1, x2 = x2, root
 
            n += 1;
 
            xm = ((x1 * f(x2) - x2 * f(x1)) /
                            (f(x2) - f(x1)))
            table.add_row(["%e"%x1,"%e"%x2,"%e"%(abs(xm-root))])
             
            if(abs(xm - root) < E):
                break
        res += str(table)
         
        res+='\nRoot : ' + "%.18f"%root+'\n\n'

        roots.add_row(['Secant', "%.18f"%root])
    else:
        print("Can not find a root in the given interval")



chrnt = dict()

print('The function is now f(x)=0')
while input('Add one more term  a.x^p ? yes/no _ ').count('yes')>0:
    a = float(input('a='))
    p = float(input('p='))
    chrnt[p] = a
print(chrnt)



a =-100
b = 150
E = 1e-5
false_position_method(a, b, E)
bisection_method(a, b, E)
newton_raphson_method(a, E)
secant(a, b, E)
# print(res)
print('\n\n\n'+str(roots))
