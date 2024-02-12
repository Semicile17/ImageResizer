import cv2 as cv 
#Resizing image (100x100)->dimensions
def resizeImg(imgPath):
    img=cv.imread(imgPath)
    def resize(img):
        imgResized=cv.resize(img,(100,100),interpolation=cv.INTER_CUBIC)
        return imgResized
    imgResized=resize(img)
    cv.imshow('Image',imgResized)

