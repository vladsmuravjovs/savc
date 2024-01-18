import os

import numpy as np

import prefs as pr

from moviepy import *
from moviepy.editor import *

from PIL import Image

def makeVideo(files):
    prefs = pr.load()
    
    wdir = os.getcwd() + prefs['workdir']

    audio = []
    for aud in files['audio']:
        audio.append(AudioFileClip(wdir + aud))

    images = []
    for i in range(0, len(audio)):
        img = Image.open(wdir + files['images'][i])
        img = img.resize(prefs['res'])
        img = img.convert("RGB", palette=Image.ADAPTIVE, colors=32)
        img = img.save(wdir + '__' + files['images'][i])

        images.append(ImageClip(wdir + '__' + files['images'][i], duration=audio[i].duration))

    audio_clip = concatenate_audioclips(audio)
    video_clip = concatenate_videoclips(images, method="compose")
    video_clip = video_clip.set_audio(audio_clip)
    video_clip.write_videofile(prefs['outputname'], fps=24)

    # clean up
    for i in files['images']:
        if(os.path.exists(wdir + '__' + i)):
            os.remove(wdir + '__' + i)