import os
import datetime
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn.cluster import KMeans

# Path to the folder containing input sonar images
path1 = r'sonar'

# Path to the output folder for processed images
path2 = r'output_kmeans_processed'

# Create output directory if it doesn't exist
if not os.path.exists(path2):
    os.makedirs(path2)

# List all .jpg image files in the input directory  # default image format
filelist = [f for f in os.listdir(path1) if f.endswith('.jpg')]

total_time = 0
num = 0

# Process each sonar image in the input folder
for item in filelist:
    start_time = datetime.datetime.now()

    name1 = os.path.splitext(item)[0]  # Get filename without extension
    src = os.path.join(path1, item)  # Full path to input image

    # Read image using matplotlib (RGB format)
    img = np.array(mpimg.imread(src))

    # Convert to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Normalize pixel values to [0,1]
    imgGray = imgGray / 255.0

    # Flatten grayscale image to a 1D vector for clustering
    imgpixel = imgGray.flatten().reshape((-1, 1))

    # Apply KMeans clustering with 2 clusters (foreground/background)
    kmeans = KMeans(n_clusters=2, random_state=0)
    label = kmeans.fit(imgpixel)
    imgLabel = np.array(label.labels_).reshape(imgGray.shape)

    end_time = datetime.datetime.now()
    time_consume = (end_time - start_time).total_seconds()
    total_time += time_consume
    num += 1

    print(f"{item} processed in {time_consume:.4f} seconds")

    # Convert label image to 8-bit grayscale image for saving
    imgLabel_uint8 = (imgLabel * 255).astype(np.uint8)

    # Ensure foreground is white and background is black (optional)
    if np.sum(imgLabel_uint8 == 255) < np.sum(imgLabel_uint8 == 0):
        imgLabel_uint8 = 255 - imgLabel_uint8

    # Save the processed binary acoustic image
    dst = os.path.join(path2, name1 + '.jpg')
    cv2.imwrite(dst, imgLabel_uint8)

    # Generate high-resolution output image using matplotlib (optional)
    # fig = plt.figure(frameon=False)
    # ax1 = plt.Axes(fig, [0., 0., 1., 1.])
    # fig.add_axes(ax1)
    # plt.imshow(imgLabel, cmap='gray')
    # plt.axis('off')
    #
    # height, width, _ = img.shape
    # fig.set_size_inches(width / 100.0 / 3.0, height / 100.0 / 3.0)
    # plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
    # plt.margins(0, 0)
    #
    # dst = os.path.join(path2, name1 + '.jpg')
    # plt.savefig(dst, bbox_inches='tight', pad_inches=0.0)
    # plt.close()

# Report average processing time per sonar frame
average_time = total_time / num if num > 0 else 0
print(f"\nProcessed {num} images. Average time per image: {average_time:.4f} seconds")
