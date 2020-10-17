from tkinter import *
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
import pygame
from uteis import *

root = Tk()
root.title("Idioms' Glossary")
dimensao(root)

style = ThemedStyle(root)
style.set_theme('breeze')

bt_style = ttk.Style()
bt_style.configure('estilo_bt.TButton',
                   font=('Agency FB', 24, 'bold'),
                   ANCHOR=CENTER) 

# IMAGENS         
#        

botao = ttk.Button(root,
                      text='Teste',
                      # command=chama_jp,
                      # image=bt_img_jp,
                      compound="top",
                      style='estilo_bt.TButton',
                      width=20)

botao.grid(row=0, column=0)

root.mainloop()
