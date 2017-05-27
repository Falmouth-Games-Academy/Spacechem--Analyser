import numpy as np
import cv2
import os

#template folder
TEMPLATE_FOLDER="templates"
#our test image
TEST_IMAGE_NAME="Reactor - A Brief History Of SpaceChem.jpg"

def main():
    img = cv2.imread(TEST_IMAGE_NAME)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #show image in a window
    cv2.imshow('image',img)
    #wait for any key to be pressed
    cv2.waitKey(0)
    #destroy window
    cv2.destroyAllWindows()

#main method, called when this file is executed
if __name__ == '__main__':
  main()
