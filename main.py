from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import pygame
from uteis import *

root = Tk()
root.title("Idioms' Glossary")
root.configure(background='#DCDAD5')
dimensao(root)

style = ThemedStyle(root)
style.set_theme('clam')

bt_style = ttk.Style()
bt_style.configure('estilo_bt.TButton', font=('Agency FB', 24, 'bold'), relief='flat') 

# IMAGENS         
bt_img_america_do_norte = PhotoImage(file='imgs/continentes/continentes_contornados/continent_america_do_norte.png')
bt_img_america_do_sul = PhotoImage(file='imgs/continentes/continentes_contornados/continent_america_do_sul.png')
bt_img_afria = PhotoImage(file='imgs/continentes/continentes_contornados/continente_africa.png')
bt_img_asia = PhotoImage(file='imgs/continentes/continentes_contornados/continente_asia.png')
bt_img_australia = PhotoImage(file='imgs/continentes/continentes_contornados/continente_australia.png')
bt_img_europa = PhotoImage(file='imgs/continentes/continentes_contornados/continente_europa.png')

bt_america_do_norte = ttk.Button(root,
                      text='América do Norte',
                      # command=chama_jp,
                      image=bt_img_america_do_norte,
                      compound="top",
                      style='estilo_bt.TButton', width=20)

bt_america_do_sul = ttk.Button(root,
                      text='América do Sul',
                      # command=,
                      image=bt_img_america_do_sul,
                      compound="top",
                      style='estilo_bt.TButton', width=20)

bt_africa = ttk.Button(root,
                      text='África',
                      # command=,
                      image=bt_img_afria,
                      compound="top",
                      style='estilo_bt.TButton', width=20)

bt_asia = ttk.Button(root,
                      text='Ásia',
                      # command=,
                      image=bt_img_asia,
                      compound="top",
                      style='estilo_bt.TButton', width=20)

bt_australia = ttk.Button(root,
                      text='Austrália',
                      # command=,
                      image=bt_img_australia,
                      compound="top",
                      style='estilo_bt.TButton', width=20)

bt_europa = ttk.Button(root,
                      text='Europa',
                      # command=,
                      image=bt_img_europa,
                      compound="top",
                      style='estilo_bt.TButton', width=20)

# BOTÕES CONTINENTES
bt_america_do_norte.grid(row=0, column=0)
bt_europa.grid(row=0, column=1)
bt_asia.grid(row=0, column=2)
bt_america_do_sul.grid(row=1, column=0)
bt_africa.grid(row=1, column=1)
bt_australia.grid(row=1, column=2)

root.mainloop()
