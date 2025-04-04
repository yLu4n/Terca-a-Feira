from pywinauto.application import Application
from pywinauto import Desktop
from pywinauto.application import Application
import time
import psutil

# Lista todos os processos em execução
for proc in psutil.process_iter(attrs=['pid', 'name']):
    if "chrome" in proc.info['name'].lower():  # Filtra apenas processos do Chrome
        print(f"Nome: {proc.info['name']}, PID: {proc.info['pid']}")

pid = 4512  

# Nome: chrome.exe, PID: 2060
# Nome: chrome.exe, PID: 4512
# Nome: chrome.exe, PID: 7780
# Nome: chrome.exe, PID: 10208
# Nome: chrome.exe, PID: 10728
# Nome: chrome.exe, PID: 12232
# Nome: chrome.exe, PID: 17256
# Nome: chrome.exe, PID: 18820

# Conecta ao processo pelo PID
app = Application(backend="uia").connect(process=pid)

# Obtém a janela principal
janela = app.top_window()

# Foca na janela
janela.set_focus()

print("Janela focada com sucesso!")
