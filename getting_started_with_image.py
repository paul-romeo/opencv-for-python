import cv2 
img = cv2.imread("lena.jpg", -1)    # 0: B&W, 1: color, 2: color + alpha
print(img)

# Display the image 
cv2.imshow("image", img)
k = cv2.waitKey(5000)  

cv2.imwrite("lena_copy.png", img) 


print(f'value of k: {k}')
if k == 27: 
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("lena_copy.png", img)   # write img to a new file 
    cv2.destroyAllWindows()


