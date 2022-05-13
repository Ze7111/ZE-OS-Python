import os, time, sys, msvcrt
from components import logincheck
from getpass import getpass
from containers import generatekey
from containers import encrypt
from containers import decrypt
from core import debugpanel
from classes import console
from components import createreqfile
from random import seed
from random import randint
from core import kernal
from classes import rprogressbar
from os import getpid
from rich.align import Align
from rich.text import Text
from rich.panel import Panel
from core import commandline
from components.appchecker import apptxtwrite as app
from src import errorscreen
import glob
from core.exit import shutdown as exit1
from cryptography.fernet import Fernet
from rich.progress import Progress