
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Step 1: Generate 400 2D Gaussian distributed data points
np.random.seed(42)
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # Identity covariance matrix
data = np.random.multivariate_normal(mean, cov, 400)

# Random stretching/compression
stretch_matrix = np.array([[2, 0], [0, 0.5]])
stretched_data = data @ stretch_matrix.T

# Step 2: Perform PCA
pca = PCA(n_components=2)
pca_data = pca.fit_transform(stretched_data)
principal_axes = pca.components_

# Plot the original data and principal components
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(stretched_data[:, 0], stretched_data[:, 1], alpha=0.6, label="Data points")
origin = np.mean(stretched_data, axis=0)
for length, vector in zip(pca.explained_variance_, principal_axes):
    plt.quiver(*origin, *(vector * length * 3), color="red", scale=1, scale_units="xy", angles="xy")
plt.title("Original Data with Principal Components")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.legend()

# Step 3: Compress data to 1D and reconstruct to 2D
compressed_data = pca.transform(stretched_data)[:, :1]  # Keep only the first principal component
reconstructed_data = pca.inverse_transform(np.hstack([compressed_data, np.zeros_like(compressed_data)]))

# Plot the reconstructed data
plt.subplot(1, 2, 2)
plt.scatter(reconstructed_data[:, 0], reconstructed_data[:, 1], alpha=0.6, label="Reconstructed Data (1D)")
plt.title("Reconstructed Data in 2D Space")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis("equal")
plt.legend()

plt.tight_layout()
plt.show()
