import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('capturedvid.avi',0)

def fourierTransform(img):

    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))

    plt.subplot(121),plt.imshow(img, cmap = 'gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.VideoWriter_fourcc()

def holoTransform(img):
    hologram_r=(np.ifft2(np.fftshift(np.pad(FTh(X,Y)))))