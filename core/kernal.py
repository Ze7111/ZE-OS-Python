from classes.rprogressbar import progress
from core.commandline import baseshell
from components.appchecker import apptxtwrite as app
import os
elevationlevel = 0
path = 'none'
def verifycredits():
    global elevationlevel
    with open("keys\\process.key", 'r') as processKey:
        processKeyValue = processKey.readline()
        
    if os.path.exists("keys\\process.key"):
        os.remove("keys\\process.key")
    else:
        print("Validation error")
        
    if processKeyValue == "A879FL239K":
        elevationlevel = 2
        
    elif processKeyValue == "D6H84G6436":
        elevationlevel = 3
        
    elif processKeyValue == "7894X982F4":
        elevationlevel = 1
        
    else:
        elevationlevel = 0
    commandlineenv()
        
def commandlineenv():
    global path
    app()
    taskthree = "[red]Importing Shell"
    tasktwo = "[green]Verifying Applications"
    taskone = ""
    progress(taskone, tasktwo, taskthree)
    pathtext = 'root/home/apps'
    path = 'apps'
    baseshell(elevationlevel, pathtext)
    