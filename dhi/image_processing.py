import cv2
import numpy as np
from matplotlib import pyplot as plt
w=50
h=50
im_arr=[]
def readImages():
    img1=cv2.imread('interferogram01.png',0)
    im_arr.append(img1)
    img2=cv2.imread('interferogram02,png',0)
    im_arr.append(img2)
    img3=cv2.imread('interferogram03.png',0)
    im_arr.append(img3)
    img4=cv2.imshow('interferogram04.png',0)
    im_arr.append(img4)
    return im_arr
def processImage():
    for img in im_arr:
        f=np.fft.fft2(img)
        fshift=np.fft.fftshift(f)
        magnitude_spectrum = 20*np.log(np.abs(fshift))
    return im_arr, magnitude_spectrum

def plot_graphs():

    origIm=plt.subplot(121),plt.imshow(img, cmap='gist_yarg')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    fft_plot=plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='RdPu')
    plt.title('Fourierova transformace'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.xticks([]), plt.yticks([])


    plt.show()