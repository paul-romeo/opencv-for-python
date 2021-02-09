import numpy as np 
import cv2 

# Display all events in cv2 
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)