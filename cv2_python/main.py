import cv2 
large_image = cv2.imread(r"D:\download\large_image.jpg")[100:324,100:324,:]
small_image = cv2.resize(cv2.imread(r"D:\download\small_image.jpg"),(224,224))
gray_image = cv2.cvtColor(small_image,cv2.COLOR_BGR2GRAY)

thresold  = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 4)
thresold_inv = cv2.bitwise_not(thresold)
small_image = cv2.bitwise_and(small_image,small_image,mask=thresold_inv)
large_image = cv2.bitwise_and(large_image, large_image,mask=thresold)+small_image
cv2.imshow("thresold",thresold)
cv2.imshow("inv_thresold",thresold_inv)
cv2.imshow("small_image",small_image)
cv2.imshow("large_image",large_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
