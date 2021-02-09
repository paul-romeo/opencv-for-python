import cv2
import datetime 

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# Set the video capture at 640x480 resolution at 20 frames per second (fps) 
#   using fourcc video codex and set the saving of content to output.avi 
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480))

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == True: 
        # Display frame size 
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

        # Display datetime 
        dateAndTime = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        frame = cv2.putText(frame, dateAndTime, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)


        out.write(frame)    # write the video capture to output.avi

        # cv2.imshow("frame", frame)  # set frame to color 
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   # press 'q' to exit 
            break 
    else: 
        break 


cap.release()
out.release()
cv2.destroyAllWindows()