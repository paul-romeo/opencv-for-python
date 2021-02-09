import cv2 
import numpy as np 

img = cv2.imread("shapes.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect corners using Shi Tomasi corner detector 
corners = cv2.goodFeaturesToTrack(gray, 150, 0.01, 10)
corners = np.int0(corners)

# Mark the corners with a small circle 
for corner in corners: 
    x,y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow("Image with marked corners", img)

if cv2.waitKey(0) & 0xFF == 27: # exit when key 'q' is pressed 
    cv2.destroyAllWindows() 

