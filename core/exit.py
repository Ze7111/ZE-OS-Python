from time import sleep
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
import os
def shutdown():
    os.system("cls")
    console = Console()
    with console.screen(style="bold white on purple") as screen:
        for count in range(6, 0, -1):
            text = Align.center(
                Text.from_markup(f"S H U T I N G   D O W N", justify="center"),
                vertical="middle",
            )
            screen.update(Panel(text))
            sleep(1)
            os.system("cls")
    exit()