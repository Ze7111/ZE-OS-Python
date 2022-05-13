import os
os.system("cls")
print("Would you like to automagicly install all the dependencies? STRONGLY RECOMMENDED IF YOU DONT KNOW WHAT YOU HAVE (y for yes, n for no)")
depn = input("- ")
depn = depn.lower()
if depn == 'y':
    try:
        os.system("pip install time")
        os.system("pip install rich")
        os.system("pip install random")
        os.system("pip install datetime")
        os.system("pip install sys")
    except:
        import time, sys, random
else:
    from datetime import datetime
from rich import console
import time, sys, random
from datetime import datetime
from rich.console import Console
from rich.style import Style
from rich.syntax import Syntax
from rich import print
from random import seed
from random import randint
Console = Console()
# DEPENDICIES  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
key = "First letter (O for O only, X for X only, MX for more X, MO for more O, E for even ammount. l for divinding, b for blanks. O X O, eg: MXlXOX, or OlbbO)"
grid = [
    'a', 'b', 'c',
    'd', 'e', 'f',
    'g', 'h', 'i',
]
a, b, c, d, e, f, g, h, i = 0, 0, 0, 0, 0, 0, 0, 0, 0
pointer = 0
testlist = [ "TEST BEGIN", "separatortop", "OlObb", "separatorbottem", "OlbOb", "OlbbO", "OlOOb", "OlbOO","OlObO", "OlOOO", "XlXbb", "XlbXb", "XlbbX", "XlXXb", "XlbXX", "XlXbX", "XlXXX", "ElOXb", "ElXOb", "ElbOX", "ElbXO", "ElObX", "ElXbO", "MOlOOX", "MOlXOO", "MOlOXO", "MXlXXO", "MXlOXX", "MXlXOX" ]
testlistbackup = [ "TEST BEGIN", "separatortop", "OlObb", "separatorbottem", "OlbOb", "OlbbO", "OlOOb", "OlbOO","OlObO", "OlOOO", "XlXbb", "XlbXb", "XlbbX", "XlXXb", "XlbXX", "XlXbX", "XlXXX", "ElOXb", "ElXOb", "ElbOX", "ElbXO", "ElObX", "ElXbO", "MOlOOX", "MOlXOO", "MOlOXO", "MXlXXO", "MXlOXX", "MXlXOX" ]
testStat = 0
gamestat = 0
dividerneed = 0
no = 0
# ALL BASE REQS ABOVE THIS LINE -----------------------------------------------------------------------------------------------------------------------------------------------

# GAME LOGIC BELOW ------------------------------------------------------------------------------------------------------------------------------------------------------------

def mainlogic():
    global gamestat
    global pointer
    global testStat
    global testlistbackup
    global no
    if gamestat == 0:
        if testStat == 0:
            os.system("cls")
            Console.print("What would you like to do, for test type 1, to go anywhere in the code press 2, To start the game press 3, for multiplayer 4", style='#00ff0f')
            m = input("- ")
            if m == '1':
                testStat = 1
                os.system("cls")
                testsys()
            elif m == '4':
                gamestat = 3
                os.system("cls")
                GameBEGINMulti()
            elif m == '2':
                os.system("cls")
                Console.print("First letter (O for O only, X for X only, MX for more X, MO for more O, E for even ammount. l for divinding, b for blanks. O X O, eg: MXlXOX, or OlbbO)", style='#ffff0f')
                Console.print("Where would you like to go?", style='#00ff0f')
                l = input("- ")
                try:
                    pointer = eval(l)
                    Console.print("EVALUATING....", style='#ffff0f')
                    time.sleep(4)
                    pointer()
                except:
                    Console.print("EVALUATING....", style='#ffff0f')
                    time.sleep(4)
                    Console.print('Sorry function not found in the code.', style='#ffff0f')
                    time.sleep(2)
                    mainlogic()
                else:
                    Console.print("EVALUATING....", style='#ffff0f')
                    time.sleep(4)
                    Console.print('Sorry function not found in the code.', style='#ffff0f')
                    time.sleep(2)
                    mainlogic()
            elif m == '3':
                gamestat = 1
                os.system("cls")
                GameBEGIN()
        else:
            testsys()
    elif gamestat == 1:
        if no == 0:
            GameBEGIN()
        elif no == 2:
            Board2()
        elif no == 3:
            Board3()
    elif gamestat == 3:
        if no == 0:
            GameBEGINMulti()
        elif no == 2:
            Board2()
        elif no == 3:
            Board3()

def retrymove():
    GameBEGIN()

def retrymove1():
    GameBEGINMulti()

def retrymove2():
    playerTurn()

def playerTurn():
    global pointer
    global gamestat
    global grid
    global a, b, c, d, e, f, g, h, i
    if gamestat == 4:
        print(" ")
        Console.print("LOADING....", style='#ffff0f')
        time.sleep(4)
        Console.print("Reference Board", style='#44e36e')
        Console.print("7|8|9", style='#e37c44')
        Console.print("4|5|6", style='#e37c44')
        Console.print("1|2|3", style='#e37c44')
        Console.print("What move would you like to make? look at refrence board to know what to type.", style='#00ff0f')
        o = int(input("- "))
        while True:
            if o == 7:
                if a == 0:
                    a = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            elif o == 8:
                if b == 0:
                    b = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            elif o == 9:
                if c == 0:
                    c = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            elif o == 4:
                if d == 0:
                    d = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            elif o == 5:
                if e == 0:
                    e = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            elif o == 6:
                if f == 0:
                    f = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            elif o == 1:
                if g == 0:
                    g = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            elif o == 2:
                if h == 0:
                    h = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            elif o == 3:
                if i == 0:
                    i = 2
                    Board()
                else:
                    Console.print("AI CANT PUT HERE!", style='#e37c44')
                    continue
            else:
                print("tie?")
    else:
        GameBEGINMulti()

def aiTurn():
    global pointer
    global gamestat
    global grid
    global a, b, c, d, e, f, g, h, i
    time.sleep(2)
    while True:
        o = o = random.randint(1,9)
        if o == 7:
            if a == 0:
                a = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        elif o == 8:
            if b == 0:
                b = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        elif o == 9:
            if c == 0:
                c = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        elif o == 4:
            if d == 0:
                d = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        elif o == 5:
            if e == 0:
                e = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        elif o == 6:
            if f == 0:
                f = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        elif o == 1:
            if g == 0:
                g = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        elif o == 2:
            if h == 0:
                h = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        elif o == 3:
            if i == 0:
                i = 2
                Board()
            else:
                Console.print("AI CANT PUT HERE!", style='#e37c44')
                continue
        else:
            print("tie?")
    else:
        GameBEGIN()

def Board():
    global a, b, c, d, e, f, g, h, i
    global pointer
    global dividerneed
    global no
    global gamestat
    no = 2
    if a == 1:
        if b == 1:
            if c == 1:
                os.system("cls")
                Console.print("You Won", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if a == 2:    
        if b == 2:
            if c == 2:
                os.system("cls")
                Console.print("You Lost", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()

#--------------------------- X - SPLIT ---------------------------

    if a == 1:
        if b == 0:
            if c == 0:
                XlXbb()
    if a == 0:
        if b == 1:
            if c == 0:
                XlbXb()
    if a == 0:
        if b == 0:
            if c == 1:
                XlbbX()
    if a == 1:
        if b == 1:
            if c == 0:
                XlXXb()
    if a == 0:
        if b == 1:
            if c == 1:
                XlbXX()
    if a == 1:
        if b == 0:
            if c == 1:
                XlXbX()

#--------------------------- O - SPLIT ---------------------------

    if a == 2:
        if b == 0:
            if c == 0:
                OlObb()
    if a == 0:
        if b == 2:
            if c == 0:
                OlbOb()
    if a == 0:
        if b == 0:
            if c == 2:
                OlbbO()
    if a == 2:
        if b == 2:
            if c == 0:
                OlOOb()
    if a == 0:
        if b == 2:
            if c == 2:
                OlbOO()
    if a == 2:
        if b == 0:
            if c == 2:
                OlObO()

#--------------------------- E V E N   M I X ---------------------------

    if a == 1:
        if b == 2:
            if c == 0:
                ElXOb()
    if a == 2:
        if b == 1:
            if c == 0:
                ElOXb()
    if a == 1:
        if b == 0:
            if c == 2:
                ElXbO()
    if a == 2:
        if b == 0:
            if c == 1:
                ElObX()
    if a == 0:
        if b == 2:
            if c == 1:
                ElbOX()
    if a == 0:
        if b == 1:
            if c == 2:
                ElbXO()

#--------------------------- U N E V E N   M I X ---------------------------

    if a == 2:
        if b == 2:
            if c == 1:
                MOlOOX()
    if a == 1:
        if b == 2:
            if c == 2:
                MOlXOO()
    if a == 2:
        if b == 1:
            if c == 2:
                MOlOXO()
    if a == 1:
        if b == 1:
            if c == 2:
                MXlXXO()
    if a == 2:
        if b == 1:
            if c == 1:
                MXlOXX()
    if a == 1:
        if b == 2:
            if c == 1:
                MXlXOX()
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Board2()

def Board2():
    Console.print("╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌", style='#ce44e3')
    global a, b, c, d, e, f, g, h, i
    global pointer
    global dividerneed
    global no
    global gamestat
    no = 3
    if d == 1:
        if e == 1:
            if f == 1:
                os.system("cls")
                Console.print("You Won", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if d == 2:    
        if e == 2:
            if f == 2:
                os.system("cls")
                Console.print("You Lost", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()

#--------------------------- X - SPLIT ---------------------------

    if d == 1:
        if e == 0:
            if f == 0:
                XlXbb()
    if d == 0:
        if e == 1:
            if f == 0:
                XlbXb()
    if d == 0:
        if e == 0:
            if f == 1:
                XlbbX()
    if d == 1:
        if e == 1:
            if f == 0:
                XlXXb()
    if d == 0:
        if e == 1:
            if f == 1:
                XlbXX()
    if d == 1:
        if e == 0:
            if f == 1:
                XlXbX()

#--------------------------- O - SPLIT ---------------------------

    if d == 2:
        if e == 0:
            if f == 0:
                OlObb()
    if d == 0:
        if e == 2:
            if f == 0:
                OlbOb()
    if d == 0:
        if e == 0:
            if f == 2:
                OlbbO()
    if d == 2:
        if e == 2:
            if f == 0:
                OlOOb()
    if d == 0:
        if e == 2:
            if f == 2:
                OlbOO()
    if d == 2:
        if e == 0:
            if f == 2:
                OlObO()

#--------------------------- E V E N   M I X ---------------------------

    if d == 1:
        if e == 2:
            if f == 0:
                ElXOb()
    if d == 2:
        if e == 1:
            if f == 0:
                ElOXb()
    if d == 1:
        if e == 0:
            if f == 2:
                ElXbO()
    if d == 2:
        if e == 0:
            if f == 1:
                ElObX()
    if d == 0:
        if e == 2:
            if f == 1:
                ElbOX()
    if d == 0:
        if e == 1:
            if f == 2:
                ElbXO()

#--------------------------- U N E V E N   M I X ---------------------------

    if d == 2:
        if e == 2:
            if f == 1:
                MOlOOX()
    if d == 1:
        if e == 2:
            if f == 2:
                MOlXOO()
    if d == 2:
        if e == 1:
            if f == 2:
                MOlOXO()
    if d == 1:
        if e == 1:
            if f == 2:
                MXlXXO()
    if d == 2:
        if e == 1:
            if f == 1:
                MXlOXX()
    if d == 1:
        if e == 2:
            if f == 1:
                MXlXOX()
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Board3()

def Board3():
    Console.print("╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌", style='#ce44e3')
    global a, b, c, d, e, f, g, h, i
    global pointer
    global dividerneed
    global no
    global gamestat
    no = 0
#--------------------------- WIN STATES ---------------------------
    if g == 1:
        if h == 1:
            if i == 1:
                os.system("cls")
                Console.print("You Won", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if g == 2:    
        if h == 2:
            if i == 2:
                os.system("cls")
                Console.print("You Lost", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if a == 1:
        if d == 1:
            if g == 1:
                os.system("cls")
                Console.print("You Won", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if b == 1:
        if e == 1:
            if h == 1:
                os.system("cls")
                Console.print("You Won", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if c == 1:
        if f == 1:
            if i == 1:
                os.system("cls")
                Console.print("You Won", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if a == 2:
        if d == 2:
            if g == 2:
                os.system("cls")
                Console.print("You Lost", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if b == 2:
        if e == 2:
            if h == 2:
                os.system("cls")
                Console.print("You Lost", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if c == 2:
        if f == 2:
            if i == 2:
                os.system("cls")
                Console.print("You Lost", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if a == 1:
        if e == 1:
            if i == 1:
                os.system("cls")
                Console.print("You Won", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if c == 1:
        if e == 1:
            if g == 1:
                os.system("cls")
                Console.print("You Won", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if a == 2:
        if e == 2:
            if i == 2:
                os.system("cls")
                Console.print("You Lost", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
    if c == 2:
        if e == 2:
            if g == 2:
                os.system("cls")
                Console.print("You Lost", style='#44e36e')
                gamestat = 0
                time.sleep(5)
                mainlogic()
#--------------------------- X - SPLIT ---------------------------

    if g == 1:
        if h == 0:
            if i == 0:
                XlXbb()
    if g == 0:
        if h == 1:
            if i == 0:
                XlbXb()
    if g == 0:
        if h == 0:
            if i == 1:
                XlbbX()
    if g == 1:
        if h == 1:
            if i == 0:
                XlXXb()
    if g == 0:
        if h == 1:
            if i == 1:
                XlbXX()
    if g == 1:
        if h == 0:
            if i == 1:
                XlXbX()

#--------------------------- O - SPLIT ---------------------------

    if g == 2:
        if h == 0:
            if i == 0:
                OlObb()
    if g == 0:
        if h == 2:
            if i == 0:
                OlbOb()
    if g == 0:
        if h == 0:
            if i == 2:
                OlbbO()
    if g == 2:
        if h == 2:
            if i == 0:
                OlOOb()
    if g == 0:
        if h == 2:
            if i == 2:
                OlbOO()
    if g == 2:
        if h == 0:
            if i == 2:
                OlObO()

#--------------------------- E V E N   M I X ---------------------------

    if g == 1:
        if h == 2:
            if i == 0:
                ElXOb()
    if g == 2:
        if h == 1:
            if i == 0:
                ElOXb()
    if g == 1:
        if h == 0:
            if i == 2:
                ElXbO()
    if g == 2:
        if h == 0:
            if i == 1:
                ElObX()
    if g == 0:
        if h == 2:
            if i == 1:
                ElbOX()
    if g == 0:
        if h == 1:
            if i == 2:
                ElbXO()

#--------------------------- U N E V E N   M I X ---------------------------

    if g == 2:
        if h == 2:
            if i == 1:
                MOlOOX()
    if g == 1:
        if h == 2:
            if i == 2:
                MOlXOO()
    if g == 2:
        if h == 1:
            if i == 2:
                MOlOXO()
    if g == 1:
        if h == 1:
            if i == 2:
                MXlXXO()
    if g == 2:
        if h == 1:
            if i == 1:
                MXlOXX()
    if g == 1:
        if h == 2:
            if i == 1:
                MXlXOX()
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    GameBEGINstat()

#---------------------------------------------------------------------------------------------------------------

def GameBEGIN():
    global GameBEGINstat
    global pointer
    global gamestat
    global grid
    global a, b, c, d, e, f, g, h, i
    gamestat = 2
    GameBEGINstat = 1
    if gamestat == 2:
        print(" ")
        Console.print("LOADING....", style='#ffff0f')
        time.sleep(4)
        os.system("cls")
        Console.print("LOADING....  FINISHED", style='#00ff0f')
        os.system("cls")
        Console.print("Reference Board", style='#44e36e')
        Console.print("7|8|9", style='#e37c44')
        Console.print("4|5|6", style='#e37c44')
        Console.print("1|2|3", style='#e37c44')
        Console.print("What move would you like to make? look at refrence board to know what to type.", style='#00ff0f')
        o = int(input("- "))
        if o == 7:
            if a == 0:
                a = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 8:
            if b == 0:
                b = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 9:
            if c == 0:
                c = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 4:
            if d == 0:
                d = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 5:
            if e == 0:
                e = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 6:
            if f == 0:
                f = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 1:
            if g == 0:
                g = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 2:
            if h == 0:
                h = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 3:
            if i == 0:
                i = 1
                aiTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove()
        elif o == 0:
            gamestat = 0
            Console.print('Quiting, will return to main screen.', style='#ff0f0f')
            time.sleep(3)
            mainlogic()
    else:
        mainlogic()

def GameBEGINMulti():
    global pointer
    global gamestat
    global GameBEGINstat
    global grid
    global a, b, c, d, e, f, g, h, i
    GameBEGINstat = eval("GameBEGINMulti")
    if gamestat == 3:
        print(" ")
        Console.print("LOADING....", style='#ffff0f')
        time.sleep(4)
        Console.print("Reference Board", style='#44e36e')
        Console.print("7|8|9", style='#e37c44')
        Console.print("4|5|6", style='#e37c44')
        Console.print("1|2|3", style='#e37c44')
        Console.print("What move would you like to make? (Your X) look at refrence board to know what to type.", style='#00ff0f')
        o = int(input("- "))
        if o == 7:
            if a == 0:
                a = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 8:
            if b == 0:
                b = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 9:
            if c == 0:
                c = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 4:
            if d == 0:
                d = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 5:
            if e == 0:
                e = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 6:
            if f == 0:
                f = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 1:
            if g == 0:
                g = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 2:
            if h == 0:
                h = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 3:
            if i == 0:
                i = 1
                playerTurn()
            else:
                Console.print("SPACE TAKEN!", style='#e37c44')
                retrymove1()
        elif o == 0:
            gamestat = 0
            Console.print('Quiting, will return to main screen.', style='#ff0f0f')
            time.sleep(3)
            mainlogic()
    else:
        mainlogic()

def testsys():
    time.sleep(0.05)
    global pointer
    global testStat
    global testlist
    global testlistbackup
    Console.print('Sucessfully removed, ',testlist.pop(0), ', from the list', style='#ff0000')
    time.sleep(0.1)
    try:
        pointer = eval(testlist[0])
        print(pointer)
        time.sleep(0.05)
        pointer()
    except:
        print(" ")
        Console.print('TEST SUCESS', style='#ffff0f')
        testStat = 0
        testlist.extend(testlistbackup)
        time.sleep(3)
        mainlogic()

def basegrid():
    global testlist
    global pointer
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("Reference Board", style='#44e36e')
    Console.print("7|8|9", style='#e37c44')
    Console.print("4|5|6", style='#e37c44')
    Console.print("3|2|1", style='#e37c44')
    mainlogic()

# SEPRATORS BELOW -----------------------------------------------------------------------------------------------------------------------------------------------

def separatorbottem():
    global pointer
    global dividerneed
    dividerneed = 0
    Console.print("╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌", style='#ce44e3')
    mainlogic()

def separatortop():
    global pointer
    Console.print("╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌╎╌╌╌╌╌╌╌", style='#ce44e3')
    mainlogic()

# MAIN PLAYABLITY -----------------------------------------------------------------------------------------------------------------------------------------------

def OlObb():
    global pointer
    Console.print(" ┌───┐ ╎       ╎       ", style='#ce44e3')
    Console.print(" │   │ ╎       ╎       ", style='#ce44e3')
    Console.print(" └───┘ ╎       ╎       ", style='#ce44e3')
    mainlogic()

def OlbOb():
    global pointer
    Console.print("       ╎ ┌───┐ ╎       ", style='#ce44e3')
    Console.print("       ╎ │   │ ╎       ", style='#ce44e3')
    Console.print("       ╎ └───┘ ╎       ", style='#ce44e3')
    mainlogic()

def OlbbO():
    global pointer
    Console.print("       ╎       ╎ ┌───┐ ", style='#ce44e3')
    Console.print("       ╎       ╎ │   │ ", style='#ce44e3')
    Console.print("       ╎       ╎ └───┘ ", style='#ce44e3')
    mainlogic()

def OlOOb():
    global pointer
    Console.print(" ┌───┐ ╎ ┌───┐ ╎       ", style='#ce44e3')
    Console.print(" │   │ ╎ │   │ ╎       ", style='#ce44e3')
    Console.print(" └───┘ ╎ └───┘ ╎       ", style='#ce44e3')
    mainlogic()

def OlbOO():
    global pointer
    Console.print("       ╎ ┌───┐ ╎ ┌───┐ ", style='#ce44e3')
    Console.print("       ╎ │   │ ╎ │   │ ", style='#ce44e3')
    Console.print("       ╎ └───┘ ╎ └───┘ ", style='#ce44e3')
    mainlogic()

def OlOOO():
    global pointer
    Console.print(" ┌───┐ ╎ ┌───┐ ╎ ┌───┐ ", style='#ce44e3')
    Console.print(" │   │ ╎ │   │ ╎ │   │ ", style='#ce44e3')
    Console.print(" └───┘ ╎ └───┘ ╎ └───┘ ", style='#ce44e3')
    mainlogic()

def OlObO():
    global pointer
    Console.print(" ┌───┐ ╎       ╎ ┌───┐ ", style='#ce44e3')
    Console.print(" │   │ ╎       ╎ │   │ ", style='#ce44e3')
    Console.print(" └───┘ ╎       ╎ └───┘ ", style='#ce44e3')
    mainlogic()
    
def bbb():
    global pointer
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    Console.print("       ╎       ╎       ", style='#ce44e3')
    mainlogic()

def XlXXX():
    global pointer
    global pointer
    Console.print("  ╲ ╱  ╎  ╲ ╱  ╎  ╲ ╱  ", style='#ce44e3')
    Console.print("   ╳   ╎   ╳   ╎   ╳   ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎  ╱ ╲  ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()

def XlXbb():
    global pointer
    Console.print("  ╲ ╱  ╎       ╎       ", style='#ce44e3')
    Console.print("   ╳   ╎       ╎       ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎       ╎       ", style='#ce44e3')
    mainlogic()

def XlbXb():
    global pointer
    Console.print("       ╎  ╲ ╱  ╎       ", style='#ce44e3')
    Console.print("       ╎   ╳   ╎       ", style='#ce44e3')
    Console.print("       ╎  ╱ ╲  ╎       ", style='#ce44e3')
    mainlogic()

def XlbbX():
    global pointer
    Console.print("       ╎       ╎  ╲ ╱  ", style='#ce44e3')
    Console.print("       ╎       ╎   ╳   ", style='#ce44e3')
    Console.print("       ╎       ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()

def XlXXb():
    global pointer
    Console.print("  ╲ ╱  ╎  ╲ ╱  ╎       ", style='#ce44e3')
    Console.print("   ╳   ╎   ╳   ╎       ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎  ╱ ╲  ╎       ", style='#ce44e3')
    mainlogic()

def XlbXX():
    global pointer
    Console.print("       ╎  ╲ ╱  ╎  ╲ ╱  ", style='#ce44e3')
    Console.print("       ╎   ╳   ╎   ╳   ", style='#ce44e3')
    Console.print("       ╎  ╱ ╲  ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()

def XlXbX():
    global pointer
    Console.print("  ╲ ╱  ╎       ╎  ╲ ╱  ", style='#ce44e3')
    Console.print("   ╳   ╎       ╎   ╳   ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎       ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()

def ElOXb():
    global pointer
    Console.print(" ┌───┐ ╎  ╲ ╱  ╎       ", style='#ce44e3')
    Console.print(" │   │ ╎   ╳   ╎       ", style='#ce44e3')
    Console.print(" └───┘ ╎  ╱ ╲  ╎       ", style='#ce44e3')
    mainlogic()

def ElXOb():
    global pointer
    Console.print("  ╲ ╱  ╎ ┌───┐ ╎       ", style='#ce44e3')
    Console.print("   ╳   ╎ │   │ ╎       ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎ └───┘ ╎       ", style='#ce44e3')
    mainlogic()

def ElbXO():
    global pointer
    Console.print("       ╎  ╲ ╱  ╎ ┌───┐ ", style='#ce44e3')
    Console.print("       ╎   ╳   ╎ │   │ ", style='#ce44e3')
    Console.print("       ╎  ╱ ╲  ╎ └───┘ ", style='#ce44e3')
    mainlogic()

def ElbOX():
    global pointer
    Console.print("       ╎ ┌───┐ ╎  ╲ ╱  ", style='#ce44e3')
    Console.print("       ╎ │   │ ╎   ╳   ", style='#ce44e3')
    Console.print("       ╎ └───┘ ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()

def ElObX():
    global pointer
    Console.print(" ┌───┐ ╎       ╎  ╲ ╱  ", style='#ce44e3')
    Console.print(" │   │ ╎       ╎   ╳   ", style='#ce44e3')
    Console.print(" └───┘ ╎       ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()

def ElXbO():
    global pointer
    Console.print("  ╲ ╱  ╎       ╎ ┌───┐ ", style='#ce44e3')
    Console.print("   ╳   ╎       ╎ │   │ ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎       ╎ └───┘ ", style='#ce44e3')
    mainlogic()

def MOlOOX():
    global pointer
    Console.print(" ┌───┐ ╎ ┌───┐ ╎  ╲ ╱  ", style='#ce44e3')
    Console.print(" │   │ ╎ │   │ ╎   ╳   ", style='#ce44e3')
    Console.print(" └───┘ ╎ └───┘ ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()

def MOlXOO():
    global pointer
    Console.print("  ╲ ╱  ╎ ┌───┐ ╎ ┌───┐ ", style='#ce44e3')
    Console.print("   ╳   ╎ │   │ ╎ │   │ ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎ └───┘ ╎ └───┘ ", style='#ce44e3')
    mainlogic()

def MOlOXO():
    global pointer
    Console.print(" ┌───┐ ╎  ╲ ╱  ╎ ┌───┐ ", style='#ce44e3')
    Console.print(" │   │ ╎   ╳   ╎ │   │ ", style='#ce44e3')
    Console.print(" └───┘ ╎  ╱ ╲  ╎ └───┘ ", style='#ce44e3')
    mainlogic()

def MXlXXO():
    global pointer
    Console.print("  ╲ ╱  ╎  ╲ ╱  ╎ ┌───┐ ", style='#ce44e3')
    Console.print("   ╳   ╎   ╳   ╎ │   │ ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎  ╱ ╲  ╎ └───┘ ", style='#ce44e3')
    mainlogic()

def MXlOXX():
    global pointer
    Console.print(" ┌───┐ ╎  ╲ ╱  ╎  ╲ ╱  ", style='#ce44e3')
    Console.print(" │   │ ╎   ╳   ╎   ╳   ", style='#ce44e3')
    Console.print(" └───┘ ╎  ╱ ╲  ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()
def MXlXOX():
    global pointer
    Console.print("  ╲ ╱  ╎ ┌───┐ ╎  ╲ ╱  ", style='#ce44e3')
    Console.print("   ╳   ╎ │   │ ╎   ╳   ", style='#ce44e3')
    Console.print("  ╱ ╲  ╎ └───┘ ╎  ╱ ╲  ", style='#ce44e3')
    mainlogic()
basegrid()