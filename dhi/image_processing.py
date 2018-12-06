import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

res=np.zeros((2748,3840))
img = cv2.imread('usaf2deg.png',0)
F = np.fft.fft2(img)
fshift = np.fft.fftshift(F)
y,x=F.shape
Xc=1694
Yc=1474
wind=90
start_X=x//2-(Xc//2)
start_Y=y//2-(Yc//2)
F_resized= np.fft.fftshift(F[Yc-wind:Yc+wind, Xc-wind:Xc+wind])

F_mag = np.abs((F_resized))
F_phase = np.angle((F_resized))
F_rephased=np.fft.ifft2(F_phase)
np.real(F_rephased)
magn_plot=plt.subplot(121),plt.imshow(np.log(F_mag), cmap='gist_yarg')
plt.title("|F(k)|")
phase_plot=plt.subplot(122), plt.imshow(F_rephased)
plt.show()
# Fnew_phase = 2.0*math.pi*np.random.rand(F_rephased.shape[0], F_rephase.shape[1])

# magnitude_spectrum = 20*np.log(np.abs(fshift))
# res=res+magnitude_spectrum
# origIm=plt.subplot(121),plt.imshow(img, cmap='gist_yarg')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# fft_plot=plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='RdPu')
# plt.title('Fourierova transformace'), plt.xticks([]), plt.yticks([])
# plt.show()
# #
# Xc=1693
# Yc=1122
# wind=140
# y,x=res.shape
# start_X=x//2-(Xc//2)
# start_Y=y//2-(Yc//2)
# res_im=res[start_Y:start_Y+wind, start_X:start_X+wind]
# # #zoomed fft
# zoomed_plot=plt.plot(), plt.imshow((20*np.log(np.abs(np.fft.fftshift(np.fft.fft2(res_im))))))
# # plt.show()
#
# c2=np.fft.ifft2(np.fft.fftshift(res_im))
# ang=np.angle(c2)
# print(ang)
# f_filtered = np.real(np.fft.ifft2(np.fft.ifftshift(P)))
# print(d=f_filtered)
# plt.imshow(c2)
# # plt.plt.plot, show(phase)
