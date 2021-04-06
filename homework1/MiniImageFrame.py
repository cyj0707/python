import matplotlib.pylab as plt
import cv2
import numpy as np

class PImage:
    # import image
    def __init__(self,ImagePath):
        self.im = cv2.imread(ImagePath)
        self.Image_Width,self.Image_Height,self.RGBLength= self.im.shape
    # show Image
    def showImg(self):
        plt.imshow(self.im)
        plt.axis('off')
        plt.show()
    # show gray Image
    def showGrayImg(self):
        plt.imshow(self.im,cmap='gray')
        plt.axis('off')
        plt.show()
    def GetWidth(self):
        return self.Image_Width
    def GetHeight(self):
        return self.Image_Height
    def GetPixelAt(self,x,y):
        return self.im[x,y]
    # set pixel
    def SetPixelAt(self,x,y,c):
        self.im[x,y] = c
    # restore color
    def reColor(self):
        self.im=cv2.cvtColor(self.im,cv2.COLOR_BGR2RGB)
    # blur
    def blur(self):
        self.im=cv2.GaussianBlur(self.im,(7,7),3)
    # grayscale
    def gray(self):
        self.im=cv2.cvtColor(self.im,cv2.COLOR_BGR2GRAY)
    # edge detection
    def canny(self):
        self.im=cv2.Canny(self.im,180,200)
    # grab cut
    def grabCut(self):
        mask = np.zeros(self.im.shape[:2],np.uint8)
        bgdModel = np.zeros((1,65),np.float64)
        fgdModel = np.zeros((1,65),np.float64)
        rect = (50,50,450,290)
        cv2.grabCut(self.im,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
        mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
        self.im = self.im*mask2[:,:,np.newaxis]
    im = []
    Image_Width = 0
    Image_Height = 0
    RGBLength = 3