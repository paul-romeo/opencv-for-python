import cv2 as cv 
from matplotlib import pyplot as plt 

img = cv.imread("gradient.png", 0)

# Convert the img to RGB format 
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Set simple binary and binary invert thresholds 
_, threshold_binary = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
_, threshold_binary_invert = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
_, threshold_truncate = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, threshold_to_zero = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, threshold_to_zero_invert = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

titles = ["ORIGINAL", "BINARY", "BINARY_INVERT", "TRUNCATE", "TOZERO", "TOZERO_INVERT"]
images = [img, threshold_binary, threshold_binary_invert,threshold_truncate, threshold_to_zero, threshold_to_zero_invert]

# Display the img using matplotlib 
for i in range(6):
    plt.subplot(2,3, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

# plt.imshow(img)

# # Hide the plot ticks 
# plt.xticks([]), plt.yticks([])
# plt.show()

# cv.waitKey(0)
# cv.destroyAllWindows()
