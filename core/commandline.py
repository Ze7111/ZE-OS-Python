from email.mime import application
import os, sys
from classes.console import console
from src.errorscreen import fullerror
from glob import glob
from core.exit import shutdown as exit1

def nothigh():
    return console.print("Please restart the shell and login as rootuser to use these functions", style="red")

def baseshell(elevationlevel, path):
    if sys.platform == 'win32':
        type = "Windows Shell"
    
    console.print(f"{path} >", style='#0be62c', end =" ")
    userinp1 = input("")
    userinp = userinp1.lower()
    application = ""
    
    filename = 'apps\\apps.json'
    path1 = "none"
    start_path = 'apps'
    substring = ".py"
    
    if userinp == "sudo":
        if elevationlevel < 1:
            console.print("Please restart the shell and login as rootuser to use these functions", style="red")
        elif elevationlevel > 1:
            console.print("YOUR ALREADY ROOTUSER", style="red")
            
    elif userinp == "apps":
        for path1,dirs,files in os.walk(start_path):
            for filename in files:
                print(filename)
    
    elif substring in userinp:
        try:
            importpath = userinp
            imported = getattr(__import__("apps", fromlist=[importpath]), "application")
            imported
            application()
        except Exception as expection:
            print(f"Error in reading app, maybe doesn't exist? (Expection Thrown, {expection})")
    
    elif userinp == "cd":
        if elevationlevel < 1:
            nothigh()
        else:
            console.print(f"Enter New Path >", style='#0be62c', end =" ")
            cdloc = input(" ")
            os.popen("cd ",cdloc)
            path = f'root/home/{cdloc}'
        
    elif userinp == 'help':
        console.print(f"This is ZE OS help, if you would like {type} commands, type 'help unix'", style="purple")
        console.print("HELP UNIX      Unix comand set", style="purple")
        console.print("CD             Change path to a diffrent folder in the dir", style="purple")
        console.print("DIR            All folders in the cuurrent dir", style="purple")
        console.print("APPS           Show all installed apps", style="purple")
        console.print("APPS HELP      Help with opening apps", style="purple")
        console.print("CLEAR          Clears the screen", style="purple")
        console.print("EXIT           Shutdown the OS", style="purple")
        
    elif userinp == 'apps help':
        console.print(f"This is ZE OS help, if you would like {type} commands, type 'help unix'", style="purple")
        console.print("To open an app find the name of the app you would like to open. Then type 'appname.py', replace the appname.py with the name of the app your trying to open (not case sensitive)", style="purple")
    
    elif userinp == 'help unix':
        try:
            cmd = os.popen("help").read()
            console.print(cmd, style="purple")
        except Exception as exception:
            console.print(f"Some error is stopping you here, {exception}", style="red")
    
    elif userinp == 'clear':
        try:
            cmd = os.system("cls")
        except Exception as exception:
            console.print(f"Some error is stopping you here, {exception}", style="red")
            
    elif userinp == 'cls':
        try:
            cmd = os.system("cls")
        except Exception as exception:
            console.print(f"Some error is stopping you here, {exception}", style="red")
    
    elif userinp == 'exit':
        exit1()
    
    else:
        extrastring = "not recognized"
        try:
            os.popen(userinp)
            cmd = os.popen(userinp).read()
            if extrastring in cmd:
                console.print(f"Big Error, {userinp} does not exist anywhere on the OS, maybe you made a typo?", style="red")
            console.print(cmd, style="blue")
        except Exception as exception:
            console.print(f"Some error is stopping you here, {exception}", style="red")
        
        
    baseshell(elevationlevel, path)