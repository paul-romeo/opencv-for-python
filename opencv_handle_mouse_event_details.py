import numpy as np 
import cv2 

def click_event(event, x, y, flags, param): 
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Left mouse button clicked event 
    if event == cv2.EVENT_LBUTTONDOWN: 
        print(x, ', ', y)

        # Put text string (x,y) at location (x,y) using font at fontsize in cyan color, with lineweight 2 
        strXY = "(" + str(x) + ", " + str(y) + ")"
        cv2.putText(img, strXY, (x,y), font, .5, (255,255,0), 2)

    # Right mouse button clicked event 
    if event == cv2.EVENT_RBUTTONDOWN: 
        print(x, ', ', y)
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        
        strBGR = "(" + str(blue) + ", " + str(green) + ", " + str(red) + ")"
        cv2.putText(img, strBGR, (x,y), font, .5, (0,255,255), 2)

    cv2.imshow("image", img)


# Display "lena.jpg" as the background image 
img = cv2.imread("lena.jpg")
cv2.imshow("image", img)

# Call click_event 
cv2.setMouseCallback("image", click_event)
cv2.waitKey(0)

# Close all windows 
cv2.destroyAllWindows()