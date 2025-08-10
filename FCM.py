import numpy as np
import cv2
import os


def euclidean_dist_squared(a, b):
    """
    Compute squared Euclidean distance between two vectors.

    Parameters:
        a (np.ndarray): Vector or array.
        b (np.ndarray): Vector or array.

    Returns:
        float: Squared Euclidean distance.
    """
    return np.sum((a - b) ** 2)


def initialize_membership(height, width, c):
    """
    Initialize fuzzy membership matrix with Dirichlet distribution.

    Parameters:
        height (int): Image height.
        width (int): Image width.
        c (int): Number of clusters.

    Returns:
        np.ndarray: Membership matrix of shape (height, width, c).
    """
    mu = np.random.dirichlet(np.ones(c), size=(height * width))
    return mu.reshape(height, width, c)


def update_cluster_centers(img, mu, c, b):
    """
    Update cluster centers based on current membership matrix.

    Parameters:
        img (np.ndarray): Input image normalized to [0,1], shape (H, W, C).
        mu (np.ndarray): Membership matrix, shape (H, W, c).
        c (int): Number of clusters.
        b (float): Fuzziness exponent (>1).

    Returns:
        np.ndarray: Updated cluster centers, shape (c, channels).
    """
    h, w, ch = img.shape
    img_flat = img.reshape(-1, ch)
    mu_flat = mu.reshape(-1, c)

    m = np.zeros((c, ch), dtype=np.float32)
    for k in range(c):
        u_b = mu_flat[:, k] ** b
        m[k] = np.sum(u_b[:, None] * img_flat, axis=0) / np.sum(u_b)
    return m


def update_membership(img, m, c, b):
    """
    Update fuzzy membership matrix based on current cluster centers.

    Parameters:
        img (np.ndarray): Input image normalized to [0,1].
        m (np.ndarray): Current cluster centers.
        c (int): Number of clusters.
        b (float): Fuzziness exponent.

    Returns:
        np.ndarray: Updated membership matrix.
    """
    h, w, ch = img.shape
    img_flat = img.reshape(-1, ch)
    dist = np.zeros((h * w, c), dtype=np.float32)

    # Compute squared distance to each cluster center
    for k in range(c):
        diff = img_flat - m[k]
        dist[:, k] = np.sum(diff ** 2, axis=1) + 1e-6  # add small epsilon to avoid division by zero

    mu_new = np.zeros_like(dist)
    # Update membership values according to fuzzy c-means formula
    for k in range(c):
        mu_new[:, k] = 1.0 / np.sum((dist[:, k][:, None] / dist) ** (1 / (b - 1)), axis=1)
    return mu_new.reshape(h, w, c)


def segment_image(img, mu):
    """
    Assign each pixel to cluster with highest membership.

    Parameters:
        img (np.ndarray): Input image (unused here but kept for interface consistency).
        mu (np.ndarray): Membership matrix.

    Returns:
        np.ndarray: Hard cluster labels, shape (H, W).
    """
    labels = np.argmax(mu, axis=2)
    return labels


def remove_noise(labels, c):
    """
    Post-processing to remove noise by majority voting in 3x3 neighborhood.

    Parameters:
        labels (np.ndarray): Cluster labels.
        c (int): Number of clusters (unused here but kept for interface).

    Returns:
        np.ndarray: Denoised cluster labels.
    """
    h, w = labels.shape
    labels_denoised = labels.copy()
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            window = labels[i - 1:i + 2, j - 1:j + 2].flatten()
            center = labels[i, j]
            # If center pixel label is not the majority in neighborhood, replace with majority label
            if np.sum(window == center) <= 2:
                unique, counts = np.unique(window, return_counts=True)
                majority = unique[np.argmax(counts)]
                labels_denoised[i, j] = majority
    return labels_denoised


def process_single_image(img_path, c=2, b=2, max_iter=20):
    """
    Process a single image with fuzzy c-means segmentation.

    Parameters:
        img_path (str): Input image filepath.
        c (int): Number of clusters.
        b (float): Fuzziness parameter.
        max_iter (int): Maximum iterations.

    Returns:
        np.ndarray or None: Output segmented RGB image or None if failed.
    """
    img = cv2.imread(img_path)
    if img is None:
        print(f"Warning: Cannot read image: {img_path}")
        return None

    # Normalize image to [0, 1]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB).astype(np.float32) / 255.0
    h, w, _ = img.shape
    mu = initialize_membership(h, w, c)

    # Iterate update of cluster centers and memberships
    for _ in range(max_iter):
        m = update_cluster_centers(img, mu, c, b)
        mu = update_membership(img, m, c, b)

    labels = segment_image(img, mu)
    labels_denoised = remove_noise(labels, c)

    # Generate black-white segmented image for visualization
    output_img = np.zeros((h, w, 3), dtype=np.uint8)
    output_img[labels_denoised == 0] = [0, 0, 0]  # black
    output_img[labels_denoised == 1] = [255, 255, 255]  # white
    return output_img


def process_image_folder(input_folder, output_folder, c=2, b=2, max_iter=20):
    """
    Batch process images in folder with fuzzy c-means segmentation.

    Parameters:
        input_folder (str): Folder path with input images.
        output_folder (str): Folder path to save segmented images.
        c (int): Number of clusters.
        b (float): Fuzziness parameter.
        max_iter (int): Maximum iterations.
    """
    os.makedirs(output_folder, exist_ok=True)
    image_extensions = [".jpg", ".png", ".jpeg", ".bmp", ".tif", ".tiff"]

    for fname in os.listdir(input_folder):
        if not any(fname.lower().endswith(ext) for ext in image_extensions):
            continue
        input_path = os.path.join(input_folder, fname)
        output_img = process_single_image(input_path, c, b, max_iter)
        if output_img is not None:
            output_path = os.path.join(output_folder, fname.split('.')[0] + "_FCM_sonar.jpg")
            output_img_bgr = cv2.cvtColor(output_img, cv2.COLOR_RGB2BGR)
            cv2.imwrite(output_path, output_img_bgr)
            print(f"Processed: {fname} → {output_path}")


# Example usage
if __name__ == "__main__":
    input_dir = "sonar_data"
    output_dir = "output_images"
    process_image_folder(input_dir, output_dir, c=2, b=2, max_iter=20)
