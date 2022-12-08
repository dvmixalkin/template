import cv2
import numpy as np
from PIL import Image


def draw_rectangle(image, box, label, color, thickness, vis=False):
    image_copy = image.copy()
    x_min, y_min, x_max, y_max = box
    image_copy = cv2.rectangle(image_copy, [x_min, y_min], [x_max, y_max], color, thickness)
    image_copy = cv2.putText(image_copy, label, (x_min, y_min - 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
    if vis:
        Image.fromarray(image_copy.astype(np.uint8)).show()
    return image_copy


def main():
    # coordinates
    image = np.ones([300, 300, 3]) * 255
    x_min, y_min, x_max, y_max = 45, 45, 220, 220
    box = [x_min, y_min, x_max, y_max]
    label = 'Fedex'

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2
    draw_rectangle(image, box, label, color, thickness, vis=True)


if __name__ == '__main__':
    main()
