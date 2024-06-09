import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-0.5,0.5,100)
y = 4*(x**4) -1/2*(x**3)-x**2
def value(x):
    return  4*(x**4) -1/2*(x**3)-x**2
plt.plot(x,y)
x0 = -0.5
def gradient(x):
    return 16*(pow(x,3)) - 3/2*(x**2) - 2*x
def x_new(x_old,lamda,alpha,beta):
    grad = gradient(x_old)
    if value(x_old-lamda*grad) > value(x_old) -lamda*alpha*pow(grad,2):
        lamda = beta*lamda
    return x_old + lamda*grad,grad,lamda

for i in range(25):
    plt.scatter(np.array([x0]),np.array([value(x0)]),color = 'red')
    x_old = x0
    x0,grad,lamda  = x_new(x0,lamda,alpha,beta)
    plt.plot([x_old,x0],[value(x_old),value(x0)],color = "blue")
plt.show()