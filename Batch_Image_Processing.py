import cv2  # import computer visualisation module
import glob  # import Glob: Filename Pattern Mataching module

images = glob.glob("*.jpg")  # create list of all images in folder

for image in images:
    img = cv2.imread(image, 0)  # read the images starting at list point 0
    re = cv2.resize(img, (100, 100))  # resize the image to 100*100 pixels
    cv2.imshow("Heh", re)  # show the image in a window with title 'heh'
    cv2.waitKey(500)  # wait 0.5 seconds
    cv2.destroyAllWindows()  # close the window
    cv2.imwrite("resized_" + image, re)  # save the file with prefix 'resized_'
