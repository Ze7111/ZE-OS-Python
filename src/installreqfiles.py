def install():
    nextline= ""
    import pip, sys
    pip.main(["install", 'rich'])
    pip.main(["install", 'random'])
    pip.main(["install", 'os'])
    pip.main(["install", 'time'])
    pip.main(["install", 'subprocess'])
    import subprocess
    from subprocess import Popen, PIPE, CalledProcessError
    #DETACHED_PROCESS = 0x00000008
    #pid = subprocess.Popen([sys.executable, "python src\subtransreqinstall.py"],
    #                       creationflags=DETACHED_PROCESS).pid
    lineno = 0
    process = subprocess.Popen("python src\subtransreqinstall.py", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    for line in process.stdout:
        lineno = lineno + 1
    
    from time import sleep
    from rich.console import Console
    from rich.align import Align
    from rich.text import Text
    from rich.panel import Panel
    from random import seed
    from random import random
    import os
    seed(5)
    file = open("data\\requirements.txt", 'r')
    line_count = 0
    for line in file:
        if line != "\n":
            line_count += 1
    file.close()
    os.system("cls")
    console = Console()
    with console.screen(style="bold white on black") as screen:
        for line_count in range(line_count, 0, -lineno):
            
            text = Align.center(
                Text.from_markup(f"[blink]Installing Required Files, please wait", justify="center"),
                vertical="middle",
            )
            screen.update(Panel(text))
            value = 4
            sleep(value)
            os.system("cls")
install()