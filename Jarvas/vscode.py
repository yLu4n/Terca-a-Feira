import os
from pywinauto import Application


class VsCode():
    def __init__(self):
        self.caminho_vs = r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        self.app = Application()
    
    def abrir_vscode(self):
        self.app.start(self.caminho_vs)