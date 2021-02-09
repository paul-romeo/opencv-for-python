import cv2
import numpy as np 

# The image can be found in https://github.com/opencv/opencv/tree/master/samples/data

# Display the original chessboard image 
img = cv2.imread("chessboard_img.png")
cv2.imshow("Chessboard", img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray, 2, 3, 0.04)
dst = cv2.dilate(dst, None)

# Mark all corners of the image in red 
img[dst > 0.01 * dst.max()] = [0,0,255]

# Display the chessboard image with marked corners 
cv2.imshow("Chessboard with Marked Corners", img)

if cv2.waitKey(0) & 0xFF == 27: 
    cv2.destroyAllWindows()