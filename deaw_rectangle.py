import cv2
import numpy as np
from PIL import Image


def draw_rectangle():
    # Reading an image in default mode
    image = np.zeros([300, 300, 3])

    # Window name in which image is displayed
    window_name = 'Image'

    # Start coordinate, here (5, 5)
    # represents the top left corner of rectangle
    start_point = (5, 5)

    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    end_point = (220, 220)

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    image = cv2.rectangle(image, start_point, end_point, color, thickness)

    # Displaying the image
    Image.fromarray(image.astype(np.uint8)).show()


def main():
    draw_rectangle()


if __name__ == '__main__':
    main()
