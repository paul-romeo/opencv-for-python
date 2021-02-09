import numpy as np 
import cv2 
from matplotlib import pyplot as plt 


img = cv2.imread("lena.jpg") 
b,g,r = cv2.split(img)

# Display the history of img, blue, green, red
plt.hist(img.ravel(),256,[0,256])
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])
plt.show()

# Display images 
cv2.imshow("Image", img)
cv2.imshow("Blue", b)
cv2.imshow("Green", g)
cv2.imshow("Red", r)

cv2.waitKey(0)
cv2.destroyAllWindows()