import cv2 
import numpy as np 

img = cv2.imread("smarties.png")
output = img.copy()

# Create the gray image, then blur this image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# Detect all circles on the gray image 
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1,20,param1=50, param2=30, minRadius=0, maxRadius=0)
detected_circles = np.uint16(np.around(circles))


# Mark the circles and their center on the output image 
for (x,y,r) in detected_circles[0,:]:
    cv2.circle(output, (x,y), r, (0,0,0), 3)  # mark the circle in black
    cv2.circle(output, (x,y), 2, (0,255,255), 3)    # mark its center in yellow 

cv2.imshow("Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

