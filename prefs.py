import json
import os

def load():
    userPrefs = {
        'workdir':'\\dump\\',
        'outputname':'video.mp4',
        'res':[480,480]
    }

    if os.path.exists(os.getcwd() + '\\userprefs.txt'):
        file = open("userprefs.txt","r")
        userPrefs = json.loads(file.read())
        file.close()
    else:
        save(userPrefs)

    return userPrefs

def save(prefs):
    file = open("userprefs.txt", "w")
    file.write(json.dumps(prefs))
    file.close()

def getPrettyNames(prefs):
    prettyNames = {
        'workdir':"The directory where all of the audio and image materials are located within the current directory.",
        'outputname':"The name of the output video file.",
        'res':"The resolution to resize the images to."
    }

    return prettyNames

def getDesc(pref):
    names = getPrettyNames(load())

    if pref in names:
        return pref
    else:
        return None