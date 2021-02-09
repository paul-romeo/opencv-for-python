import numpy as np 
import cv2 

def click_event(event, x, y, flags, param): 
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Left mouse button clicked event 
    if event == cv2.EVENT_LBUTTONDOWN: 
        blue = img[x,y,0]
        green = img[x,y,1]
        red = img[x,y,2]
        # Draw a small red filled circle as point 
        cv2.circle(img, (x,y), 3, (0,0,255), -1)

        # Open a new window using the color of the mouse cursor that clicks
        myColorImage = np.zeros((512,512,3), np.uint8)
        myColorImage[:] = [blue, green, red]


        cv2.imshow("color", myColorImage)


# Display a black background 
img = cv2.imread("lena.jpg")
cv2.imshow("image", img)

# Initialize points array 
points = []

# Call click_event 
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)

# Close all windows 
cv2.destroyAllWindows()