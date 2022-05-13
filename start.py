#--------------- D E P E N D I C I E S ---------------#  
try:
    import os, time, sys, msvcrt
    from components.logincheck import checker, passchek, finalcheck
    from containers.generatekey import write_key
    from containers.encrypt import encrypt
    from containers.decrypt import decrypt
    from core.debugpanel import realdebug
    from classes.console import console
    from src.errorscreen import fullerror
    from components.createreqfile import req
    from random import seed
    from random import randint
    from core.kernal import verifycredits
    from classes.rprogressbar import progress
    from os import getpid
except:
    from src.installreqfiles import install
    install()
    
#--------------- S T A R T   U P ---------------# 

os.system("cls")
seed(532542532)  
value = os.getpid()
with open('temp\\session.id', 'w') as sessionID:
    sessionID.write(f'START UP PROCESS ID 0x{value}')

reqstat = req()
if reqstat == "updated requirements file":
    console.print(reqstat, style="bold green")
    time.sleep(2)
else:
    console.print(reqstat, style="bold red")
    time.sleep(3)
error = "none"
info = 0
usercheck = ""
os.system("cls")

#--------------- L O G I N ---------------#
def logininfo():
    global info, sessionID, value, usercheck
    
    
    key = open("keys\\accountsdb.key", "rb").read()
    filename = "data\\accounts.sql" 
    
    
    value = randint(1927461937, 1736451723946)
    with open('temp\\session.id', 'a') as sessionID:
        sessionID.write(f'\n LOGIN PROCESS ID 0x{value}')
        
        
    user = console.input("[bold red]Enter Username : ")
    usercheck = user
    console.print("[bold red]Enter Password :", end =" ")
    passwor = ''
    while True:
        # x = getch.getch()
        x = msvcrt.getch().decode("utf-8")
        if x == '\r' or x == '\n':
            break
        print('⚬', end='', flush=True)
        passwor +=x
    passw = passwor
    
    
    #          ∨ ∨ ∨ ∨                            D E B U G   P A N E L   #
    if user == "one":
        if passw == "1":
            print(" ")
            debugpanel()
        else:
            error = (" D O N T   C O M E   H E R E   A G A I N ")
            fullerror(error)
            retry()
    #          ∧ ∧ ∧ ∧                            D E B U G   P A N E L   #


    with open("data\\accounts.sql") as f:
        file_1_line = f.readline()
    with open("src\\database.sql") as f2:    
        file_2_line = f2.readline()
    if file_1_line == file_2_line:
        f.close()
        f2.close()
        print(" ")
        console.print("[#e60b0b]POSSIBLE DATA BREACH\u2757")
        time.sleep(3)
        taskone = "[blue]Cleaning up "
        tasktwo = "[bold red]Verifying Integrity "
        taskthree = "[red]Encrypting "
        progress(taskone, tasktwo, taskthree)
        
        try:
            checker(user, passw)
            passchek(passw)
            info = finalcheck()
        except Exception as exception:
            print(exception)
            raise
        
        #          ∨ ∨ ∨ ∨                                    E N C R Y P T   #
        encrypt(filename, key)
        #          ∧ ∧ ∧ ∧                                    E N C R Y P T   #
        
        
    else:
        #          ∨ ∨ ∨ ∨                                    D E C R Y P T   #
        decrypt(filename, key)
        #          ∧ ∧ ∧ ∧                                    D E C R Y P T   #
        
        try:
            checker(user, passw)
            passchek(passw)
            info = finalcheck()
        except:
            print(" ")
            console.print("[#e60b0b]login failed, fatal error, check usercheck.py")
        
        #          ∨ ∨ ∨ ∨                                    E N C R Y P T   #
        encrypt(filename, key)
        #          ∧ ∧ ∧ ∧                                    E N C R Y P T   #
    print(" ")
    check()

#--------------- C R E D   C H E C K ---------------#
def check():
    global info, sessionID, value, user, usercheck
    
    value = randint(1927461937, 1736451723946)
    with open('temp\\session.id', 'a') as sessionID:  
        sessionID.write(f'\n LOGIN CHECK PROCESS ID 0x{value}')
    
    try:    
        if info == 1:
            console.print("login Sucess", style="green")
            time.sleep(1)
            with open('keys\\process.key', 'w') as processKey:
                
                if usercheck == "admin":
                    processKeyValue = "A879FL239K"
                    processKey.write(processKeyValue)
                    time.sleep(2)
                    
                elif usercheck == "dev":
                    processKeyValue = "D6H84G6436"
                    processKey.write(processKeyValue)
                    
                elif usercheck == "superuser":
                    processKeyValue = "7894X982F4"
                    processKey.write(processKeyValue)
                    
                else:
                    processKeyValue = "unelevated"
                    processKey.write(processKeyValue)
                    
            one = verifycredits()
            if one == 1:
                exit()
            
            
        elif info == 0:
            console.print("Failed To Authenticate", style="red")
            time.sleep(2)
            os.system("cls")
            logininfo()
        else:
            error = "F128"
            console.print("sector <0x424535C44415441> is corrupted, error code ",error," )")
    except Exception as expection:
        error = "F129"
        console.print(f"sector <0x4245545445441> is corrupted, error code {error} \n{expection}")

#--------------- R E T R Y ---------------#
def retry():
    os.system("cls")
    logininfo()

#--------------- D E B U G   P A N E L ---------------#
def debugpanel():
    global sessionID, value
    
    value = randint(1927461937, 1736451723946)
    with open('temp\\session.id', 'a') as sessionID:  
        sessionID.write(f'\n DEBUG PROCESS ID 0x{value}')
        
    console.print(">", style='#0be62c', end =" ")
    marker = input()
    if marker == 'e':
        encryptiontest()
    elif marker == 'd':
        realdebug()
        
def encryptiontest():
    key = open("keys\\accountsdb.key", "rb").read()
    filename = "data\\accounts.sql"
    console.print(">", style='#0be62c', end =" ")
    tin = int(input())
    if tin == 6:
        write_key()
    elif tin == 1:
        decrypt(filename,key)
    elif tin == 2:
        encrypt(filename,key)
        
#--------------- S T A R T ---------------#
logininfo()