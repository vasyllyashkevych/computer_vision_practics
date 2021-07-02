import cv2 as cv2

# cap = cv2.VideoCapture('test_videos/vid1.avi')
cap = cv2.VideoCapture(0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2(varThreshold=1000)

while(1):
	ret, frame = cap.read()
	cv2.imshow('Original', frame)
	fgmask = fgbg.apply(frame)
	
	fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
	cv2.imshow('frame',fgmask)
	
	k = cv2.waitKey(30) & 0xff
	if k == 27:
		break

cap.release()
cv2.destroyAllWindows()
