import cv2 
import numpy as np 
import matplotlib.pylab as plt


def regionOfInterest(img, vertices):
    mask = np.zeros_like(img)
    # channelCount = img.shape[2]
    matchMaskColor = 255
    cv2.fillPoly(mask, vertices, matchMaskColor)
    maskedImage = cv2.bitwise_and(img, mask)

    return maskedImage 

def drawTheLines(img, lines):
    img = np.copy(img)
    width = img.shape[0]
    height = img.shape[1]
    channelCount = 3  # img in RGB has channelCount of 3 
    blankedImage = np.zeros((width, height, channelCount), dtype=np.uint8)

    # Draw the lines on the blankedImage 
    for line in lines: 
        for x1,y1,x2,y2 in line: 
            cv2.line(blankedImage, (x1,y1), (x2,y2), (255,0,0), thickness=4)
    
    # Add two images (img, and blankedImage). Note that the blankedImage has lines drawn on it now 
    img = cv2.addWeighted(img, 0.8, blankedImage, 1, 0.0)

    return img 

# Read and convert the road1.png image to RGB color format 
image = cv2.imread("road1.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Define the region of interest 
height = image.shape[0]
width = image.shape[1]
regionOfInterestVertices = [
    (0, height),
    (width/2, height/2), 
    (width, height)
]

# Generate the croppedImage from the grayImage 
grayImage = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
cannyImage = cv2.Canny(grayImage, 100, 200)
croppedImage = regionOfInterest(cannyImage, 
        np.array([regionOfInterestVertices], np.int32),)

# Extract lines on the cropped image using the HoughLinesP method  
lines = cv2.HoughLinesP(croppedImage, 
                        rho=6,
                        theta=np.pi/60,
                        threshold=160,
                        lines=np.array([]),
                        minLineLength=40,
                        maxLineGap=25
                        )

# Draw the lines on the RGB colored image 
imageWithLines = drawTheLines(image, lines)

# Display the image 
plt.imshow(imageWithLines)
plt.show()

