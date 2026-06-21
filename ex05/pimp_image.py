import numpy as np
import matplotlib.pyplot as plt

def ft_invert(array)-> array:
    """Inverts the color of the image received."""
    try:
        #8-bit color is: 255 - pixel_value
        inverted = 255 - array.copy()

        plt.imshow(inverted)
        plt.title("Inverted")
        plt.show()
        return inverted
    except Exception as e:
        print(f"Error in ft_invert: {e}")
        return None

def ft_red(array)-> array:
    """Applies a red filter to the image."""
    try:
        red_img = array.copy()
        red_img[:, :, 1] = red_img[:, :, 1] * 0 #green
        red_img[:, :, 2] = red_img[:, :, 2] * 0 #blue

        plt.imshow(red_img)
        plt.title("Red Channel")
        plt.show()
        return red_img
    except Exception as e:
        print(f"Error in ft_red: {e}")
        return None

def ft_green(array)-> array:
    """Applies a green filter to the image."""
    try:
        green_img = array.copy()
        green_img[:, :, 0] = green_img[:, :, 0] - green_img[:, :, 0]  #red
        green_img[:, :, 2] = green_img[:, :, 2] - green_img[:, :, 2]  #blue

        plt.imshow(green_img)
        plt.title("Green Channel")
        plt.show()
        return green_img
    except Exception as e:
        print(f"Error in ft_green: {e}")
        return None

def ft_blue(array)-> array:
    """Applies a blue filter to the image."""
    try:
        blue_img = array.copy()
        blue_img[:, :, 0] = 0 #red
        blue_img[:, :, 1] = 0 #green

        plt.imshow(blue_img)
        plt.title("Blue Channel")
        plt.show()
        return blue_img
    except Exception as e:
        print(f"Error in ft_blue: {e}")
        return None

def ft_grey(array)-> array:
    """Applies a grey filter to the image."""
    try:
        grey_img = array.copy()

        grey_channel = grey_img[:, :, 1]  #green channel as the base luminance
        grey_img[:, :, 0] = grey_channel
        grey_img[:, :, 1] = grey_channel
        grey_img[:, :, 2] = grey_channel

        plt.imshow(grey_img)
        plt.title("Grayscale")
        plt.show()
        return grey_img
    except Exception as e:
        print(f"Error in ft_grey: {e}")
        return None