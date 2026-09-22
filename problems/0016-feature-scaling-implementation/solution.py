import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    mean_data = data.mean(axis=0)
    std_data = data.std(axis=0)

    standardized_data = (data - mean_data)/std_data

    normalized_data = (data - np.min(data, axis=0))/(np.max(data, axis=0)-np.min(data, axis=0))


    return standardized_data, normalized_data