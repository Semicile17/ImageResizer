from tkinter import filedialog
import resize
import Savepath

def openImage():
    filePath = filedialog.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg;*.gif')])
    if filePath:
        print('Image file path:', filePath)
        #Resizes the image with its path saved to the csv file 
        Savepath. SaveImagePathToCsv(filePath)
        resize.resizeImg(filePath)


