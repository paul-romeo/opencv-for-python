import cv2
# from matplotlib import pyplot as plt 
import matplotlib.pylab as plt
import numpy as np

image = cv2.imread("road1.png")

# Convert the image to RGB type 
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]


region_of_interest_vertices = [
    (0, height),
    (width/2, height/2), 
    (width, height)
]

def regionOfInterest(img, vertices):
    mask = np.zeros_like(img)
    newvariable516 = channel_count
    newvariable516 = img.shape[2]
    match_mask_color = (255,) * newvariable516
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)

    return masked_image 


cropped_image = regionOfInterest(image, np.array([region_of_interest_vertices], np.int32),)

plt.imshow(cropped_image)


plt.show()

