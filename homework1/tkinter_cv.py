import tkinter as tk
import tkinter.filedialog as tkfd
from PIL import Image, ImageTk
from MiniImageFrame import *
from getImageFromWeb import *
# build window
window = tk.Tk()
window.title('Image window')
window.geometry('300x200')
# set label
var = tk.StringVar()
l = tk.Label(window, textvariable = var, font=('Arial', 12))
# button functions
def getPFW():
    getImg("http://pic.yxdown.com/list/0_459_1.html")
def image():
    filename = tkfd.askopenfilename()
    img=PImage(filename)
    img.reColor()
    img.showImg()
def blur():
    filename = tkfd.askopenfilename()
    img=PImage(filename)
    img.reColor()
    img.blur()
    img.showImg()
def gray():
    filename = tkfd.askopenfilename()
    img=PImage(filename)
    img.reColor()
    img.gray()
    img.showGrayImg()
def canny():
    filename = tkfd.askopenfilename()
    img=PImage(filename)
    img.reColor()
    img.canny()
    img.showGrayImg()
def grabcut():
    filename = tkfd.askopenfilename()
    img=PImage(filename)
    img.reColor()
    img.grabCut()
    img.showImg()
# set buttons
bu = tk.Button(window, text='get pictures from web', font=('Arial', 12), width=20, height=1, command=getPFW)
b1 = tk.Button(window, text='read image', font=('Arial', 12), width=10, height=1, command=image)
b2 = tk.Button(window, text='blur', font=('Arial', 12), width=10, height=1, command=blur)
b3 = tk.Button(window, text='gray', font=('Arial', 12), width=10, height=1, command=gray)
b4 = tk.Button(window, text='edge', font=('Arial', 12), width=10, height=1, command=canny)
b5 = tk.Button(window, text='grab cut', font=('Arial', 12), width=10, height=1, command=grabcut)
bu.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
l.pack()
# loop
window.mainloop()