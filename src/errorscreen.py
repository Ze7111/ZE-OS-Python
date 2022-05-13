from time import sleep
from rich.console import Console
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
import os
def fullerror(error):
    os.system("cls")
    console = Console()
    with console.screen(style="bold white on red") as screen:
        for count in range(10, 0, -1):
            text = Align.center(
                Text.from_markup(f"[blink]Don't Panic! Your System Has Crashed, ERROR [bold]{error}[/], We will Restart it [/blink]\n{count} seconds", justify="center"),
                vertical="middle",
            )
            screen.update(Panel(text))
            sleep(1)
            os.system("cls")