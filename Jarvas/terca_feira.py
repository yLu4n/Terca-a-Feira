import time
import pyautogui
from pywinauto import Desktop
import schedule as sch
import os
import webbrowser


def abrir_programas_dias_da_semana():
    # Abre o VSCode
    os.startfile(caminho_vs)
    time.sleep(5)
    
    # Abre o Spotify nas minhas músicas Favoritas
    os.startfile(caminho_spotify)
    pyautogui.click(x=272, y=589)

    # Abre na Plataforma Udemy e entra no curso atual
    webbrowser.open("https://www.udemy.com/home/my-courses/learning/")
    janela_curso_python.wait("exists", timeout=5)
    time.sleep(7)
    pyautogui.scroll(-350)
    pyautogui.click(x=313, y=585, duration=0.8)

    # Abre o Linkedin
    webbrowser.open("https://www.linkedin.com/feed/")


def abrir_programas_final_de_semana():
    os.startfile(caminho_roblox)
    webbrowser.open("https://www.youtube.com/")
    os.startfile(caminho_roblox)


# Caminhos dos aplicativos
caminho_roblox = r"C:\Users\User\AppData\Local\Roblox\Versions\version-347f4ac346734391\RobloxPlayerBeta.exe"
caminho_vs = r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe"
caminho_spotify = r"C:\Users\User\AppData\Local\Microsoft\WindowsApps\SpotifyAB.SpotifyMusic_zpdnekdrzrea0\Spotify.exe"

janela_curso_python = Desktop(backend="uia").window(title_re=".*Meu aprendizado | Udemy.*")

# Programação da Semana
sch.every().monday.do(abrir_programas_dias_da_semana())
sch.every().tuesday.do(abrir_programas_dias_da_semana())
sch.every().wednesday.do(abrir_programas_dias_da_semana())
sch.every().thursday.do(abrir_programas_dias_da_semana())
sch.every().friday.do(abrir_programas_dias_da_semana())

# Programaão do final de Semana
