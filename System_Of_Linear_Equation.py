import numpy

def naive_gauss(mat):
    global roots
    # Naive Gaussian Elimination
    for i in range(n):
        if mat[i][i] == 0.0:
            print('Divide by zero !')
            
        for j in range(i+1, n):
            div = mat[j][i]/mat[i][i]
            
            for k in range(n+1):
                mat[j][k] = mat[j][k] - div * mat[i][k]
    back_sub(mat)

def gauss_with_partial_pivoting(newmat):
    forward_eli(newmat)
    back_sub(newmat)
 
# function for elementary operation of swapping two rows
def swap_row(i,j,newmat):
    global n

    for k in range(n + 1):
        temp = newmat[i][k]
        newmat[i][k] = newmat[j][k]
        newmat[j][k] = temp
 
# Forward Elimination
def forward_eli(newmat):
    global n
    for k in range(n):
        row_max = k
        val_max = newmat[row_max][k]
 
        for i in range(k + 1, n):
            if (abs(newmat[i][k]) > val_max):
                val_max = newmat[i][k]
                row_max = i
 
        # Swap the greatest value row with current row
        if (row_max != k):
            swap_row(k, row_max, newmat)
 
        for i in range(k + 1, n):
            f = newmat[i][k]/newmat[k][k]
            for j in range(k + 1, n + 1):
                newmat[i][j] -= newmat[k][j]*f 
            newmat[i][k] = 0

def back_sub(newmat):
    global roots
    roots[n-1] = newmat[n-1][n]/newmat[n-1][n-1]

    for i in range(n-2,-1,-1):
        roots[i] = newmat[i][n]
        for j in range(i+1,n):
            roots[i] = roots[i] - newmat[i][j]*roots[j]
        roots[i] = roots[i]/newmat[i][i]

def show(method):
    global roots
    print("\nUsing",method , 'the Unknown values are : ')
    for i in range(0,n):
        print('X'+str(i), ' : ','%.6f'%roots[i])

def ludecomp(newmat):
    n = newmat.shape[0]
    Upper = numpy.copy(newmat)
    Lower = numpy.zeros((n,n))
    for row in range(n):
        Lower[row][row] = 1

    for i in range(n):
        for k in range(i,n-1,1):
            factor = Upper[k+1][i] / Upper[i][i]
            Lower[k+1][i] = factor
            Upper[k+1] -= factor * Upper[i]

    return Lower, Upper

def callnaivegauss(mat):
    newmat = numpy.copy(mat)
    naive_gauss(newmat)
    show(" Naive Gaussian Elimination")

def callpartialgauss(mat):
    newmat = numpy.copy(mat)
    gauss_with_partial_pivoting(newmat)
    show(" Gaussian Elimination with partial pivoting ")

# ---------------------- code starts from here -------------------------
n = int(input('Number of equations: '))
# n*(n+1) matrix .. 1 extra column for values of that equation
mat = numpy.zeros((n,n+1))
uppertri = numpy.zeros((n,n))
lowertri = numpy.zeros((n,n))
roots = numpy.zeros(n)

vals = []
print('Enter Augmented Matrix Coefficients: input format : x1 x2 x3 ... a1 ')
for i in range(1,n+1):
    print("Enter equation no.",i)
    eqn = input("")
    vals.append( eqn.split())

# input matrix build
for row in range(n):
    for col in range(n+1):
        mat[row][col] = float(vals[row][col])

print('\n--------- Augmented Matrix ---------\n',mat)

callnaivegauss(mat)
callpartialgauss(mat)

# Copying just the first part of the augmented matrix
newmat = numpy.zeros((n,n))
for row in range(n):
    for col in range(n):
        newmat[row][col] = mat[row][col]

lowertri, uppertri = ludecomp(newmat)
print('\n---------lower triangle matrix---------\n',lowertri)
print('\n---------upper triangle matrix---------\n',uppertri)