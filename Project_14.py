import numpy as np
import cv2 as cv2
import os


class FaceDetection(object):
    def __init__(self, video):
        print(os.getcwd())
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.eyes_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        self.images = self.split_video(video)
        self.isFace, self.photo, self.frame, self.sqf, self.sqe = self.get_face()

    def split_video(self, path):
        """
            Function to extract frames
        :param path:
        :return:
        """
        vidObj = cv2.VideoCapture(path)
        images = []

        # Used as counter variable
        count = 0

        # checks whether frames were extracted
        success = 1

        while success:
            # vidObj object calls read
            # function extract frames
            success, image = vidObj.read()

            # Saves the frames with frame-count
            # cv2.imwrite("frame%d.jpg" % count, image)
            images.append(image)
            count += 1
        return images

    def get_face(self):
        minEyes = 0.0
        minFace = 0.0
        frontalFace = None
        valid = False

        for img in self.images:
            if not isinstance(img, np.ndarray):
                continue
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                # squareFace = w * h
                # if minFace > squareFace:
                #     continue
                # else:
                #     minFace = squareFace
                #     frontalFace = img

                #cv2.rectangle(self.image,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                cv2.rectangle(roi_color, (x, y), (x + w, y + h), (155, 127, 255), 2)

                # Detects eyes of different sizes in the input image
                eyes = self.eyes_cascade.detectMultiScale(roi_gray)

                # To draw a rectangle in eyes
                for (ex, ey, ew, eh) in eyes:
                    squareEye = ew * eh
                    if minEyes > squareEye:
                        continue
                    else:
                        minEyes = squareEye
                        frontalFace = img
                        valid = True
                        # cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
                        #cv2.imshow("ss", roi_color)
                        #cv2.waitKey(0)

        # return valid, roi_color, frontalFace, minFace, minEyes
        return valid, roi_color, frontalFace, minFace, minEyes

    def get_notification(self):
        # self.isFace, self.photo, self.frame, self.sqf, self.sqe
        notification = ""
        squareFrame = self.frame.shape[0] * self.frame.shape[1]
        print("SquareFrame : ", squareFrame)
        print("SquareFace : ", self.sqe)

        if self.sqe / squareFrame < 0.001:
            notification = "Be close to camera front"
        elif self.sqe / squareFrame > 0.05:
            notification = "Be far from camera front"
        else:
            notification = "Good position"
        return notification


# # Tests
# video_path = "video.avi"
# p = FaceDetection(video_path)
# print(p.get_notification())
# if p.isFace:
#     cv2.imshow('ResultsFrame', p.frame)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
# else:
#     print(p.isFace)

