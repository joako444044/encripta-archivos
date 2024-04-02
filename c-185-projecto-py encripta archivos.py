# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:06:32 2024

@author: joako
"""

from tkinter import *
from tkinter import filedialog as fd
import hashlib

root=Tk()
root.geometry("250x190")

def apply_md5():
    print("Función MD5")
    file = fd.askopenfilename(title="Text",filetypes=(("Text Document","*.txt"),))
    print(file)
    read_f = open(file,"r")
    readed_fil = read_f.read()
    hex_f = hashlib.md5(readed_fil.encode())
    hexed_file = hex_f.hexdigest()
    name = file.split(".")[0]
    exit_f = open(name + "-encoded,md5.txt","w")
    exit_f.write(hexed_file)
    print(hexed_file)
    
def apply_sha256():
    print("Función SHA")   
    file = fd.askopenfilename(title="Text",filetypes=(("Text Document","*.txt"),))
    print(file)
    read_f = open(file,"r")
    readed_fil = read_f.read()
    hex_f = hashlib.sha256(readed_fil.encode())
    hexed_file = hex_f.hexdigest()
    name = file.split(".")[0]
    exit_f = open(name + "-encoded,sha256.txt","w")
    exit_f.write(hexed_file)
    print(hexed_file)
    
btn=Button(root, text="Aplicar MD5",command=apply_md5)
btn.place(relx=0.3,rely=0.5, anchor=CENTER)
btn1=Button(root, text="Aplicar SHA256",command=apply_sha256)
btn1.place(relx=0.7,rely=0.5, anchor=CENTER)
root.mainloop()