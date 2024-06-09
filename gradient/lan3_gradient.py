import torch
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Define the function
def z_function(x, y):
    return  2*pow(x,2)- pow(y,2)+ 6*y

# Create a grid of x and y values
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
x, y = np.meshgrid(x, y)

# Compute the z values
z = z_function(x, y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.6)

# Set plot labels
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Plot of z = (x-2)^2 - (x-2)(y-2) + 1/2 * (y-2)^2')

# Gradient descent parameters
x_torch = torch.tensor(0.0, requires_grad=True)
y_torch = torch.tensor(-2.0, requires_grad=True)
lr = 0.01

def value(x, y):
    return  2*pow(x,2)- pow(y,2)+ 6*y

x_list = []
y_list = []
z_list = []

# Gradient descent loop
for i in range(15):
    z_torch = value(x_torch, y_torch)
    z_torch.backward()
    
    with torch.no_grad():
        x_torch -= lr * x_torch.grad
        y_torch -= lr * y_torch.grad

    # Track the values
        x_list.append(x_torch.item())
        y_list.append(y_torch.item())
        z_list.append(value(x_torch,y_torch).item())

    # Zero the gradients
    x_torch.grad.zero_()
    y_torch.grad.zero_()
    x_torch.requires_grad_(True)  
    y_torch.requires_grad_(True)

# Plotting the gradient descent path
path, = ax.plot([], [], [], color='r', marker='o')

    
def update(num, x_list, y_list, z_list, path):
    path.set_data(x_list[:num], y_list[:num])
    path.set_3d_properties(z_list[:num])
    return path

ani = FuncAnimation(fig, update, frames=len(x_list), fargs=(x_list, y_list, z_list, path), interval=100, blit=False)

plt.show()
