from tkinter import *
import customtkinter
from CTkColorPicker import AskColor
from PIL import Image

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
window.title("Mensch ärgere dich nicht")
window.geometry("673x366")
window.resizable(0,0)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

frame = customtkinter.CTkFrame(master = window)
frame.grid(row = 0, column = 0, padx = 20, pady = 20, sticky="nsew")
frame.grid_columnconfigure((0,1,2,3), weight=1)
frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
frame1 = customtkinter.CTkFrame(master = frame)
frame1.grid(row = 1, column = 3, rowspan = 4, padx = 10, pady= 10, sticky="nsew")
frame1.grid_columnconfigure(0, weight=1)
frame1.grid_rowconfigure((0,1,2,3), weight=1)

label1 = customtkinter.CTkLabel(master = frame, text = "Menü", width=70, height=30, font=('Helvetica', 30), fg_color="#4d4d4d", corner_radius = 5)
label2 = customtkinter.CTkLabel(master = frame, text = "Player1", corner_radius = 5, fg_color = "#4d4d4d")
label3 = customtkinter.CTkLabel(master = frame, text = "Player2", corner_radius = 5, fg_color = "#4d4d4d")
label4 = customtkinter.CTkLabel(master = frame, text = "Player3", corner_radius = 5, fg_color = "#4d4d4d")
label5 = customtkinter.CTkLabel(master = frame, text = "Player4", corner_radius = 5, fg_color = "#4d4d4d")

label1.grid(row = 0, column = 0, padx=12, pady= 12, sticky="nsew")
label2.grid(row = 1, column = 0, padx=12, pady= 12, sticky="nsew")
label3.grid(row = 2, column = 0, padx=12, pady= 12, sticky="nsew")
label4.grid(row = 3, column = 0, padx=12, pady= 12, sticky="nsew")
label5.grid(row = 4, column = 0, padx=12, pady= 12, sticky="nsew")

combobox1 = customtkinter.CTkOptionMenu(master =frame, values=["Mensch", "KI"])
combobox2 = customtkinter.CTkOptionMenu(master =frame, values=["Mensch", "KI"])
combobox3 = customtkinter.CTkOptionMenu(master =frame, values=["Mensch", "KI"])
combobox4 = customtkinter.CTkOptionMenu(master =frame, values=["Mensch", "KI"])

combobox1.grid(row = 1, column = 1, padx=12, pady= 12, sticky="nsew")
combobox2.grid(row = 2, column = 1, padx=12, pady= 12, sticky="nsew")
combobox3.grid(row = 3, column = 1, padx=12, pady= 12, sticky="nsew")
combobox4.grid(row = 4, column = 1, padx=12, pady= 12, sticky="nsew")

img= customtkinter.CTkImage(Image.open("Farbeimer.png"), size=(26, 26))

button_color1 = customtkinter.CTkButton(master = frame, image = img, text = "", height = 25, width = 25, fg_color = "RED", command=ask_color1)
button_color2 = customtkinter.CTkButton(master = frame, image = img, text = "", height = 25, width = 25, fg_color = "YELLOW",command=ask_color2)
button_color3 = customtkinter.CTkButton(master = frame, image = img, text = "", height = 25, width = 25, fg_color = "BLUE",command=ask_color3)
button_color4 = customtkinter.CTkButton(master = frame, image = img, text = "", height = 25, width = 25, fg_color = "GREEN",command=ask_color4)

button_color1.grid (row=1, column= 2, padx=35, pady= 12, sticky="nsew")
button_color2.grid (row=2, column= 2, padx=35, pady= 12, sticky="nsew")
button_color3.grid (row=3, column= 2, padx=35, pady= 12, sticky="nsew")
button_color4.grid (row=4, column= 2, padx=35, pady= 12, sticky="nsew")

entry1 = customtkinter.CTkEntry(master= frame1, placeholder_text="Name")
entry2 = customtkinter.CTkEntry(master= frame1, placeholder_text="Name")
entry3 = customtkinter.CTkEntry(master= frame1, placeholder_text="Name")
entry4 = customtkinter.CTkEntry(master= frame1, placeholder_text="Name")

entry1.grid (row = 0, column = 0, padx=12, pady= 12, sticky="nsew")
entry2.grid (row = 1, column = 0, padx=12, pady= 12, sticky="nsew")
entry3.grid (row = 2, column = 0, padx=12, pady= 12, sticky="nsew")
entry4.grid (row = 3, column = 0, padx=12, pady= 12, sticky="nsew")
                               
button  = customtkinter.CTkButton(master=frame, text = "START", fg_color= "#e60000", font=('Helvetica', 15), hover_color = "#ff6666")
button.grid(row= 0, column = 3, padx = 10)

window.mainloop()