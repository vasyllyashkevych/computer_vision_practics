import os
import unittest
from PIL import Image

from Project_23 import ImageFiltering


class ImageFilteringTestCase(unittest.TestCase):

    image = Image.open(os.getcwd() + "/tests/test.jpg")
    model = ImageFiltering(True, True, True)

    def test_denoising_conditions(self):
        """ Test if denoising condition is switched on.
        """
        filters = ImageFiltering(denoising=True, dilation=False, contrasting=False)
        self.assertTrue(filters.isDenoising and not filters.isDilation and not filters.isContrasting)

    def test_dilation_conditions(self):
        """ Test if dilation condition is switched on.
        """
        filters = ImageFiltering(denoising=False, dilation=True, contrasting=False)
        self.assertTrue(not filters.isDenoising and filters.isDilation and not filters.isContrasting)

    def test_contrasting_conditions(self):
        """ Test if contrasting condition is switched on.
        """
        filters = ImageFiltering(denoising=False, dilation=False, contrasting=True)
        self.assertTrue(not filters.isDenoising and not filters.isDilation and filters.isContrasting)

    def test_all_conditions(self):
        """ Test if all conditions are switched on.
        """
        self.assertTrue(self.model.isDenoising and self.model.isDilation and self.model.isContrasting)

    def test_all_filters_implementation(self):
        """ Test if all filters are implemented.
        """
        self.assertEqual(len(self.model.filter(self.image)), 3)


if __name__ == '__main__':
    unittest.main()