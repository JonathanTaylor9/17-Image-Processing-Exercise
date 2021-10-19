import cv2

img = cv2.imread("galaxy.jpg", 0)  # import the galaxy.jpg file

# resizes image to half original size
resized_image = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))
# displays resized image in window titled "Galaxy"
cv2.imshow("Galaxy", resized_image)
# saves resized image as 'Galaxy_Resized.jpg'
cv2.imwrite("Galaxy_Resized.jpg", resized_image)
# possibility to show image for period of time - currently displays until closed by user
cv2.waitKey(0)
# closes image window; used in conjunction with waitKey command above
cv2.destroyAllWindows()