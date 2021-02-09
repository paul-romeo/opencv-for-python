import cv2 

img = cv2.imread("shapes.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# cv2.imshow("Image", img)

# Display and label the shapes 
for contour in contours:

    # Draw contour around the shape 
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    cv2.drawContours(img, [approx], 0, (0,0,0), 5)

    # Label the shape 
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3: 
        cv2.putText(img,"Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    elif len(approx) == 4: 
        x1, y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(x) / y
        if aspectRatio >= 0.95 and aspectRatio <= 1.05: 
            cv2.putText(img,"Square", (x1,y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
        else: 
            cv2.putText(img,"Rectangle", (x1,y1), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    elif len(approx) == 5: 
        cv2.putText(img,"Pentagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    elif len(approx) == 10: 
        cv2.putText(img,"Star", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))

    else: 
        cv2.putText(img,"Circle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))



cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
