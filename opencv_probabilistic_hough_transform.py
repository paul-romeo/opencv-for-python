import cv2 
import numpy as np 

img = cv2.imread("sudoku.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# Step 1: Edge detection 
edges = cv2.Canny(imgray, 50, 150, apertureSize=3)
cv2.imshow("Edges", edges)

# Step 2: Mapping of edge points to Hough space and storage in an accumulator 
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)

# Step 3: Interpretation of the accumulator to yield lines of infinite length using thresholding and other constraints 
for line in lines: 
    x1,y1,x2,y2 = line[0]

    # Step 4: Conversion of infinite lines to finite lines 
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
