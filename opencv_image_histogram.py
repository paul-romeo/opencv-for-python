import numpy as np 
import cv2 
from matplotlib import pyplot as plt 

# Create an image of 200x200 with top half of black and bottom half of white 
#  with a small part of gray 
img = np.zeros((200,200), np.uint8)
img = cv2.rectangle(img, (0,100), (200,200), (255), -1)
img = cv2.rectangle(img, (0,50), (100,100), (127), -1)



# Display the history of img (show value of 40,000 at 0)
plt.hist(img.ravel(),256,[0,256])
plt.show()

cv2.imshow("Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()