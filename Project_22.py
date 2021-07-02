import numpy as np, cv2

img1 = cv2.imread('../../images/images/1.jpg', 0)
img2 = cv2.imread('../../images/images/2.jpg', 0)
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
vis = np.zeros((max(h1, h2), w1+w2), np.uint8)
vis[:h1, :w1] = img1
vis[:h2, w1:w1+w2] = img2
vis = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

cv2.imshow("test", vis)
cv2.waitKey()


'''
#To verify
import cv2
import numpy as np
img = cv2.imread('img.png')
vis = np.concatenate((img1, img2), axis=1)
cv2.imwrite('out.png', vis)
'''
