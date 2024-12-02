import numpy as np
import matplotlib.pyplot as plt

# Activation function: Sigmoid


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Derivative of the sigmoid function


def sigmoid_derivative(x):
    return x * (1 - x)


# Initialize the network
np.random.seed(42)  # For reproducibility
input_layer_size = 3  # Number of input features
hidden_layer_size = 4  # Number of neurons in the hidden layer
output_layer_size = 1  # Number of output neurons

# Randomly initialize weights and biases
weights_input_hidden = np.random.rand(input_layer_size, hidden_layer_size)
bias_hidden = np.random.rand(hidden_layer_size)

weights_hidden_output = np.random.rand(hidden_layer_size, output_layer_size)
bias_output = np.random.rand(output_layer_size)

# Input data (features)
X = np.array([[0.1, 0.2, 0.3],
              [0.4, 0.5, 0.6],
              [0.7, 0.8, 0.9]])

# Target data (labels)
y = np.array([[0.3], [0.7], [1.0]])

# Learning rate
learning_rate = 0.1

# Forward propagation


def forward_propagation(X):
    # Input to hidden layer
    z_hidden = np.dot(X, weights_input_hidden) + bias_hidden
    a_hidden = sigmoid(z_hidden)

    # Hidden to output layer
    z_output = np.dot(a_hidden, weights_hidden_output) + bias_output
    a_output = sigmoid(z_output)

    return z_hidden, a_hidden, z_output, a_output

# Backward propagation


def backward_propagation(X, y, z_hidden, a_hidden, z_output, a_output):
    global weights_input_hidden, bias_hidden, weights_hidden_output, bias_output

    # Error in output
    output_error = a_output - y
    output_delta = output_error * sigmoid_derivative(a_output)

    # Error in hidden layer
    hidden_error = np.dot(output_delta, weights_hidden_output.T)
    hidden_delta = hidden_error * sigmoid_derivative(a_hidden)

    # Update weights and biases
    weights_hidden_output -= learning_rate * np.dot(a_hidden.T, output_delta)
    bias_output -= learning_rate * np.sum(output_delta, axis=0)

    weights_input_hidden -= learning_rate * np.dot(X.T, hidden_delta)
    bias_hidden -= learning_rate * np.sum(hidden_delta, axis=0)

    return np.mean(np.abs(output_error))


# Training the network
epochs = 1000
losses = []  # To store the loss over epochs
weights_hidden_output_history = []  # Track the hidden-to-output weights

for epoch in range(epochs):
    z_hidden, a_hidden, z_output, a_output = forward_propagation(X)
    loss = backward_propagation(X, y, z_hidden, a_hidden, z_output, a_output)
    losses.append(loss)
    # Save a copy of the hidden-to-output weights at each epoch
    weights_hidden_output_history.append(weights_hidden_output.copy())

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss}")

# Final output after training
print("Final Output After Training:")
print(a_output)

# Convert weights history to a NumPy array for plotting
weights_hidden_output_history = np.array(weights_hidden_output_history)

# Plot the loss graph
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(losses, label="Loss")
plt.title("Loss over Epochs")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.grid(True)
plt.legend()

# Plot the weights graph
plt.subplot(1, 2, 2)
for i in range(weights_hidden_output.shape[0]):
    for j in range(weights_hidden_output.shape[1]):
        plt.plot(
            weights_hidden_output_history[:, i, j], label=f'Weight[{i}][{j}]')
plt.title("Weights Evolution")
plt.xlabel("Epochs")
plt.ylabel("Weights")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
