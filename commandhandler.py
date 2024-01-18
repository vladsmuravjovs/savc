import filehandler as fh
import videohandler as vh
import prefs as pr
import os
import json

def createVideo():
    files = fh.getFilesFromDirectory(os.getcwd() + pr.load()['workdir'])
    files = fh.breakDownFilesByType(files)

    vh.makeVideo(files)

    print('your video is done!')
    print('type "exit" or "quit" to quit the program.')

def startEditPrefs():
    prefs = pr.load()

    os.system('cls')

    print("Type in the name of the variable you'd like to change.")
    print("Type in 'info' and the name of the variable for its' explanation")
    print("Preference editing: ")

    for x,y in prefs.items():
        print(x + " = " + str(y))
    
    inp = input()
    while(True):
        if(inp == 'exit' or inp == 'quit'):
            break
        if(inp in prefs.keys()):
            editPref(inp)
            break
    
    os.system('cls')
    displayHelp()

def editPref(prefName):
    os.system('cls')
    print('Editing the variable ' + prefName)
    print(pr.getDesc(prefName))
    print('Enter the new value: ')
    prefs = pr.load()

    newVal = input()
    if(newVal.startswith('[') and newVal.endswith(']')):
        newVal = json.loads(newVal)
    
    prefs[prefName] = newVal

    pr.save(prefs)
    

def displayHelp():
    print('type "create" to create the video.')
    print('type "edit" to edit your preferences.')
    print('type "exit" or "quit" to quit the program.')
    print('type "help" for the command list.')

def createCommandHandler():
    inputs = {
            'help':lambda x: displayHelp(),
            'create': lambda x : createVideo(),
            'edit': lambda x : startEditPrefs()
        }

    command = input()
    while(True):
        if(command in inputs):
            inputs[command](None)
        command = input()
        if(command == "exit" or command == "quit"):
            break