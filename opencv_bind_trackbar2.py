import numpy as np 
import cv2 

def nothing(x):
    print(x)

# Create a black window image 
# img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow("image")

# Create a trackbar 'CP' in the "image" window with range of 10 to 400, callback to nothing 
cv2.createTrackbar('CP', "image", 10, 400, nothing)


# Create trackbar for the switch 
switch = "color/gray"
cv2.createTrackbar(switch, "image", 0,1, nothing)

while (1):
    img = cv2.imread("lena.jpg")
    
    # Get positions of each trackbar 
    pos = cv2.getTrackbarPos("CP", "image")

    font = cv2.FONT_HERSHEY_SIMPLEX
    # put red text "str(pos)" on the image window at location (50,150), fontsize of 6, with lineweight 10
    cv2.putText(img, str(pos), (50,150), font, 6, (0,0,255), 10)

    k = cv2.waitKey(1) & 0xFF 
    if k == 27: 
        break 

    s = cv2.getTrackbarPos(switch, "image")

    if s == 0: 
        pass 
    else: 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.imshow("image", img)

cv2.destroyAllWindows()