import cv2
import os

# Global variables for ROI selection via mouse events
roi_corners = []
drawing = False
roi_selected = False


def draw_roi(event, x, y, flags, param):
    """
    Mouse callback function to interactively select a rectangular ROI on the sonar image.

    Parameters:
        event: OpenCV mouse event type
        x, y: Mouse coordinates
        flags: Event flags (not used)
        param: Additional parameters (not used)
    """
    global roi_corners, drawing, roi_selected

    if event == cv2.EVENT_LBUTTONDOWN:
        # Start drawing ROI rectangle
        drawing = True
        roi_corners = [(x, y)]

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        # Update the second corner of the rectangle during mouse move
        roi_corners[1:] = [(x, y)]

    elif event == cv2.EVENT_LBUTTONUP:
        # Finish drawing ROI rectangle on sonar image
        drawing = False
        roi_corners[1:] = [(x, y)]
        roi_selected = True


def adaptive_threshold_segmentation(image, block_size=3, C=2):
    """
    Perform adaptive mean thresholding to segment image regions.

    Parameters:
        image (np.ndarray): Input BGR image or ROI
        block_size (int): Size of pixel neighborhood for adaptive thresholding (must be odd)
        C (int): Constant subtracted from the mean (threshold adjustment)

    Returns:
        thresholded (np.ndarray): Binary inverted thresholded image (foreground=white)
    """
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresholded = cv2.adaptiveThreshold(
        gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, block_size, C
    )
    return thresholded


# ------------------------
# Interactive ROI selection
# ------------------------
image_path = 'sonar.jpg'
image = cv2.imread(image_path)
output_image = image.copy()

cv2.namedWindow("Original Image")
cv2.setMouseCallback("Original Image", draw_roi)

while True:
    temp_image = output_image.copy()

    # Draw ROI rectangle if defined
    if len(roi_corners) == 2:
        cv2.rectangle(temp_image, roi_corners[0], roi_corners[1], (0, 255, 0), 2)

    cv2.imshow("Original Image", temp_image)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("s") and roi_selected:
        # Apply adaptive threshold to selected ROI
        x1, y1 = roi_corners[0]
        x2, y2 = roi_corners[1]

        roi = image[y1:y2, x1:x2]
        thresholded_roi = adaptive_threshold_segmentation(roi)

        # Overlay thresholded ROI on output image
        output_image[y1:y2, x1:x2] = cv2.cvtColor(thresholded_roi, cv2.COLOR_GRAY2BGR)

        cv2.imshow("Segmented ROI", output_image)
        cv2.imwrite('../../result.png', output_image)

    elif key == ord("q"):
        # Exit program
        break

cv2.destroyAllWindows()


# ------------------------------------------
# Batch adaptive threshold segmentation script
# ------------------------------------------
def batch_adaptive_segmentation(input_folder='demo-crop', output_folder='adaptive_seg'):
    """
    Apply adaptive threshold segmentation to all sonar images in the input folder,
    saving results in the output folder.

    Parameters:
        input_folder (str): Directory path containing input sonar images.
        output_folder (str): Directory path to save segmented sonar images.
    """
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.png', '.jpeg', '.bmp', '.tif')):
            input_path = os.path.join(input_folder, filename)
            image = cv2.imread(input_path)

            if image is None:
                print(f"Cannot read image: {filename}")
                continue

            thresholded = adaptive_threshold_segmentation(image)
            result_image = cv2.cvtColor(thresholded, cv2.COLOR_GRAY2BGR)
            output_path = os.path.join(output_folder, filename)
            cv2.imwrite(output_path, result_image)
            print(f"Processed and saved: {output_path}")

# To run batch processing, uncomment below and specify folders
# batch_adaptive_segmentation('demo-crop', 'adaptive_seg')
