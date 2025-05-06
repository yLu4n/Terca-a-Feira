import time
import pyautogui
from pywinauto import Desktop
import schedule as sch
import os
import webbrowser

def iniciar_caminhos():
    
    caminho_roblox = r"C:\Users\User\AppData\Local\Roblox\Versions\version-347f4ac346734391\RobloxPlayerBeta.exe"
    caminho_vs = r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe"
    caminho_spotify = r"C:\Users\User\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\Spotify.exe"




janela_curso_python = Desktop(backend="uia").window(title_re=".*Meu aprendizado | Udemy.*")