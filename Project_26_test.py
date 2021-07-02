import os
import unittest
import numpy as np
from PIL import Image

from Project_26 import ImageRotation


class ImageRotationTestCase(unittest.TestCase):

    image = Image.open(os.getcwd() + "/tests/test.jpg")
    model = ImageRotation([5, 10, 15, 20], numpy_or_pillow=True)

    def test_rotated_angles(self):
        """ Test if all angles were rotated.
        """
        self.assertEqual(len(self.model.rotate(self.image)), len(self.model._list_of_angles))

    def test_numpy_format(self):
        """ Test if rotated image content is in numpy format.
        """
        self.assertIsInstance(self.model.rotate(self.image)[0], np.ndarray)

    def test_pillow_format(self):
        """ Test if rotated image content is in pillow format.
        """
        self.model.isNumpyOrPillow = False
        self.assertTrue(Image.isImageType(self.model.rotate(self.image)[0]))


if __name__ == '__main__':
    unittest.main()