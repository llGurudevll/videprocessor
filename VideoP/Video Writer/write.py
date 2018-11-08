


import cv2
import numpy as np
import os
import moviepy.editor as mp
import subprocess


 
from os.path import isfile, join
 
def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    files.sort(key = lambda x: int(x[5:-4]))
 
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
 
    out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'X264'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        out.write(frame_array[i])
    out.release()
 
def main():
    pathIn= './data/'
    pathOut = 'video.mp4'

    fps = 25.100



    convert_frames_to_video(pathIn, pathOut, fps)
    video = mp.VideoFileClip("video.mp4")
    video.write_videofile("output.mp4", audio="audio.mp3")

    
 
if __name__=="__main__":
    main()
