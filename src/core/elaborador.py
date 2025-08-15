import flet as ft

from dataclasses import dataclass
from datetime import datetime
from src.pages.home.Home import Home

import os
@dataclass
class Exame:
    name: str
    empresa: str
    data: datetime

class Funtions:
    def __init__(self):
        diretorio_pai = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.scan_path = os.path.join(diretorio_pai, "scaneados")
        self.exames_path = os.path.join(diretorio_pai, "Exames")
    
class Interfaces:
    def __init__(self,page:ft.Page):
        self.page = page
        self.home = Home(self.page)
    
    def build_interface(self):
        return self.page.add(self.home.build_view())