import cv2

img=cv2.imread("galaxy.jpg",0) #import the galaxy.jpg file

resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2))) #resizes image to 1000*500 pixels
cv2.imshow("Galaxy",resized_image) #displays resized image in window titled "Galaxy"
cv2.imwrite("Galaxy_Resized.jpg", resized_image)
cv2.waitKey(0) #possibility to show image for period of time - currently permanently
cv2.destroyAllWindows() #closes image window; used in conjunction with waitKey command above
