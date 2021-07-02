from PIL import Image
import numpy as np


class ImageRotation:
    """
        Image rotation class.
    @param _list_of_angles:
        Implement rotation for list of degrees.
    """

    _list_of_angles: list

    def __init__(self, angl_list: list):
        self._list_of_angles = angl_list

    def rotate(self, image: Image) -> list:
        """
            Rotate the given image according to the defined parameters.
        @param image: The image in Pillow  format.
        :return:
            A list of the rotated images in numpy format.
        """
        list_of_rotated = []
        image_height, image_width = image.size

        if self._list_of_angles:
            for angle in self._list_of_angles:
                shift = angle * 2
                rotated = np.array(image.rotate(angle))
                shifted = rotated[angle:image_width - shift, angle:image_height - shift]
                list_of_rotated.append(Image.fromarray(shifted).resize((image_width, image_height)))

        return list_of_rotated
