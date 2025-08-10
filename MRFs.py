import cv2
import numpy as np
import datetime
import os
from sklearn.cluster import KMeans

# Set input and output sonar file directories
input_dir = 'sonar'
output_kmeans_dir = 'output_kmeans_processed'
output_mrf_dir = 'output_mrf'

os.makedirs(output_kmeans_dir, exist_ok=True)
os.makedirs(output_mrf_dir, exist_ok=True)

filelist = [f for f in os.listdir(input_dir) if f.endswith('.jpg')]

total_time = 0
processed_images = 0


def gaussian_pdf(mean, std, x):
    """Compute Gaussian probability density (with small epsilon to avoid division by zero)"""
    std = max(std, 1e-6)
    return (1.0 / (np.sqrt(2 * np.pi) * std)) * np.exp(-0.5 * ((x - mean) / std) ** 2)


def run_kmeans(img_gray, n_clusters=2):
    """Perform KMeans clustering on grayscale sonar image"""
    flat_pixels = img_gray.flatten().reshape(-1, 1)
    kmeans = KMeans(n_clusters=n_clusters, n_init=10)
    labels = kmeans.fit_predict(flat_pixels)
    return labels.reshape(img_gray.shape)


def initialize_statistics(img_gray, labels, n_clusters):
    """Compute initial mean and std per class"""
    mean_list = []
    std_list = []

    for k in range(n_clusters):
        mask = (labels == k)
        pixels = img_gray[mask]
        if len(pixels) == 0:
            mean, std = 0, 1
        else:
            mean = pixels.mean()
            std = pixels.std() if pixels.std() > 0 else 1e-6
        mean_list.append(mean)
        std_list.append(std)

    return mean_list, std_list


def mrf_smoothing(img_gray, init_labels, n_clusters, max_iter=3):
    """Apply MRF-based smoothing"""
    labels = init_labels.copy()
    height, width = labels.shape

    for iteration in range(max_iter):
        mean_list, std_list = initialize_statistics(img_gray, labels, n_clusters)
        new_labels = labels.copy()

        for i in range(1, height - 1):
            for j in range(1, width - 1):
                probs = []
                for k in range(n_clusters):
                    # Count neighbor agreement
                    neighborhood = labels[i-1:i+2, j-1:j+2]
                    prior = np.sum(neighborhood == k)
                    likelihood = gaussian_pdf(mean_list[k], std_list[k], img_gray[i, j])
                    probs.append(np.exp(prior) * likelihood)

                new_labels[i, j] = np.argmax(probs)

        labels = new_labels
        print(f"MRF iteration {iteration + 1} completed")

    return labels


for filename in filelist:
    start_time = datetime.datetime.now()
    name_base = os.path.splitext(filename)[0]
    filepath = os.path.join(input_dir, filename)

    # Load and preprocess image
    img = cv2.imread(filepath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) / 255.0

    # KMeans segmentation
    labels_kmeans = run_kmeans(gray, n_clusters=2)

    # Invert black/white: class 0 -> 255, class 1 -> 0
    kmeans_binary = np.where(labels_kmeans == 0, 255, 0).astype(np.uint8)
    kmeans_path = os.path.join(output_kmeans_dir, name_base + '.jpg')
    cv2.imwrite(kmeans_path, kmeans_binary)

    # MRF optimization
    labels_mrf = mrf_smoothing(gray, labels_kmeans, n_clusters=2, max_iter=3)
    mrf_binary = np.where(labels_mrf == 0, 0, 255).astype(np.uint8)
    mrf_path = os.path.join(output_mrf_dir, name_base + '.jpg')
    cv2.imwrite(mrf_path, mrf_binary)

    # Time logging
    elapsed = (datetime.datetime.now() - start_time).total_seconds()
    total_time += elapsed
    processed_images += 1
    print(f"{filename} done in {elapsed:.2f}s")

print(f"\nAverage processing time: {total_time / processed_images:.3f} seconds/image")
