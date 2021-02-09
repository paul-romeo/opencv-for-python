import cv2 as cv 
import numpy as np 

img = cv.imread("sudoku.png", cv.IMREAD_GRAYSCALE)

_, threshold_binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,11,2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)


# Display the original and threshold images 
cv.imshow("Original", img)
cv.imshow("threshold_binary", threshold_binary)
cv.imshow("adaptive_mean_c", th2)
cv.imshow("adaptive_gaussian_c", th3)

cv.waitKey(0)

cv.destroyAllWindows()