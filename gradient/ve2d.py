import matplotlib.pyplot as plt
import torch
import numpy as np
from matplotlib.animation import FuncAnimation

def value(x, y):
    return 2*pow(x,2)- pow(y,2)+ 6*y
def chieu(a,b,c,d,diem):
    outputx = None
    outputy = None
    x,y = diem
    if y > d:
        outputy = d
        if x  > b:
            outputx = b
        elif x < a:
            outputx = a
        else:
            outputx =  x 
        
    elif y < c:
        outputy = c
        if x  > b:
            outputx = b
        elif x < a:
            outputx = a
        else:
            outputx =  x 
        
    else:
        outputy = y
        if x  > b:
            outputx = b
        elif x < a:
            outputx = a
        else:
            outputx =  x 
            
    return outputx,outputy
    
# Create a grid of x and y values
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
x, y = np.meshgrid(x, y)

# Compute the z values
z = value(x, y)

# Plot the contour
fig, ax = plt.subplots()
contour = ax.contour(x, y, z, cmap='viridis')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_title('Contour Plot with Gradient Descent Path')

# Gradient descent parameters
x_torch = torch.tensor(0.0, requires_grad=True)
y_torch = torch.tensor(0.1, requires_grad=True)

lr = 0.08

x_list = []
y_list = []
x_list.append(3)
y_list.append(2)
# Gradient descent loop
for i in range(20):
    z_torch = value(x_torch, y_torch)
    z_torch.backward()
    
    with torch.no_grad():
        x_torch -= lr * x_torch.grad
        y_torch -= lr * y_torch.grad
        # x_new,y_new = chieu(-5,0,-5,0,(x_torch.item(),y_torch.item()))
        x_new ,y_new = x_torch.item(),y_torch.item()
        x_list.append(x_new)
        y_list.append(y_new)
    
    # Zero the gradients
    x_torch.grad.zero_()
    y_torch.grad.zero_()

# Plotting the gradient descent path
path, = ax.plot([], [], 'ro-', markersize=5)

def update(num, x_list, y_list, path):
    path.set_data(x_list[:num], y_list[:num])
    return path,
# x = np.linspace(-5,0,100)
# y = np.linspace(-5,0,100)
# x,y = np.meshgrid(x,y)
# plt.scatter(x,y)
ani = FuncAnimation(fig, update, frames=len(x_list), fargs=(x_list, y_list, path), interval=100, repeat=True)

plt.show()
