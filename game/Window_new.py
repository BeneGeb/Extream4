from tkinter import *
import customtkinter
from CTkColorPicker import AskColor


def ask_color1():
    pick_color = AskColor()  # open the color picker
    color = pick_color.get()  # get the color string
    button_color1.configure(fg_color=color)

def ask_color2():
    pick_color = AskColor()  # open the color picker
    color = pick_color.get()  # get the color string
    button_color2.configure(fg_color=color)

def ask_color3():
    pick_color = AskColor()  # open the color picker
    color = pick_color.get()  # get the color string
    button_color3.configure(fg_color=color)

def ask_color4():
    pick_color = AskColor()  # open the color picker
    color = pick_color.get()  # get the color string
    button_color4.configure(fg_color=color)

window = customtkinter.CTk()
window.geometry("673x366")
window.grid_columnconfigure((0,1,2,3,4,5), weight=1)
window.grid_rowconfigure((0,1,2,3,4,5), weight=1)

label1 = customtkinter.CTkLabel(master = window, text = "Menue", width=70, height=30, font=('Helvetica', 30))
label2 = customtkinter.CTkLabel(master = window, text = "Player1", corner_radius = 5, fg_color = "#4d4d4d", width=70, height=30)
label3 = customtkinter.CTkLabel(master = window, text = "Player2", corner_radius = 5, fg_color = "#4d4d4d", width=70, height=30)
label4 = customtkinter.CTkLabel(master = window, text = "Player3", corner_radius = 5, fg_color = "#4d4d4d", width=70, height=30)
label5 = customtkinter.CTkLabel(master = window, text = "Player4", corner_radius = 5, fg_color = "#4d4d4d", width=70, height=30)

label1.grid(row = 0, column = 0)
label2.grid(row = 1, column = 0)
label3.grid(row = 2, column = 0)
label4.grid(row = 3, column = 0)
label5.grid(row = 4, column = 0)

combobox1 = customtkinter.CTkOptionMenu(master =window, values=["Mensch", "KI"])
combobox2 = customtkinter.CTkOptionMenu(master =window, values=["Mensch", "KI"])
combobox3 = customtkinter.CTkOptionMenu(master =window, values=["Mensch", "KI"])
combobox4 = customtkinter.CTkOptionMenu(master =window, values=["Mensch", "KI"])

combobox1.grid(row = 1, column = 1)
combobox2.grid(row = 2, column = 1)
combobox3.grid(row = 3, column = 1)
combobox4.grid(row = 4, column = 1)

img = PhotoImage(file ="Farbeimer.png")


button_color1 = customtkinter.CTkButton(master = window, image = img, text = "", height = 25, width = 25, command=ask_color1)
button_color2 = customtkinter.CTkButton(master = window, image = img, text = "", height = 25, width = 25, command=ask_color2)
button_color3 = customtkinter.CTkButton(master = window, image = img, text = "", height = 25, width = 25, command=ask_color3)
button_color4 = customtkinter.CTkButton(master = window, image = img, text = "", height = 25, width = 25, command=ask_color4)

button_color1.grid (row=1, column= 2)
button_color2.grid (row=2, column= 2)
button_color3.grid (row=3, column= 2)
button_color4.grid (row=4, column= 2)

button  = customtkinter.CTkButton(master=window, text = "START")
button.place(relx=0.5, rely = 0.5, anchor = CENTER)
button.grid(row= 5, column = 2, sticky="EW")

window.mainloop()
