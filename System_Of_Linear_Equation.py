import numpy

def naive_gauss():
    global mat
    global roots
    # Naive Gaussian Elimination
    for i in range(n):
        if mat[i][i] == 0.0:
            print('Divide by zero !')
            # quit()
            
        for j in range(i+1, n):
            div = mat[j][i]/mat[i][i]
            
            for k in range(n+1):
                mat[j][k] = mat[j][k] - div * mat[i][k]
    back_sub()

def back_sub():
    global mat
    global roots
    roots[n-1] = mat[n-1][n]/mat[n-1][n-1]

    for i in range(n-2,-1,-1):
        roots[i] = mat[i][n]
        for j in range(i+1,n):
            roots[i] = roots[i] - mat[i][j]*roots[j]
        roots[i] = roots[i]/mat[i][i]


# ---------------------- code starts from here -------------------------
n = int(input('Number of equations: '))
# n*(n+1) matrix .. 1 extra column for values of that equation
mat = numpy.zeros((n,n+1))
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
        mat[row][col] = int(vals[row][col])

# augmented matrix display
print('---------------- Augmented Matrix -----------------')
for row in range(n):
    for col in range(n+1):
        print('%.5f'%mat[row][col],end=' ')
    print('')

naive_gauss()
print("\nUsing Naive Gaussing elimination , the Unknown values are : ")
for i in range(0,n):
    print('X'+str(i), ' : ',roots[i])