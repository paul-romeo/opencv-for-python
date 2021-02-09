import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Set the video capture at 640x480 resolution at 20 frames per second (fps) 
#   using fourcc video codex and set the saving of content to output.avi 
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))

# while (True):
while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True: 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Display frame size 
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        # Change the frame size to 320 x 240 
        cap.set(3, 320)
        cap.set(4, 240)

        # Display the new frame size 
        print(cap.get(3))
        print(cap.get(4))

        out.write(frame)    # write the video capture to output.avi

        # cv2.imshow("frame", frame)  # set frame to color 
        cv2.imshow("frame", gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):   # press 'q' to exit 
            break 
    else: 
        break 


cap.release()
out.release()
cv2.destroyAllWindows()