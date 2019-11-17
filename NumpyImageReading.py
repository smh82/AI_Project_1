import numpy as np
import matplotlib.pylab as plt
from PIL import Image
import os 

def getFiles(rootDir):
    for dirName, subdirList, fileList in os.walk(rootDir):
        print("Found directory : %s" %dirName)
        fileCount = len(fileList)
        print (fileCount)
        for fname in fileList:
            print("\t : %s " %fname)
    return fileList , dirName , fileCount

def reSizeImages(fileList, dirName):
    for i in fileList:
        img = Image.open( dirName  +"\\"+ i )                               # image extension *.png,*.jpg
        new_width  = 512
        new_height = 512
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        img.save("Resize_" + i)                                         # format may what u want ,*.png,*jpg,*.gif
 
def InsertIntoNpArray(fileCount,photos):
    for i in range(1,fileCount+1):
    #      print("file"+str(i)+".png")  
        im= plt.imread("Resize_file"+str(i)+".png")
        print(type(im))
        print(im.shape)
        photos[i]=im
    #     print(im)


def bridge():
    fileList, dirName, fileCount = getFiles(".\images")
    print(fileList)
    print(dirName)
    print(fileCount)
    reSizeImages(fileList,dirName)
    photos = np.zeros([fileCount+1,512,512,3])
    InsertIntoNpArray(fileCount,photos)



if __name__ == "__main__" :
    bridge()


