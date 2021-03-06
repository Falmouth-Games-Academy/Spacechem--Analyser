import numpy as np
import cv2
import os
from github import Github

#template folder
TEMPLATE_FOLDER="templates"
#our test image
TEST_IMAGE_NAME="Reactor - A Brief History Of SpaceChem.jpg"
IMAGE_ROOT_DIR="images"
#Threshold
THRESHOLD=0.8
#Image Test Area
IMAGE_TEST_AREA=[110,0,900,640]

#CSV filename
CSV_FILENAME="spacechem.csv"

#GIT_ACCESS_TOKEN="8a5c954f77a2a8c92fb753e9cbcfd305bec9bdfa"
#ORGANIZATION_NAME="Falmouth University Games Academy"
#REPO_NAME="comp110-worksheets"

def readTemplateFiles(templateDirectory):
    templateDict={}
    for currentFile in os.listdir( templateDirectory ):
        template = cv2.imread(templateDirectory+"\\"+currentFile,0)
        name=currentFile.split('.')[0]
        templateDict[name]=template

    return templateDict

def getTestImagesFromRepo():
    g = Github(GIT_ACCESS_TOKEN)
    for org in g.get_user().get_orgs():
        if (org.name==ORGANIZATION_NAME):
            for fork in org.get_repo(REPO_NAME).get_forks():
                print fork.id


def main():
    CSVString=""
    img = cv2.imread(TEST_IMAGE_NAME,0)
    #populate the templates list from the directory
    #and load each one
    templates=readTemplateFiles(TEMPLATE_FOLDER)
    for key,value in templates.iteritems():
        CSVString+=key
        CSVString+=","
    CSVString+="\n"

    #loop through each template and check to see if we get a match
    for key,value in templates.iteritems():
        currentCount=0
        res = cv2.matchTemplate(img,value,cv2.TM_CCOEFF_NORMED)
        #width and height of the template
        w, h = value.shape[::-1]
        #check to see if the result is in a certain threshold
        loc = np.where( res >= THRESHOLD)
        for pt in zip(*loc[::-1]):
            #draw rectanges for each match that is in the test area
            if ((pt[0]>IMAGE_TEST_AREA[0]) and (pt[0]<IMAGE_TEST_AREA[2]) and (pt[1]>IMAGE_TEST_AREA[1]) and (pt[1]<IMAGE_TEST_AREA[3])):
                cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255),2)
                currentCount+=1
        CSVString+=str(currentCount)
        CSVString+=","

    f=open(CSV_FILENAME,"w")
    f.write(CSVString)
    f.close()

    #show image in a window
    cv2.imshow('image',img)
    #wait for any key to be pressed
    cv2.waitKey(0)
    #destroy window
    cv2.destroyAllWindows()

#main method, called when this file is executed
if __name__ == '__main__':
  main()
