import cv2
import imutils
import numpy as np


class ImageDistance:
    """
        A class for calculation a distance to the object on the image.
    @param _known_width:
        Object width in inches.
    @param _known_distance:
        Distance in inches from camera to object, but it is known from camera's specification.
    @param _focal_length:
        Focal length - the distance to the marker from the camera.
    """
    _known_width: float
    _known_distance: float
    _focal_length: float

    def __init__(self, image: np.ndarray, known_width: float, known_distance: float):
        self._known_width = known_width
        self._known_distance = known_distance
        self._focal_length = self.get_focal_length(image)

    @staticmethod
    def find_marker(image: np.ndarray):
        """
            Finds the biggest object in the picture, convert the image to grayscale, blur it and detect edges.
        @param image:
            Input image in numpy format.
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(gray, 35, 125)

        # Find the contours in the edged image and keep the largest one.
        # We'll assume that this is our piece of paper in the image
        cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts, key = cv2.contourArea)

        # Compute the bounding box of the of the paper region and return it
        return cv2.minAreaRect(c)

    def get_focal_length(self, image: np.ndarray):
        """
            Find the marker in the image, then compute the distance to the marker from the camera.
        @param image:
            Input image in numpy format.
        @return:
            A calculated focal length.
        """
        marker = self.find_marker(image)
        return (marker[1][0] * self._known_distance) / self._known_width

    def get_distance(self, image: np.ndarray, is_drawn: bool):
        """
            Calculates distance between camera and object
        @param image:
            An input image.
        @param is_drawn:
            Ability to draw boundary box around the object.
        @return:
            A calculated distance of the object to the camera.
        """
        marker = self.find_marker(image)
        distance = (self._known_width * self._focal_length) / marker[1][0]

        if not is_drawn:
            return distance, np.zeros([10, 10, 3], dtype=np.uint8)
        else:
            # Draw a bounding box around the image and display it
            box = np.int0(cv2.boxPoints(object))
            cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
            cv2.putText(image, "%.4fft" % (distance / 12),
                        (image.shape[1] - 300, image.shape[0] - 20),
                        cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), 3)
            return distance, image