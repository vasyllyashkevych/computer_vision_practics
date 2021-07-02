# open source: https://github.com/JamzyWang/OD/blob/master/computeDistance.py
#
import unittest
import cv2 as cv2
import numpy as np

from Project_24 import ImageDistance


class ImageCorrelationTestCase(unittest.TestCase):

    image = cv2.imread("tests/test_focal.jpg")
    imageDistance = ImageDistance(image=image, known_width=4.330708661, known_distance=7.874015748)

    def test_instance_creation(self):
        """ Test if instance of class created successfully.
        """
        self.assertTrue(self.imageDistance._known_width == 4.330708661 and
                        self.imageDistance._known_distance == 7.874015748 and
                        self.imageDistance._focal_length == 0.0)

    def test_distance_calculation(self):
        """ Test if distance calculation method is working.
        """
        image = cv2.imread("tests/test_image.jpg")
        self.assertFalse(self.imageDistance.get_distance(image, False)[0], 0.0)

    def test_distance_and_is_drawn(self):
        """ Test if distance calculation method is working.
        """
        image = cv2.imread("tests/test_image.jpg")
        self.assertFalse(self.imageDistance.get_distance(image, True)[1], image.shape)


if __name__ == '__main__':
    unittest.main()