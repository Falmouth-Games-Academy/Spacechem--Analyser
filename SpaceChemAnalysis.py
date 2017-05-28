import numpy as np
import cv2
import os

#template folder
TEMPLATE_FOLDER="templates"
#our test image
TEST_IMAGE_NAME="Reactor - A Brief History Of SpaceChem.jpg"
#Threshold
THRESHOLD=0.8
#Image Test Area
IMAGE_TEST_AREA=[110,0,900,640]

def main():
    img = cv2.imread(TEST_IMAGE_NAME)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #populate the templates list from the directory
    #and load each one
    templates=[]
    for currentFile in os.listdir( TEMPLATE_FOLDER ):
        template = cv2.imread(TEMPLATE_FOLDER+"\\"+currentFile,0)
        templates.append(template)

    #loop through each template and check to see if we get a match
    for currentTemplate in templates:
        res = cv2.matchTemplate(img_gray,currentTemplate,cv2.TM_CCOEFF_NORMED)
        #width and height of the template
        w, h = currentTemplate.shape[::-1]
        #check to see if the result is in a certain threshold
        loc = np.where( res >= THRESHOLD)
        for pt in zip(*loc[::-1]):
            #draw rectanges for each match that is in the test area
            if ((pt[0]>IMAGE_TEST_AREA[0]) and (pt[0]<IMAGE_TEST_AREA[2]) and (pt[1]>IMAGE_TEST_AREA[1]) and (pt[1]<IMAGE_TEST_AREA[3])):
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255),2)

    #show image in a window
    cv2.imshow('image',img)
    #wait for any key to be pressed
    cv2.waitKey(0)
    #destroy window
    cv2.destroyAllWindows()

#main method, called when this file is executed
if __name__ == '__main__':
  main()
