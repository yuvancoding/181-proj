from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

root = Tk()
root.geometry("1080x400")
root.confid(bg = '#zF2CCC3')
root.title("Language Translator")

language = list(LANGUAGES.values())
title_label = Label(root, text = "LANGUAGE TRANSLATOR", bg='#F2CCC3', fonts =("Sylfane", 18, "bold", "italic"))
title_label.place(relx=0.5,rely=0.1,achpr=CENTER)

input_label = Label(root,text="Enter Text", font = 'arial 13 bold', bg="#F2CCC3")
input_label.place(relx=0.02,rely=0.2, anchor= CENTER)
src_lang = ttk.Combobox(root, values=language, width=22, state="readonly")
src_lang.place(relx=0.13,rely=0.2,anchor=W)
scr_lang.set('english')

output_label = Label(root,text="Output", font = 'arial 13 bold', bg="#F2CCC3")
output_label.place(relx=0.81,rely=0.2, anchor= E)
dest_lang = ttk.Combobox(root, values=language, width=22, state="readonly")
dest_lang.place(relx=0.98,rely=0.2,anchor=E)
dest_lang.set('choose output language')

Input_text = Text(root,font='arial 10', height = 11, wrap = WORD, padx=5, pady=5, width=60, bg="#FFFCF9", bd=0)
Input_text.place(relx=0.03,rely=0.5,anchor=W)
Output_text = Text(root,font='arial 10', height = 11, wrap = WORD, padx=5, pady=5, width=60, bg="#FFFCF9", bd=0)
Output_text.place(relx=0.98,rely=0.5,anchor=W)