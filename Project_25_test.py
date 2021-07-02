import os
import unittest
from PIL import Image

from Project_25 import ImageFlipping


class ImageFlippingTestCase(unittest.TestCase):

    image = Image.open(os.getcwd() + "/tests/test.jpg")
    model = ImageFlipping(True, True)

    def test_horizontal_conditions(self):
        """ Test if horizontal flipping condition is switched on.
        """
        flipping = ImageFlipping(vertically=False, horizontally=True)
        self.assertTrue(not flipping.isVertically and flipping.isHorizontally)

    def test_vertical_conditions(self):
        """ Test if vertical flipping condition is switched on.
        """
        flipping = ImageFlipping(vertically=True, horizontally=False)
        self.assertTrue(flipping.isVertically and not flipping.isHorizontally)

    def test_all_conditions(self):
        """ Test if all conditions are switched on.
        """
        self.assertTrue(self.model.isVertically and self.model.isHorizontally)

    def test_all_flipping_implementation(self):
        """ Test if all filters are implemented.
        """
        self.assertEqual(len(self.model.flip(self.image)), 2)


if __name__ == '__main__':
    unittest.main()