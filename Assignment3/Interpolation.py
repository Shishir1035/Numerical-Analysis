import prettytable as pt

global size

solutions = pt.PrettyTable(['Methods','Linear','Quadratic','Cubic'])

def gauss_with_partial_pivoting(newmat,n):
    newmat1 = forward_eli(newmat,n)
    return back_sub(newmat1,n)
 
# function for elementary operation of swapping two rows
def swap_row(i,j,newmat,n):

    for k in range(n + 1):
        temp = newmat[i][k]
        newmat[i][k] = newmat[j][k]
        newmat[j][k] = temp
 
# Forward Elimination
def forward_eli(newmat,n):
    for k in range(n):
        row_max = k
        val_max = newmat[row_max][k]
 
        for i in range(k + 1, n):
            if (abs(newmat[i][k]) > val_max):
                val_max = newmat[i][k]
                row_max = i
 
        # Swap the greatest value row with current row
        if (row_max != k):
            swap_row(k, row_max, newmat,n)
 
        for i in range(k + 1, n):
            f = newmat[i][k]/newmat[k][k]
            for j in range(k + 1, n + 1):
                newmat[i][j] -= newmat[k][j]*f 
            newmat[i][k] = 0
    return newmat

def back_sub(newmat,n):
    roots = [0.0 for i in range(n)]
    roots[n-1] = newmat[n-1][n]/newmat[n-1][n-1]

    for i in range(n-2,-1,-1):
        roots[i] = newmat[i][n]
        for j in range(i+1,n):
            roots[i] = roots[i] - newmat[i][j]*roots[j]
        roots[i] = roots[i]/newmat[i][i]
    return roots

def find_points(x1, xlist, ylist, n):
    diff = []
    for i in range(size):
        diff.append([abs(xlist[i]-x1),xlist[i],ylist[i]])

    diff.sort()
    xl = []
    yl = []
    for i in range(n+1):
        xl.append(diff[i][1])
        yl.append(diff[i][2])
    return xl,yl


def direct(x1, xlist, ylist, meth):
    if meth == 1:
        xl , yl = find_points(x1,xlist,ylist,meth)
        return linearinter(x1,xl,yl)
    elif meth == 2:
        xl , yl = find_points(x1,xlist,ylist,meth)
        return quadinter(x1,xl,yl)    
    elif meth == 3:
        xl , yl = find_points(x1,xlist,ylist,meth)
        return cubinter(x1,xl,yl)

def linearinter(xn,xl,yl):
    x0, x1 = xl
    y0, y1 = yl
    a1 = (y0 - y1) / (x0 - x1)
    a0 = y0 - a1*x0
    return (a0 + a1*xn)

def quadinter(xn, xl, yl):
    eqn = []
    for i in range(3):
        eqn.append( [1, xl[i], xl[i]**2, yl[i]] )
    
    b = gauss_with_partial_pivoting(eqn,3)
    yn = b[0] + b[1] * xn + b[2] * xn**2

    return yn

def cubinter(xn,xl,yl):
    eqn = []
    for i in range(4):
        eqn.append( [1, xl[i], xl[i]**2, xl[i]**3, yl[i]] )
    
    b = gauss_with_partial_pivoting(eqn,4)
    yn = b[0] + b[1] * xn + b[2] * xn**2 + b[3] * xn**3
    return yn

def linearlan(xn,xlist,ylist):
    xl, yl = find_points(xn, xlist, ylist, 1)
    x0, x1 = xl
    y0, y1 = yl 
    L0 = (xn - x1) / (x0 - x1)
    L1 = (xn - x0) / (x1 - x0)
    yn = L0 * y0 + L1 * y1
    return yn

def quadlan(xn,xlist,ylist):
    xl, yl = find_points(xn, xlist, ylist, 2)
    L = []

    for i in range(3):
        mul = 1
        for j in range(3):
            if i != j:
                mul *= (xn - xl[j]) / (xl[i] - xl[j])
        L.append(mul)
    
    yn = 0
    for i in range(3):
        yn += L[i] * yl[i]        
    return yn

def cubelan(xn, xlist, ylist):
    xl, yl = find_points(xn, xlist, ylist, 3)
    L = []
    
    for i in range(4):
        mul = 1
        for j in range(4):
            if i != j:
                mul *= (xn - xl[j]) / (xl[i] - xl[j])
        L.append(mul)

    yn = 0
    for i in range(4):
        yn += L[i] * yl[i]
    return yn

def linearnewton(xn,xlist,ylist):
    xl, yl = find_points(xn, xlist, ylist, 1)
    x0, x1 = xl
    y0, y1 = yl
    b0 = y0
    b1 = (y1 - y0) / (x1 - x0)
    yn = b0 + b1 * (xn - x0)
    return yn

def quadnewton(xn,xlist,ylist):
    xl, yl = find_points(xn, xlist, ylist, 2)
    
    b0 = yl[0]
    b1 = (yl[1] - yl[0]) / (xl[1] - xl[0])
    b2 = (( (yl[2]-yl[1]) / (xl[2] - xl[1]) ) - ( (yl[1] - yl[0]) / (xl[1] - xl[0]) )) / (xl[2] - xl[0])
    
    yn = b0 + b1 * (xn - xl[0]) + b2 * (xn - xl[0]) * (xn-xl[1])
    return yn

def cubenewton(xn,xlist,ylist):
    xl, yl = find_points(xn, xlist, ylist, 3)
    
    b0 = yl[0]
    b1 = (yl[1] - yl[0]) / (xl[1] - xl[0])
    b2 = (( (yl[2]-yl[1]) / (xl[2] - xl[1]) ) - ( (yl[1] - yl[0]) / (xl[1] - xl[0]) )) / (xl[2] - xl[0])
    b3 = ( ( ( (yl[3] - yl[2]) / (xl[3] - xl[2]) - (yl[2] - yl[1]) / (xl[2] - xl[1]) ) / (xl[3] - xl[1]) ) - ( ( ( (yl[2] - yl[1])/(xl[2] - xl[1]) ) - ((yl[1] - yl[0]) / (xl[1] - xl[0])) ) / (xl[2] - xl[0]) ) ) / (xl[3] - xl[0])
    
    yn = b0 + b1 * (xn - xl[0]) + b2 * (xn - xl[0]) * (xn-xl[1]) 
    yn += b3 * (xn - xl[0]) * (xn - xl[1]) * (xn - xl[2])
    return yn
    

# --------------------------- code starts from here --------------------------------
print("Number of initial pairs must be greater than or equal to 4 to get all methods working!!")
size = int(input("Number of x,y pair as input : "))
xlist = [float(i) for i in input("Enter the "+str(size)+" values of x : ").split()]
ylist = [float(i) for i in input("Enter the "+str(size)+" values of y : ").split()]

xn = float(input("Enter the value of x to find corresponding value of y : "))

# Interpolation using direct method
lineardirect = direct(xn,xlist,ylist,1)
quaddirect = direct(xn,xlist,ylist,2)
cubdirect = direct(xn,xlist,ylist,3)
solutions.add_row(["Direct",'%.18f'%lineardirect, '%.18f'%quaddirect, '%.18f'%cubdirect])

# Interpolation using lagrange method
linlagrange = linearlan(xn,xlist,ylist)
quadlagrange = quadlan(xn,xlist,ylist)
cublagrange = cubelan(xn,xlist,ylist)
solutions.add_row(["Lagrange",'%.18f'%linlagrange, '%.18f'%quadlagrange, '%.18f'%cublagrange])

# Interpolation using newton method
linnewton = linearnewton(xn,xlist,ylist)
quanewton = quadnewton(xn,xlist,ylist)
cubnewton = cubenewton(xn,xlist,ylist)
solutions.add_row(["Newton's Divide",'%.18f'%linnewton, '%.18f'%quanewton, '%.18f'%cubnewton])

print(solutions)