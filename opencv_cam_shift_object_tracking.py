import numpy as np 
import cv2 

cap = cv2.VideoCapture("slow_traffic_small.mp4")

# 1. Take the first frame of video 
ret, frame = cap.read()

# 2. Setup the initial location of window 
x,y,width, height = 300, 200, 100, 50 
track_window = (x,y,width,height)

# 3. Setup the region of input (roi) for tracking 
roi = frame[y:y+height, x:x+width]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0.,60.,32.)), np.array((180.,255.,255)))
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# cv2.imshow("Region of Interest", roi)

# 4. Setup the termination criteria: 10 iterations or move by at least 1 point 
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while (1): 
    ret, frame = cap.read()
    if ret == True: 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)

        # Apply the meanshift method to get the new location 
        ret, track_window = cv2.CamShift(dst, track_window, term_crit)

        # Draw it on the image 
        pts = cv2.boxPoints(ret)
        pts = np.int0(pts)
        final_image = cv2.polylines(frame, [pts], True, (0,255,0), 2)

            
        cv2.imshow("dst", dst)
        cv2.imshow("Final Image", final_image)


        key_pressed = cv2.waitKey(30) & 0xFF 
        if key_pressed == 27: 
            break 
    else: 
        break 
