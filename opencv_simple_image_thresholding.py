import cv2 as cv 
import numpy as np 

img = cv.imread("gradient.png")

# Set simple binary and binary invert thresholds 
_, threshold_binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, threshold_binary_invert = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, threshold_binary_1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, threshold_binary_invert_1 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)

# Set simple truncate threshold 
_, threshold_truncate = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)

# Set simple tozero threshold 
_, threshold_to_zero = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, threshold_to_zero_invert = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)


# Display the original and threshold images 
cv.imshow("Image", img)
cv.imshow("threshold_binary", threshold_binary)
cv.imshow("threshold_binary_invert", threshold_binary_invert)

cv.imshow("threshold_binary_1", threshold_binary_1)
cv.imshow("threshold_binary_invert_1", threshold_binary_invert_1)

cv.imshow("threshold_truncate", threshold_truncate)

cv.imshow("threshold_to_zero", threshold_to_zero)
cv.imshow("threshold_to_zero_invert", threshold_to_zero_invert)

cv.waitKey(0)

cv.destroyAllWindows()