import cv2 
import numpy as np 

img = cv2.imread("sudoku.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img)

# Step 1: Edge detection 
edges = cv2.Canny(imgray, 50, 150, apertureSize=3)

# Step 2: Mapping of edge points to Hough space and storage in an accumulator 
lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

# Step 3: Interpretation of the accumulator to yield lines of infinite length using thresholding and other constraints 
for line in lines: 
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho 
    y0 = b * rho 

    # x1 stores the rounded off value of (r * cos(theta) -1000 * sin(theta))
    x1 = int(x0 + 1000 * (-b))

    # y1 stores the rounded off value of (r * sin(theta) -1000 * cos(theta))
    y1 = int(y0 + 1000 * (a))

    # x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta)) 
    x2 = int(x0 - 1000 * (-b))

    # y2 stores the rounded off value of (r * sin(theta) -1000 * cos(theta))
    y2 = int(y0 - 1000 * (a))

    # Step 4: Conversion of infinite lines to finite lines 
    cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow("Hough Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
