from Getpath import *
from resize import *
from Savepath import *
from tkinter import *


#Opening file using a simple Tkinter GUI 
root = Tk()
button = Button(root, text="Open Image", command=openImage)
button.pack()
root.mainloop()