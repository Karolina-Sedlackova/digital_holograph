import tkinter as tk
#from __future__ import print_function
from PIL import Image
from PIL import ImageTk
import threading
import datetime
import imutils
import cv2
import os

width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_EXPOSURE,-12)
brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS)
#contrast = cap.get(cv2.CAP_PROP_CONTRAST)
#saturation = cap.get(cv2.CAP_PROP_SATURATION)
#hue = cap.get(cv2.CAP_PROP_HUE)
gain = cap.get(cv2.CAP_PROP_GAIN)
exposure = cap.get(cv2.CAP_PROP_EXPOSURE)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = tk.Label(root)
lmain.pack()

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    print("Brightness: ", brightness)
    #print("Contrast: ", contrast)
    #print("Saturation: ", saturation)
    #print("Hue: ", hue)
    #print("Gain: ", gain)
    print("Exposure: ", exposure)
    return cv2image

def takeSnapshot():
    # grab the current timestamp and use it to construct the
    # output path
    ts = datetime.datetime.now()
    filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
    classpath="C:\\Users\\karol\\PycharmProjets\\dhi"
    p = os.path.sep.join((classpath, filename))

    # save the file
    cv2.imwrite(p)
    print("[INFO] saved {}".format(filename))

show_frame()
takeSnapshot()
root.mainloop()
# class PhotoCapture:
#     def __init__(self, vs, outputPath):
#         # store the video stream object and output path, then initialize
#         # the most recently read frame, thread for reading frames, and
#         # the thread stop event
#         self.vs = vs
#         self.outputPath = outputPath
#         self.frame = None
#         self.thread = None
#         self.stopEvent = None
#
#         # initialize the root window and image panel
#         self.root = tk.Tk()
#         self.panel = None
#         # create a button, that when pressed, will take the current
#         # frame and save it to file
#         btn = tk.Button(self.root, text="Capture reference",
#                          command=self.takeSnapshot)
#         btn.pack(side="bottom", fill="both", expand="yes", padx=10,
#                  pady=10)
#
#         # start a thread that constantly pools the video sensor for
#         # the most recently read frame
#         self.stopEvent = threading.Event()
#         self.thread = threading.Thread(target=self.videoLoop, args=())
#         self.thread.start()
#
#         # set a callback to handle when the window is closed
#         self.root.wm_title("PyImageSearch PhotoBooth")
#         self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)
#
#     def videoLoop(self):
#         try:
#             # keep looping over frames until we are instructed to stop
#             while not self.stopEvent.is_set():
#                 # grab the frame from the video stream and resize it to
#                 # have a maximum width of 300 pixels
#                 self.frame = self.vs.read()
#                 self.frame = imutils.resize(self.frame, width =300)
#                 image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
#                 image = Image.fromarray(image)
#                 image = ImageTk.PhotoImage(image)
#
#                 # if the panel is not None, we need to initialize it
#                 if self.panel is None:
#                     self.panel = tk.Label(image=image)
#                     self.panel.image = image
#                     self.panel.pack(side="left", padx=10, pady=10)
#                 else:
#                     self.panel.configure(image=image)
#                     self.panel.image = image
#         except RuntimeError:
#             print("[INFO] caught a RuntimeError")
#
#
#
#
# class PhotoBoothApp():
#     def __init__(self, vs, outputPath):
#         # store the video stream object and output path, then initialize
#         # the most recently read frame, thread for reading frames, and
#         # the thread stop event
#         self.vs = vs
#         self.outputPath = outputPath
#         self.frame = None
#         self.thread = None
#         self.stopEvent = None
#
#         # initialize the root window and image panel
#         self.root = tk.Tk()
#         self.panel = None
#
#         # create a button, that when pressed, will take the current
#         # frame and save it to file
#         btn = tk.Button(self.root, text="Snapshot!",
#                          command=self.takeSnapshot)
#         btn.pack(side="bottom", fill="both", expand="yes", padx=10,
#                  pady=10)
#
#         # start a thread that constantly pools the video sensor for
#         # the most recently read frame
#         self.stopEvent = threading.Event()
#         self.thread = threading.Thread(target=self.videoLoop, args=())
#         self.thread.start()
#
#         # set a callback to handle when the window is closed
#         self.root.wm_title("PyImageSearch PhotoBooth")
#         self.root.wm_protocol("WM_DELETE_WINDOW", self.onClose)
#
#     def videoLoop(self):
#         # DISCLAIMER:
#         # I'm not a GUI developer, nor do I even pretend to be. This
#         # try/except statement is a pretty ugly hack to get around
#         # a RunTime error that Tkinter throws due to threading
#         try:
#             # keep looping over frames until we are instructed to stop
#             while not self.stopEvent.is_set():
#                 # grab the frame from the video stream and resize it to
#                 # have a maximum width of 300 pixels
#                 self.frame = self.vs.read()
#                 self.frame = imutils.resize(self.frame, width=300)
#
#                 # OpenCV represents images in BGR order; however PIL
#                 # represents images in RGB order, so we need to swap
#                 # the channels, then convert to PIL and ImageTk format
#                 image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
#                 image = Image.fromarray(image)
#                 image = ImageTk.PhotoImage(image)
#
#                 # if the panel is not None, we need to initialize it
#                 if self.panel is None:
#                     self.panel = tk.Label(image=image)
#                     self.panel.image = image
#                     self.panel.pack(side="left", padx=10, pady=10)
#
#                 # otherwise, simply update the panel
#                 else:
#                     self.panel.configure(image=image)
#                     self.panel.image = image
#
#         except RuntimeError:
#             print("[INFO] caught a RuntimeError")
#

#
#
#     def takeSnapshot(self):
#     # grab the current timestamp and use it to construct the
#     # output path
#         ts = datetime.datetime.now()
#         filename = "{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))
#         p = os.path.sep.join((self.outputPath, filename))
#
#     # save the file
#         cv2.imwrite(p, self.frame.copy())
#         print("[INFO] saved {}".format(filename))
#
#     def onClose(self):
# 	# set the stop event, cleanup the camera, and allow the rest of
# 	# the quit process to continue
# 	    print("[INFO] closing...")
# 	    self.stopEvent.set()
# 	    self.vs.stop()
# 	    self.root.quit()
#
# ###########################################
# # class Application(tk.Frame):
# #     def __init__(self, master=None):
# #         super().__init__(master)
# #         self.master = master
# #         self.pack()
# #         self.create_widgets()
# #
# #     def create_widgets(self):
# #         self.hi_there = tk.Button(self)
# #         self.hi_there["text"] = "Hello world\n(click me)"
# #         self.hi_there["command"] = self.say_hi
# #         self.hi_there.pack(side="top")
# #         self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
# #         self.quit.pack(side="bottom")
# #
# #         self.w2 = tk.Scale(self.master, from_=0, to=200, orient=tk.HORIZONTAL)
# #         self.w2.pack()
# #
# #     def say_hi(self):
# #         print('hello there')
#
#
# root = tk.Tk()
# app = PhotoBoothApp(cv2.VideoCapture(1),'C:\\Users\\karol\\PycharmProjects\\dhi')
# app.mainloop()
