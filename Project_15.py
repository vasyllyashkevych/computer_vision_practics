import numpy as np
import cv2
from imutils.object_detection import non_max_suppression
import os


class BodyLocation(object):
    def __init__(self, image):
        self.image = image
        self.isBody = None
        self.photo = None
        self.imgs = []
        self.isBody, self.photo, self.imgs = self.getBody()

        # initialize the HOG descriptor/person detector
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def getBody(self):
        imgs = []
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        valid = False
        roi_color = None
        # print(os.getcwd())
        body_cascade = cv2.CascadeClassifier("cascadG.xml")#(os.getcwd() + 'cascadG.xml')
        bodies = body_cascade.detectMultiScale(gray, 1.2, 5)
        print("Bodies : ", len(bodies))

        for (x, y, w, h) in bodies:
            #x -= 20
            #y -= 40
            #w += 40
            #h += 75
            cv2.rectangle(self.image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = self.image[y:y + h, x:x + w]
            imgs.append(roi_color)
            valid = True
            # self.photo = roi_color
        return valid, roi_color, imgs

    def people_detection(self):
        image = imutils.resize(image, width=min(400, image.shape[1]))
        orig = image.copy()

        # detect people in the image
        (rects, weights) = self.hog.detectMultiScale(image, winStride=(4, 4),
                                                padding=(8, 8), scale=1.05)

        # draw the original bounding boxes
        for (x, y, w, h) in rects:
            cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # apply non-maxima suppression to the bounding boxes using a
        # fairly large overlap threshold to try to maintain overlapping
        # boxes that are still people
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        # draw the final bounding boxes
        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)

        # show some information on the number of bounding boxes
        filename = imagePath[imagePath.rfind("/") + 1:]
        print("[INFO] {}: {} original boxes, {} after suppression".format(
            filename, len(rects), len(pick)))

        # show the output images
        cv2.imshow("Before NMS", orig)
        cv2.imshow("After NMS", image)
        cv2.waitKey(0)

# Tests
im = cv2.imread('6.jpg')
p = BodyLocation(im)
#p.people_detection()
if p.isBody:
    cv2.imshow('img', p.photo)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(p.isBody)

