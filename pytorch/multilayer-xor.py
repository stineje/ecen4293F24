import torch
import torch.nn as nn
import torch.optim as optim

# Step 1: Define the XOR dataset
X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
# Output as column vector
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)


class XORMLP(nn.Module):
    """ Step 2: Define a Multi-Layer Perceptron (MLP) """

    def __init__(self):
        super(XORMLP, self).__init__()
        self.hidden = nn.Linear(2, 2)  # Hidden layer: 2 inputs, 2 neurons
        self.output = nn.Linear(2, 1)  # Output layer: 2 inputs, 1 neuron

    def forward(self, x):
        # Apply sigmoid activation in hidden layer
        x = torch.sigmoid(self.hidden(x))
        # Apply sigmoid activation in output layer
        x = torch.sigmoid(self.output(x))
        return x


# Instantiate the model
model = XORMLP()

# Step 3: Define the loss function and optimizer
criterion = nn.BCELoss()  # Binary Cross-Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Step 4: Train the model
epochs = 10000
for epoch in range(epochs):
    optimizer.zero_grad()            # Reset gradients
    outputs = model(X)               # Forward pass
    loss = criterion(outputs, y)     # Compute loss
    loss.backward()                  # Backpropagation
    optimizer.step()                 # Update weights

    # Print progress every 1000 epochs
    if (epoch + 1) % 1000 == 0:
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# Step 5: Test the model
with torch.no_grad():  # No gradient tracking for inference
    predictions = model(X)
    predictions_binary = (predictions > 0.5).float()
    print("\nPredictions:")
    print(predictions)
    print("Binary Predictions:")
    print(predictions_binary)
