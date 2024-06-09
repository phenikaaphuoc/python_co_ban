import torch

x = torch.tensor(10.0, requires_grad=True)
lr = 0.3

def grad_compute(x):
    q = x**2
    q.backward()
    return x.grad

for i in range(100):
    grad = grad_compute(x)
    with torch.no_grad():  # Temporarily disable gradient tracking
        x -= lr * grad
    print(x.item())  # .item() is used to print the scalar value of the tensor
    print(grad.item())
    x.requires_grad_(True)  # Re-enable gradient tracking
    x.grad.zero_()  # Reset the gradient to zero
