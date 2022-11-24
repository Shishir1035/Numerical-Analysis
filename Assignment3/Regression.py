import matplotlib.pyplot as plt
def Regression(x, y):
    n = len(x)
    xsum = sum(x)
    ysum = sum(y)
    xx = [i*i for i in x]
    xxsum = sum(xx)
    xysum = 0

    for i in range(n):
        xysum += x[i] * y[i]
    
    a1 = (n * xysum - xsum * ysum) / (n * xxsum - xsum**2)
    a0 = (xxsum * ysum - xsum*xysum) / (n * xxsum - xsum**2)
    
    return a0, a1
# ----------------------------------------- code starts from here ----------------------------
size = int(input("Number of x,y pair as input : "))
xlist = [float(i) for i in input("Enter the "+str(size)+" values of x : ").split()]
ylist = [float(i) for i in input("Enter the "+str(size)+" values of y : ").split()]

a0,a1 = Regression(xlist, ylist)
t = []
for i in range(5):
    t.append(a0+a1*xlist[i])

plt.plot(xlist,t)
plt.title("Regression")
plt.xlabel("X")
plt.xlabel("Y")
plt.show()