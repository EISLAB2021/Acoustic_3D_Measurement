###################################################################################
##### Quantitative 3D Spatial Occupancy Measurement ####
###################################################################################

def calculate_volume_similarity_rate(true_dims: tuple, predicted_bbox_dims: tuple) -> float:
    """
    Compute the volumetric similarity between the ground-truth seafloor object and the predicted bounding box.
    The output is always capped between 0 and 100%.

    Args:
        true_dims (tuple): Ground truth seafloor object dimensions (length, width, height) in consistent units.
        predicted_bbox_dims (tuple): Predicted bounding box dimensions (length, width, height) in the same units.

    Returns:
        float: Volume similarity as a percentage (0–100%).

    Raises:
        ValueError: If either true or predicted volume is zero (invalid for comparison).
    """
    if len(true_dims) != 3 or len(predicted_bbox_dims) != 3:
        raise ValueError("Input dimensions must be 3-element tuples: (length, width, height)")

    true_l, true_w, true_h = true_dims
    pred_l, pred_w, pred_h = predicted_bbox_dims

    # Compute volumes of the seafloor object
    true_volume = true_l * true_w * true_h
    pred_volume = pred_l * pred_w * pred_h

    if true_volume <= 0 or pred_volume <= 0:
        raise ValueError("Both true and predicted volumes must be greater than zero.")

    # Compute similarity rate: smaller volume divided by larger volume
    similarity = (min(true_volume, pred_volume) / max(true_volume, pred_volume)) * 100
    return similarity


# Example usage
if __name__ == "__main__":
    true_dims = (190, 190, 28)          # Ground truth object size (LWH)
    predicted_dims = (180, 200, 29)     # Predicted bounding box size (LWH)

    similarity_rate = calculate_volume_similarity_rate(true_dims, predicted_dims)
    print(f"Volume Similarity Rate: {similarity_rate:.2f}%")
