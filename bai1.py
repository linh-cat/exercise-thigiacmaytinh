import cv2 as cv

image_name = input("Image Name: ")

img = cv.imread(image_name)

cv.imshow("anh goc: ", img)
cv.waitKey(4)

[w, h] = img.shape[:2]
for i in range(w):
    for j in range(h):
        img[i][j] = 255 - img[i][j]
cv.imshow("anh am bang", img)
cv.waitKey()
# anh am bang la anh 255 - cho cac diem anh
