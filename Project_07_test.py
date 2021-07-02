import os
import unittest
from Project_07 import VideoFraming


class VideoFramingTestCase(unittest.TestCase):

    video = VideoFraming()

    def test_video_framing_execution(self):
        """ Test if denoising condition is switched on.
        """
        source = os.getcwd() + "/test_videos/vid1.avi"
        destination = os.getcwd() + "/test_videos/vid1.avi"
        file_name_template = os.getcwd() + "/test_videos/vid1/test1_%d.jpg"
        self.assertTrue(self.video.get_destination_frames(source=source, destination=destination, file_name_template=file_name_template))


if __name__ == '__main__':
    unittest.main()