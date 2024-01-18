import os

def getFilesFromDirectory(dir):
    files = os.listdir(dir)
    
    return files

def breakDownFilesByType(files):
    f = {
        'images':[],
        'videos':[],
        'audio':[]
    }
    
    for i in files:
        l = i.lower()

        if l.endswith('.png') or l.endswith('.jpg') or l.endswith('.jpeg') or l.endswith('.bmp'):
            f['images'].append(i)
        
        if l.endswith('.mp4'):
            f['videos'].append(i)
        
        if l.endswith('.mp3') or l.endswith('.wav') or l.endswith('.ogg'):
            f['audio'].append(i)
    
    return f