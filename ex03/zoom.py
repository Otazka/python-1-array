import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        image_path = "animal.jpeg"
        img_array = ft_load(image_path)

        if img_array is None:
            return

        print(img_array)

        # 2. Zoom by slicing the array (Targeting a 400x400 region)
        # Note: You can adjust these coordinates based on your image size
        start_y, end_y = 100, 500
        start_x, end_x = 300, 700

        # Check bounds to make sure the crop is valid
        if end_y > img_array.shape[0] or end_x > img_array.shape[1]:
            start_y, end_y = 0, 400
            start_x, end_x = 0, 400

        # Slice the region and keep a single channel to get the (400, 400, 1) shape
        zoomed_array = img_array[start_y:end_y, start_x:end_x, 0:1]

        print(f"New shape after slicing: {zoomed_array.shape}")
        print(zoomed_array)

        # 3. Display the image with X and Y axis scales visible
        # np.squeeze removes the single-dimensional entry so matplotlib can map it to gray
        plt.imshow(np.squeeze(zoomed_array), cmap="gray")
        plt.title("Zoomed Image")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
