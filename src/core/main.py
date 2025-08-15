import flet as ft

from db.db_controler import Database
from db.paswords import Passwords
from core.elaborador import Interfaces

import atexit
import shutil
from pathlib import Path

class Main:
    def __init__(self,page:ft.Page):
        self.page = page
        self.db = Database()
        self.encrypt = Passwords()
        self.Interfaces = Interfaces(self.page)
        self.Interfaces.build_interface()

@atexit.register
def Limpar():
	for d in Path(".").rglob("__pycache__"):
		shutil.rmtree(d)

ft.run(main=Main)