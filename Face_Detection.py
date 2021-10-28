import cv2

# create object containing xml file data
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("face_photo.jpg")  # import image file

# convert to grayscale (aids recognition performance)
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(
    gray_image,
    scaleFactor=1.05,
    minNeighbors=5)  # detect the face, to 5% accuracy checking

for x, y, w, h in faces:
    # create green rectangle around detected face, 3 pixel wide box
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

print(type(faces))
print(faces)

cv2.imshow("Gray", img)  # display image with box
cv2.waitKey(0)
cv2.destroyAllWindows()
