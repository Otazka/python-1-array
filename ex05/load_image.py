import os
import numpy as np
from PIL import Image

def ft_load(path: str) -> np.ndarray:
    """
    A function that loads an image,
    prints its format, and its pixels
    content in RGB format
    """
    try:

        if not os.path.exists(path):
            raise FileNotFoundError(f"The file '{path}' does not exist.")

        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError("Unsupported file format. Please provide a JPG or JPEG image.")

        with Image.open(path) as img:
            img_rgb = img.convert("RGB")
            img_array = np.array(img_rgb)
            print(f"The shape of image is: {img_array.shape}")

            return img_array

    except Exception as e:
        print(f"Error: {e}")
        return None