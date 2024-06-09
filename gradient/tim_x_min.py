x0 = -1
lamda = -0.3
e = 1e-04
def gradient(x):
    return 2*x
def x_new(x_old,lamda):
    grad = gradient(x_old)
    if abs(grad) < e:
        print(f"Hoi tu o {i}")
        exit()
    return x_old + lamda*grad,grad
for i in range(20):
    print(f"{i} : {x0}")
    print(x0*x0)
    x0,grad  = x_new(x0,lamda)
    print(f"Grad: {grad}")

    