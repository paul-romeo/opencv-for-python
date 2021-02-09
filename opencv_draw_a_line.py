import numpy as np 
import cv2 

def click_event(event, x, y, flags, param): 
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Left mouse button clicked event 
    if event == cv2.EVENT_LBUTTONDOWN: 
        # Draw a small circle as point 
        cv2.circle(img, (x,y), 3, (0,0,255), -1)

        # Draw a line in blue color connecting the last two points with lineweight of 5
        points.append((x,y))
        if len(points) >= 2: 
            cv2.line(img, points[-1], points[-2], (255,0,0), 5)
        cv2.imshow("image", img)


# Display a black background 
img = np.zeros((512,512,3), np.uint8)
cv2.imshow("image", img)

# Initialize points array 
points = []

# Call click_event 
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)

# Close all windows 
cv2.destroyAllWindows()