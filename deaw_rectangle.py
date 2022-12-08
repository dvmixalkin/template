import cv2
import numpy as np
from PIL import Image


def draw_rectangle():
    # Reading an image in default mode
    image = np.ones([300, 300, 3])*255

    # Window name in which image is displayed
    window_name = 'Image'

    # Start coordinate, here (5, 5)
    # represents the top left corner of rectangle
    x_min, y_min = 45, 45

    # Ending coordinate, here (220, 220)
    # represents the bottom right corner of rectangle
    x_max, y_max = 220, 220

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.rectangle() method
    # Draw a rectangle with blue line borders of thickness of 2 px
    image = cv2.rectangle(image, [x_min, y_min], [x_max, y_max], color, thickness)
    'fontScale: Font scale factor that is multiplied by the font-specific base size.'
    cv2.putText(image, 'Fedex', (x_min, y_min - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    # Displaying the image
    Image.fromarray(image.astype(np.uint8)).show()


def main():
    draw_rectangle()


if __name__ == '__main__':
    main()
