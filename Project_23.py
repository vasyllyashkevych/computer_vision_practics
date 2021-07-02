from PIL import Image, ImageEnhance
import cv2 as cv2
import numpy as np


class ImageFiltering:
    """
        Image filtering class.
    @param isDenoising:
        Allow denoise filtering.
    @param isDilation:
        Allow dilation filtering.
    @param isContrasting:
        Allow contrasting filtering.
    """

    isDenoising: bool
    isDilation: bool
    isContrasting: bool

    def __init__(self, denoising: bool, dilation: bool, contrasting: bool):
        self.isDenoising = denoising
        self.isDilation = dilation
        self.isContrasting = contrasting

    def filter(self, image: Image) -> list:
        """
            Flip the given image according to the defined parameters.
        @param image: The image in Pillow  format.
        :return:
            A list of the flipped images in numpy format.
        """
        list_of_filtered = []

        # Denoising
        if self.isDenoising:
            list_of_filtered.append(Image.fromarray(cv2.fastNlMeansDenoisingColored(np.array(image), None, 13, 10, 5, 21)))

        # Dilation
        if self.isDilation:
            kernel = np.ones((3, 3), np.uint8)
            list_of_filtered.append(Image.fromarray(cv2.dilate(np.array(image), kernel, iterations=1)))

        # Contrasting
        if self.isContrasting:
            list_of_filtered.append(ImageEnhance.Contrast(image).enhance(1))

        return list_of_filtered
