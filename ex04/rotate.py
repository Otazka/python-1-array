import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        image_path = "animal.jpeg"
        img_array = ft_load(image_path)

        if img_array is None:
            return

        start_y, end_y = 100, 500
        start_x, end_x = 450, 850

        if end_y > img_array.shape[0] or end_x > img_array.shape[1]:
            start_y, end_y = 0, 400
            start_x, end_x = 0, 400

        square_array = img_array[start_y:end_y, start_x:end_x, 0:1]
        print(square_array)

        # 3. Transpose the image manually or using NumPy
        # First, squeeze it to a 2D array (400, 400) to safely perform a standard matrix transpose
        squeezed_array = np.squeeze(square_array)
        height, width = squeezed_array.shape

        transposed_list = [[0 for _ in range(height)] for _ in range(width)]
        for y in range(height):
            for x in range(width):
                transposed_list[x][y] = squeezed_array[y][x]

        transposed_array = np.array(transposed_list)
        print(f"New shape after Transpose: {transposed_array.shape}")
        print(transposed_array)

        # 4. Display the transposed image
        plt.imshow(transposed_array, cmap="gray")
        plt.title("Transposed Image")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
