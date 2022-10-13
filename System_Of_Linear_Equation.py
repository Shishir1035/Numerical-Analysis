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

def gauss_with_partial_pivoting(mat):
    forward_eli(mat)
    back_sub(mat)
 
# function for elementary operation of swapping two rows
def swap_row(i,j):
    global mat
    global n

    for k in range(n + 1):
        temp = mat[i][k]
        mat[i][k] = mat[j][k]
        mat[j][k] = temp
 
# Forward Elimination
def forward_eli(mat):
    global n
    for k in range(n):
        row_max = k
        val_max = mat[row_max][k]
 
        for i in range(k + 1, n):
            if (abs(mat[i][k]) > val_max):
                val_max = mat[i][k]
                row_max = i
 
        # Swap the greatest value row with current row
        if (row_max != k):
            swap_row(k, row_max)
 
        for i in range(k + 1, n):
            f = mat[i][k]/mat[k][k]
            for j in range(k + 1, n + 1):
                mat[i][j] -= mat[k][j]*f 
            mat[i][k] = 0

def back_sub(mat):
    global roots
    roots[n-1] = mat[n-1][n]/mat[n-1][n-1]

    for i in range(n-2,-1,-1):
        roots[i] = mat[i][n]
        for j in range(i+1,n):
            roots[i] = roots[i] - mat[i][j]*roots[j]
        roots[i] = roots[i]/mat[i][i]

def show(method):
    global roots
    print("\nUsing",method , 'the Unknown values are : ')
    for i in range(0,n):
        print('X'+str(i), ' : ','%.6f'%roots[i])




# ---------------------- code starts from here -------------------------
n = int(input('Number of equations: '))
# n*(n+1) matrix .. 1 extra column for values of that equation
mat = numpy.zeros((n,n+1))
mat1 = numpy.zeros((n,n+1))
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
        mat1[row][col] = float(vals[row][col])    # creating copy of given matrix


# augmented matrix display
print('---------------- Augmented Matrix -----------------')
for row in range(n):
    for col in range(n+1):
        print('%.5f'%mat[row][col],end=' ')
    print('')


naive_gauss(mat)
show(" Naive Gaussian Elimination")

gauss_with_partial_pivoting(mat1)
show(" Gaussian Elimination with Partial Pivoting")