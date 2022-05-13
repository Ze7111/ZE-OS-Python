#--------------- D E P E N D I C I E S ---------------#  
from classes.__innit__ import *
#--------------- D E P E N D I C I E S ---------------#  
def progress(taskone, tasktwo, taskthree):
    os.system('cls')
    with Progress() as progress:
        task3 = progress.add_task(taskthree, total=70)
        while not progress.finished:
            progress.update(task3, advance=0.5)
            time.sleep(0.01)
    with Progress() as progress:
        task2 = progress.add_task(tasktwo, total=70)
        while not progress.finished:
            progress.update(task3, advance=0.2)
            time.sleep(0.01)