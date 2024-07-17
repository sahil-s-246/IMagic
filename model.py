import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import glob
import joblib


def load_and_flatten_image(image_path):
    image = Image.open(image_path)
    image = image.convert("RGB")
    data = np.array(image)
    w, h, d = data.shape
    return data.reshape((w * h, d))


def combine_flattened_images(image_paths):
    combined_data = []
    for path in image_paths:
        flattened_data = load_and_flatten_image(path)
        combined_data.append(flattened_data)
    return np.vstack(combined_data)


if __name__ == "main":
    image_paths = glob.glob("images/*.jpg")[:10]
    combined_data = combine_flattened_images(image_paths)

    # Fit K-means on the combined pixel data
    n_clusters = 16  # Number of colors for compression
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(combined_data)
    joblib.dump(kmeans, "kmeans_model.pkl")