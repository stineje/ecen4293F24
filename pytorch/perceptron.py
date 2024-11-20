import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# Step 1: Create a Toy Dataset
# Points in 2D space, labeled as 0 or 1
torch.manual_seed(0)  # For reproducibility
X = torch.randn(100, 2)  # 100 points, 2 features (2D space)
y = (X[:, 0] * X[:, 1] > 0).float()  # Label: 1 if x1*x2 > 0, else 0


class Perceptron(nn.Module):
    """ define the Perceptron model """

    def __init__(self):
        super(Perceptron, self).__init__()
        # Single layer: input size = 2, output size = 1
        self.fc = nn.Linear(2, 1)

    def forward(self, x):
        return torch.sigmoid(self.fc(x))  # Sigmoid for binary classification


model = Perceptron()

# Step 3: Define the Loss and Optimizer
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
# Stochastic Gradient Descent
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Step 4: Train the Perceptron
epochs = 100
losses = []

for epoch in range(epochs):
    optimizer.zero_grad()  # Reset gradients
    y_pred = model(X).squeeze()  # Forward pass
    loss = criterion(y_pred, y)  # Compute loss
    loss.backward()  # Backpropagation
    optimizer.step()  # Update weights

    losses.append(loss.item())  # Record loss for plotting
    if (epoch + 1) % 10 == 0:
        print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item():.4f}")

# Step 5: Visualize the Results
# Plot loss curve
plt.figure(figsize=(8, 4))
plt.plot(range(epochs), losses, label='Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Training Loss')
plt.legend()
plt.show()

# Plot decision boundary
plt.figure(figsize=(8, 8))
with torch.no_grad():
    x1 = torch.linspace(-3, 3, 100)
    x2 = torch.linspace(-3, 3, 100)
    xx, yy = torch.meshgrid(x1, x2)
    grid = torch.cat((xx.reshape(-1, 1), yy.reshape(-1, 1)), dim=1)
    zz = model(grid).reshape(100, 100)

    plt.contourf(xx, yy, zz, levels=50, cmap='RdBu', alpha=0.7)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='RdBu', edgecolor='k', s=50)
    plt.colorbar(label='Prediction Probability')
    plt.title('Decision Boundary')
    plt.show()
