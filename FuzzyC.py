import cv2 as cv
import numpy as np
import math
import matplotlib.pyplot as plt


# Compute squared Euclidean distance between two vectors
def squared_distance(x, y):
    return np.sum((x - y) ** 2)


# Core Fuzzy C-Means clustering update function
def update_centers(img, centers, J_prev, c, b):
    """
    Perform iterative update of cluster centers and membership values
    until convergence of the objective function J.

    Parameters:
    - img: input image as a 3D numpy array (H x W x Channels)
    - centers: current cluster centers (c x Channels)
    - J_prev: previous iteration objective function value
    - c: number of clusters
    - b: fuzziness parameter (>1)

    Returns:
    - centers: updated cluster centers
    - mu: final membership matrix (H x W x c)
    """
    h, w, ch = img.shape
    mu = np.zeros((h, w, c), dtype=np.float64)  # Membership matrix initialization

    while True:
        # Update membership matrix based on current cluster centers
        for i in range(h):
            for j in range(w):
                denominator = 0
                for k in range(c):
                    dist = squared_distance(img[i, j], centers[k])
                    if dist == 0: dist = 1e-10  # Avoid division by zero
                    denominator += (1 / dist) ** (1 / (b - 1))
                for k in range(c):
                    dist = squared_distance(img[i, j], centers[k])
                    if dist == 0: dist = 1e-10
                    mu[i, j, k] = ((1 / dist) ** (1 / (b - 1))) / denominator

        # Update cluster centers based on new membership values
        centers_new = np.zeros_like(centers, dtype=np.float64)
        for k in range(c):
            numerator = np.zeros(ch, dtype=np.float64)
            denominator = 0
            for i in range(h):
                for j in range(w):
                    u_ij = mu[i, j, k] ** b
                    numerator += u_ij * img[i, j]
                    denominator += u_ij
            centers_new[k] = numerator / denominator

        # Compute objective function J for convergence check
        J = 0
        for i in range(h):
            for j in range(w):
                for k in range(c):
                    J += (mu[i, j, k] ** b) * squared_distance(img[i, j], centers_new[k])

        # Check for convergence based on relative change in J
        if abs(J - J_prev) / J_prev < 0.001:
            break
        centers = centers_new
        J_prev = J

    return centers, mu


# Assign hard labels to each pixel by nearest cluster center
def assign_labels(img, centers, c):
    """
    Generate label map by assigning each pixel to the nearest cluster center.

    Returns:
    - labels: 2D array (H x W) of cluster indices
    """
    h, w, _ = img.shape
    labels = np.zeros((h, w), dtype=int)
    for i in range(h):
        for j in range(w):
            dists = [squared_distance(img[i, j], centers[k]) for k in range(c)]
            labels[i, j] = np.argmin(dists)
    return labels


# Remove noise pixels by enforcing neighborhood consistency
def denoise_labels(labels):
    """
    Apply a simple noise reduction method based on 3x3 neighborhood voting.
    Pixels that differ from majority of their neighbors are replaced.

    Returns:
    - labels_denoised: noise-reduced label map
    """
    h, w = labels.shape
    labels_denoised = labels.copy()
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            window = labels[i - 1:i + 2, j - 1:j + 2].flatten()
            center_label = labels[i, j]
            if np.sum(window == center_label) <= 2:  # if center pixel is minority
                unique, counts = np.unique(window, return_counts=True)
                majority_label = unique[np.argmax(counts)]
                labels_denoised[i, j] = majority_label
    return labels_denoised


if __name__ == "__main__":
    # Number of clusters and fuzziness parameter
    c = 2
    b = 2
    J_initial = 1e10  # Initialize objective function with a large value

    # Read input sonar image and convert to float64 for calculations
    img = cv.imread('sonar.jpg').astype(np.float64)

    h, w, ch = img.shape

    # Initialize cluster centers randomly within the image color range
    centers = np.random.rand(c, ch) * 255

    # Run FCM clustering to update cluster centers and membership matrix
    centers, mu = update_centers(img, centers, J_initial, c, b)

    print("Cluster centers (RGB): ")
    print(centers.astype(int))

    # Assign hard labels based on final cluster centers
    labels = assign_labels(img, centers, c)

    # Remove noise using neighborhood voting
    labels_denoised = denoise_labels(labels)

    # Generate segmented image from labels and cluster centers
    segmented_img = np.zeros_like(img, dtype=np.uint8)
    for k in range(c):
        segmented_img[labels_denoised == k] = centers[k].astype(np.uint8)

    # Display original and segmented sonar images side by side
    plt.subplot(1, 2, 1)
    plt.title("Original Sonar Image")
    plt.imshow(cv.cvtColor(img.astype(np.uint8), cv.COLOR_BGR2RGB))

    plt.subplot(1, 2, 2)
    plt.title("Segmented Sonar Image")
    plt.imshow(cv.cvtColor(segmented_img, cv.COLOR_BGR2RGB))

    plt.show()
