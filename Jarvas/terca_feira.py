import time
import pyautogui as pa
import selenium as sel
import schedule as sch
import os
import webbrowser
from pywinauto.application import Application



def abrir_programas_dias_da_semana():
    # abre o VSCode
    os.system("code")

    # Abre Udemy e Linkedin
    webbrowser.open("https://www.udemy.com/home/my-courses/learning/")
    webbrowser.open("https://www.linkedin.com/feed/")
    webbrowser.open("https://github.com")


def abrir_programas_final_de_semana():
    webbrowser.open("https://www.youtube.com/")
    os.system("roblox")


# Programação da Semana
sch.every().monday.do(abrir_programas_dias_da_semana)
sch.every().tuesday.do(abrir_programas_dias_da_semana)
sch.every().wednesday.do(abrir_programas_dias_da_semana)
sch.every().thursday.do(abrir_programas_dias_da_semana)
sch.every().friday.do(abrir_programas_dias_da_semana)

# Programaão do final de Semana
