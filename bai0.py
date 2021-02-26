
import cv2 as cv
import numpy as np

# read image
image1 = cv.imread('image/image1.jpg')

# image2Resize = cv.resize(image1, (960, 540))

# show image

# cv.imshow("original image", image3)
# cv.waitKey(0)

# ROI

# roi = cv.selectROI(image1)
# print rectangle points of selected roi
# print(roi)

# Crop selected roi from raw image
# roi_cropped = image1[int(roi[1]):int(roi[1]+roi[3]),
#                      int(roi[0]):int(roi[0]+roi[2])]

# show cropped image
# cv.imshow("ROI", roi_cropped)

# cv.imwrite("crop.jpeg", roi_cropped)

# hold window
# cv.waitKey(0)
# cv.destroyAllWindows()


# change gray image

# gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)

# cv.imshow("Gray image", gray)
# cv.waitKey(0)
# cv.destroyAllWindows()
