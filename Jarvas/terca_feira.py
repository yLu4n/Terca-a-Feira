import time

import pyautogui

import selenium as webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By

import psutil

from pywinauto.application import Application
from pywinauto.mouse import click

import schedule as sch

import os

import webbrowser



def abrir_programas_dias_da_semana():
    # Abre o VSCode
    os.startfile(caminho_vs)
    time.sleep(5)

    # Abre na PLataforma Udemy e entra no curso atual
    webbrowser.open("https://www.udemy.com/home/my-courses/learning/")
    time.sleep(5)
    pyautogui.scroll(-450)
    pyautogui.click(x=313, y=585, duration=0.8)

    # Abre o Linkedin
    webbrowser.open("https://www.linkedin.com/feed/")


def abrir_programas_final_de_semana():
    os.startfile(caminho_roblox)
    webbrowser.open("https://www.youtube.com/")
    os.startfile(caminho_roblox)


def tocar_spotify_curtidas():
    spotify_pids = [proc.info['pid'] for proc in psutil.process_iter(['pid', 'name']) if 'Spotify' in proc.info['name']]

    if not spotify_pids:
        print("🚫 Spotify não está aberto.")
        exit()

    # Conectar com o processo
    janela_spotify = None
    for pid in spotify_pids:
        try:
            app = Application(backend="uia").connect(process=pid)
            janela = app.top_window()

            if "Spotify" in janela.window_text():
                janela_spotify = janela
                print(f"🎯 Conectado à janela do Spotify no PID: {pid}")
                break
        except Exception as e:
            print(f"⚠️ Erro ao tentar abrir a janela: {e}")

    if janela_spotify is None:
        print("🚫 Janela principal do Spotify não encontrada.")
        exit()

    # Dar foco na janela
    janela_spotify.set_focus()
    time.sleep(1)

    # Listar todos os elementos interagíveis

    alvo_texto = "Músicas Curtidas"

    for elem in janela_spotify.descendants():
        try:
            alvo_texto = "Tocar Músicas Curtidas"
            if alvo_texto.lower() in elem.window_text().lower():
                                
                # Retângulo do elemento
                rect = elem.rectangle()
                                
                # Ajusta o clique: horizontal no meio, vertical no meio + deslocamento pra baixo
                x = rect.left + (rect.width() // 2)
                y = rect.top + (rect.height() // 2) + 5  # ← AQUI: ajuste de +5 pixels pra baixo
                        
                click(coords=(x, y))
                break
        except Exception as e:
            print(f"⚠️ Erro ao tentar clicar: {e}")


# Caminhos dos aplicativos
caminho_roblox = r"C:\Users\User\AppData\Local\Roblox\Versions\version-347f4ac346734391\RobloxPlayerBeta.exe"
caminho_vs = r"C:\Users\User\AppData\Local\Programs\Microsoft VS Code\Code.exe"

# Programação da Semana
sch.every().monday.do(abrir_programas_dias_da_semana)
sch.every().tuesday.do(abrir_programas_dias_da_semana)
sch.every().wednesday.do(abrir_programas_dias_da_semana)
sch.every().thursday.do(abrir_programas_dias_da_semana)
sch.every().friday.do(abrir_programas_dias_da_semana)

# Programaão do final de Semana
