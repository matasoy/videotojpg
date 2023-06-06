import cv2
import numpy as np
import skimage.exposure
vidcap = cv2.VideoCapture('videoname.mp4') #video file name here
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("r/frame%d.jpg" % count, image)     # save frame as JPEG file      
  if count>300:
    break
  count += 1
  success,image = vidcap.read()
