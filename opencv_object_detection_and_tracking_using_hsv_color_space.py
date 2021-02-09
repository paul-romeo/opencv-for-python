import cv2 
import numpy as np 

def nothing(x):
    print(x)

#  Use the camera capture 
captured = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("LH", "Tracking",0,255,nothing)
cv2.createTrackbar("LS", "Tracking",0,255,nothing)
cv2.createTrackbar("LV", "Tracking",0,255,nothing)

cv2.createTrackbar("UH", "Tracking",255,255,nothing)
cv2.createTrackbar("US", "Tracking",255,255,nothing)
cv2.createTrackbar("UV", "Tracking",255,255,nothing)

while (True):
    # Read and display the smarties.png 
    # frame = cv2.imread("smarties.png")
    _, frame = captured.read()


    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get trackbar positions for lower (hue, saturation, value)
    #   and for upper (hue, saturation, value)
    lower_hue = cv2.getTrackbarPos("LH", "Tracking")
    lower_saturation = cv2.getTrackbarPos("LS", "Tracking")
    lower_value = cv2.getTrackbarPos("LV", "Tracking")

    upper_hue = cv2.getTrackbarPos("UH", "Tracking")
    upper_saturation = cv2.getTrackbarPos("US", "Tracking")
    upper_value = cv2.getTrackbarPos("UV", "Tracking")

    lower_bound = np.array([lower_hue, lower_saturation, lower_value])
    upper_bound = np.array([upper_hue, upper_saturation, upper_value])

    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    result = cv2.bitwise_and(frame, frame, mask=mask)

    

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)      

    key = cv2.waitKey(1)
    if key == 27: 
        break 

captured.release()
cv2.destroyAllWindows()
