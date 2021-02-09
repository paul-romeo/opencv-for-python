import numpy as np 
import cv2 

img = cv2.imread("messi5.jpg")
img2 = cv2.imread("opencv-logo.png")

print(img.shape)    # tuple of numbers of rows, columns, and channels 
print(img.size)     # numbers of pixels 
print(img.dtype)    # img datatype 

b,g,r = cv2.split(img)
img1 = cv2.merge((b,g,r))

# Duplicate the ball at different location of img1 
ball = img1[280:340, 330:390]
img1[273:333, 100:160] = ball 

# Resize both images to the same size 
img1 = cv2.resize(img1, (512,512))
img2 = cv2.resize(img2, (512,512))

# Add two images with weighted percentage 
dst = cv2.addWeighted(img1, 0.85, img2, 0.15, 0)

cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()