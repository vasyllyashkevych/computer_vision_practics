import cv2 as cv2
import os


class VideoFraming:
    def __init__(self):
        pass

    def get_frames(self, source: str) -> list:
        """
            Split a source video by frames.
        @param source:
            A path to the source video file.
        @return:
            A list of frames in np.ndarray format.
        """
        frames = []
    
        video = cv2.VideoCapture(source)
        is_next_frame = True
    
        while is_next_frame:
            is_next_frame, frame = video.read()
            frames.append(frame)
    
        video.release()
        return frames
    
    def get_destination_frames(self, source: str, destination: str, file_name_template: str) -> bool:
        """
            Catch a video file and split it by frames.
        @param source:
            A path to the source video file.
        @param destination:
            A folder for frame saving.
        @param file_name_template:
            A template of the file name with extra digit from counter.
        :return:
            True / False - results of the execution.
        """

        # Check if the target folder exists
        try:
            if not os.path.exists(destination):
                os.makedirs(destination)
        except OSError:
            return False

        try:
            video = cv2.VideoCapture(source)
            success = True
            count = 0
            while success:
                success, image = video.read()
                cv2.imwrite(destination + file_name_template % count, image)
                count += 1
            return True
        except:
            return False


source = "test_videos/vid1.avi"
destination = "test_videos/vid1"
file_name_template = "test_videos/vid1/test1_%d.jpg"

vf = VideoFraming()
vf.get_frames(source)
vf.get_destination_frames(source=source, destination=destination, file_name_template=file_name_template)