import numpy as np 
import cv2 

img = np.zeros((512,512,3), np.uint8)

# Draw a line starting at (0,0) and ending at (255,255) in blue color (255,0,0), with line width of 5 
img = cv2.line(img, (0,0), (255,255), (255,0,0),5)

# Draw an horizontal arrow starting at (0,255) and ending at (255,255) in green color (0,255,0), with line width of 10 
img = cv2.arrowedLine(img, (0,255), (255,255), (0,255,0), 10)

# Draw a rectangle on the upper right corner (384,0) and (510,128) in filled the area (-1) in red color (0,0,255)
img = cv2.rectangle(img, (384,0), (510,120), (0,0,255), -1)

# Draw a circle center at (447,63) with radius of 55 in green color with line width of 5
img = cv2.circle(img, (447,63), 55, (0,255,0), 5)

# Display "OpenCV" text in yellow color (0,255,255) starting at location (10,500) with defined font, fontsize 3
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "OpenCV", (10,500), font, 3, (0,255,255))

cv2.imshow("image", img)
cv2.waitKey(0) 
cv2.destroyAllWindows()