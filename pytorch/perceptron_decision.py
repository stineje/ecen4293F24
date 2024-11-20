import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Step 1: Create a synthetic dataset
X, y = make_classification(
    n_samples=1000,  # Number of samples
    n_features=2,    # Number of features for easy visualization
    n_informative=2,  # Number of informative features
    n_redundant=0,   # No redundant features
    n_clusters_per_class=1, random_state=42
)

# Step 2: Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)

# Step 3: Train decision tree classifiers with different splitting criteria
criteria = ['gini', 'entropy']  # Supported criteria
models = {}
for criterion in criteria:
    tree = DecisionTreeClassifier(
        criterion=criterion, max_depth=3, random_state=42)
    tree.fit(X_train, y_train)
    models[criterion] = tree

# Step 4: Evaluate and visualize each model
for criterion, tree in models.items():
    y_pred = tree.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy with {criterion.capitalize()} criterion: {accuracy:.2f}")

    plt.figure(figsize=(12, 8))
    plot_tree(tree, feature_names=['Feature 1', 'Feature 2'], class_names=[
              'Class 0', 'Class 1'], filled=True)
    plt.title(f"Decision Tree ({criterion.capitalize()} Criterion)")
    plt.show()


def calculate_classification_error(probabilities):
    """ Step 5: Add Classification Error as Custom Criterion (Manually Calculated) """
    return 1 - np.max(probabilities)


def plot_decision_boundary_and_error(tree, X, y, criterion):
    """ Plot decision boundary and manually calculate the error """
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.Paired)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=plt.cm.Paired)
    plt.title(f"Decision Boundary ({criterion.capitalize()} Criterion)")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()


# Plot for Gini, Entropy, and Classification Error
for criterion, tree in models.items():
    plot_decision_boundary_and_error(tree, X_test, y_test, criterion)
