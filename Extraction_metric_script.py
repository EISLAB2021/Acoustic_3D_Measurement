####################################################################################
##### Quantitative evaluation of the extraction accuracy of acoustic cast shadows ##
####################################################################################
import os
import cv2
import csv
import numpy as np
from tqdm import tqdm


def cal_dice(gt: np.ndarray, pred: np.ndarray) -> float:
    """
    Compute DICE coefficient (also called: F1-score).
    """
    intersection = np.logical_and(gt == 255, pred == 255).sum()
    total = (gt == 255).sum() + (pred == 255).sum()
    return 2 * intersection / total if total != 0 else 0.0


def cal_precision(gt: np.ndarray, pred: np.ndarray) -> float:
    """
    Compute precision score of acoustic shadow extraciton.
    """
    tp = np.logical_and(gt == 255, pred == 255).sum()
    fp = (pred == 255).sum()
    return tp / fp if fp != 0 else 0.0


def cal_recall(gt: np.ndarray, pred: np.ndarray) -> float:
    """
    Compute recall score of acoustic shadow extraction.
    """
    tp = np.logical_and(gt == 255, pred == 255).sum()
    fn = (gt == 255).sum()
    return tp / fn if fn != 0 else 0.0


def calculate_iou(gt: np.ndarray, pred: np.ndarray) -> float:
    """
    Compute Intersection over Union (IoU).
    """
    intersection = np.logical_and(gt == 255, pred == 255).sum()
    union = np.logical_or(gt == 255, pred == 255).sum()
    return intersection / union if union != 0 else 0.0


def process_images(folder_pred: str, folder_gt: str, output_csv: str) -> None:
    """
    Compare predicted masks with ground truth masks and compute evaluation metrics.

    Args:
        folder_pred (str): Path to predicted binary masks.
        folder_gt (str): Path to ground truth binary masks.
        output_csv (str): Path to save evaluation results.
    """
    pred_files = {os.path.splitext(f)[0]: f for f in os.listdir(folder_pred)}
    gt_files = {os.path.splitext(f)[0]: f for f in os.listdir(folder_gt)}

    results = []

    for base_name in tqdm(pred_files, desc="Evaluating", unit="image"):
        if base_name not in gt_files:
            print(f"[WARNING] Ground truth not found for {base_name}")
            continue

        pred_path = os.path.join(folder_pred, pred_files[base_name])
        gt_path = os.path.join(folder_gt, gt_files[base_name])

        # Load grayscale images
        img_pred = cv2.imread(pred_path, cv2.IMREAD_GRAYSCALE)
        img_gt = cv2.imread(gt_path, cv2.IMREAD_GRAYSCALE)

        # Convert to binary using OTSU
        _, bin_pred = cv2.threshold(img_pred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        _, bin_gt = cv2.threshold(img_gt, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        dice = cal_dice(bin_gt, bin_pred)
        precision = cal_precision(bin_gt, bin_pred)
        recall = cal_recall(bin_gt, bin_pred)
        iou = calculate_iou(bin_gt, bin_pred)

        results.append([base_name, dice, precision, recall, iou])

    # Save results to CSV
    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Image Name', 'DICE', 'Precision', 'Recall', 'IoU'])
        writer.writerows(results)

    print(f"\n[INFO] Evaluation completed. Results saved to: {output_csv}")


if __name__ == '__main__':
    # Example paths – update these with actual folders
    folder_pred = ''  # predicted
    folder_gt = '' # GT
    output_csv = 'Evaluation_results.csv'

    process_images(folder_pred, folder_gt, output_csv)
