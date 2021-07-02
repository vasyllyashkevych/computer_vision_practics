from PIL import Image
import numpy as np


class ImageFlipping:
    """
        Image flipping class.
    @param isHorizontally:
        Allow flipping horizontally.
    @param isVertically:
        Allow flipping vertically.
    """

    isHorizontally: bool
    isVertically: bool

    def __init__(self, vertically: bool, horizontally: bool):
        self.isVertically = vertically
        self.isHorizontally = horizontally

    def flip(self, image: Image) -> list:
        """
            Flip the given image according to the defined parameters.
        @param image: The image in Pillow  format.
        :return:
            A list of the flipped images in numpy format.
        """
        list_of_flipped = []

        if self.isVertically:
            list_of_flipped.append(image.transpose(Image.FLIP_TOP_BOTTOM))
        if self.isHorizontally:
            list_of_flipped.append(image.transpose(Image.FLIP_LEFT_RIGHT))
        return list_of_flipped
