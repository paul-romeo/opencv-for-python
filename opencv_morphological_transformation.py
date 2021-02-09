import cv2 
import numpy as np 

from matplotlib import pyplot as plt

# Read the img and convert to gray scale 
img = cv2.imread("smarties.png", cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)
dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)

# Morphological Transformations 
# opening applies erosion 1st, then dilation later 
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# closing applies dilation 1st, then erosion later 
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

# top_hat applies the difference between the original and opening
top_hat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)

# Setup the titles and images 
titles = ["Image", "mask", "dilation", "erosion", "opening", "closing", "gradient", "top hat"]
images = [img, mask, dilation, erosion, opening, closing, gradient, top_hat]

# Display the plots 
for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()