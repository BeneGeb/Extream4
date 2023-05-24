from tkinter import *
from tkinter import messagebox
import customtkinter
from CTkColorPicker import AskColor
from PIL import Image
from .settings import Settings
import math
import pygame
from .Game import *

class Window:
    def __init__(self, callBackStartGame):
        self.callBackStartGame = callBackStartGame

        customtkinter.set_appearance_mode("dark")
        window = customtkinter.CTk()
        window.title("Mensch ärgere dich nicht")
        window.geometry("673x366")
        window.resizable(0,0)
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0, weight=1)
    
        window_width = 673
        window_height = 366

        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # x- und y-Position für das Fenster
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)

        # Setzen der Größe und Position des Fensters
        window.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))


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

        self.KI_Check_dict = {"Mensch": False, "KI": True}
        OPTIONS = list(self.KI_Check_dict.keys())

        self.player_1 = StringVar(frame)
        self.player_1.set(OPTIONS[0])  # default value

        self.player_2 = StringVar(frame)
        self.player_2.set(OPTIONS[0])  # default value

        self.player_3 = StringVar(frame)
        self.player_3.set(OPTIONS[0])  # default value

        self.player_4 = StringVar(frame)
        self.player_4.set(OPTIONS[0])  # default value

        drop1 = customtkinter.CTkOptionMenu(master =frame,values = ["Mensch", "KI"], variable = self.player_1)
        drop2 = customtkinter.CTkOptionMenu(master =frame, values = ["Mensch", "KI"], variable = self.player_1)
        drop3 = customtkinter.CTkOptionMenu(master =frame, values = ["Mensch", "KI"], variable = self.player_1)
        drop4 = customtkinter.CTkOptionMenu(master =frame, values = ["Mensch", "KI"], variable = self.player_1)

        drop1.grid(row = 1, column = 1, padx=12, pady= 12, sticky="nsew")
        drop2.grid(row = 2, column = 1, padx=12, pady= 12, sticky="nsew")
        drop3.grid(row = 3, column = 1, padx=12, pady= 12, sticky="nsew")
        drop4.grid(row = 4, column = 1, padx=12, pady= 12, sticky="nsew")

        img= customtkinter.CTkImage(Image.open("Farbeimer.png"), size=(26, 26))

        def hex_to_rgb(value):
            value = value.lstrip('#')
            lv = len(value)
            return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

        def ask_color1():
            pick_color = AskColor()  # open the color picker
            color = pick_color.get()  # get the color string
            Settings.listPlayers[0].color = hex_to_rgb(color) 
            button_color1.configure(fg_color=color)

        def ask_color2():
            pick_color = AskColor()  # open the color picker
            color = pick_color.get()  # get the color string
            Settings.listPlayers[1].color = hex_to_rgb(color) 
            button_color2.configure(fg_color=color)

        def ask_color3():
            pick_color = AskColor()  # open the color picker
            color = pick_color.get()  # get the color string
            Settings.listPlayers[2].color = hex_to_rgb(color) 
            button_color3.configure(fg_color=color)

        def ask_color4():
            pick_color = AskColor()  # open the color picker
            color = pick_color.get()  # get the color string
            Settings.listPlayers[3].color = hex_to_rgb(color) 
            button_color4.configure(fg_color=color)

        button_color1 = customtkinter.CTkButton(master = frame, image = img, text = "", height = 25, width = 25, fg_color = "RED", command=ask_color1)
        button_color2 = customtkinter.CTkButton(master = frame, image = img, text = "", height = 25, width = 25, fg_color = "YELLOW",command=ask_color2)
        button_color3 = customtkinter.CTkButton(master = frame, image = img, text = "", height = 25, width = 25, fg_color = "BLUE",command=ask_color3)
        button_color4 = customtkinter.CTkButton(master = frame, image = img, text = "", height = 25, width = 25, fg_color = "GREEN",command=ask_color4)

        button_color1.grid (row=1, column= 2, padx=35, pady= 12, sticky="nsew")
        button_color2.grid (row=2, column= 2, padx=35, pady= 12, sticky="nsew")
        button_color3.grid (row=3, column= 2, padx=35, pady= 12, sticky="nsew")
        button_color4.grid (row=4, column= 2, padx=35, pady= 12, sticky="nsew")

        self.entry1 = customtkinter.CTkEntry(master= frame1, placeholder_text="Name")
        self.entry2 = customtkinter.CTkEntry(master= frame1, placeholder_text="Name")
        self.entry3 = customtkinter.CTkEntry(master= frame1, placeholder_text="Name")
        self.entry4 = customtkinter.CTkEntry(master= frame1, placeholder_text="Name")

        self.entry1.grid (row = 0, column = 0, padx=12, pady= 12, sticky="nsew")
        self.entry2.grid (row = 1, column = 0, padx=12, pady= 12, sticky="nsew")
        self.entry3.grid (row = 2, column = 0, padx=12, pady= 12, sticky="nsew")
        self.entry4.grid (row = 3, column = 0, padx=12, pady= 12, sticky="nsew")

        switch_var = customtkinter.StringVar(value="Extream")
        switch_1 = customtkinter.CTkSwitch(master=frame, switch_height=25, switch_width= 45, font=('Helvetica', 16), textvariable=switch_var, variable=switch_var, onvalue="Extream", offvalue="Normal")
        switch_1.grid(row=0, column = 1, padx = 10)

        def SameColorModus():
            self.startGame(window, 3)

        def CheckGameMode(window):
            GameMode = switch_var.get()
            if GameMode == "Extream":
                SameColorModus()
            else:
                self.startGame(window, 1)  
                                    
        startButton  = customtkinter.CTkButton(master=frame, text = "START", fg_color= "#e60000", font=('Helvetica', 13), hover_color = "#ff6666", command= lambda: CheckGameMode(window))
        startButton.grid(row=0, column = 3, padx = 10)

        def LoadPreviousGame():
            self.gameState = GameState()
            loadedState = self.gameState.loadGameState()
            Settings.listPlayers = loadedState.listPlayers
            self.startGame(window, 2)

        continueButton  = customtkinter.CTkButton(master=frame, text = "FORTSETZEN", fg_color= "#e60000", font=('Helvetica', 13), hover_color = "#ff6666", command= lambda: LoadPreviousGame())
        continueButton.grid(row=0, column = 2, padx = 20)

        window.mainloop()

    def startGame(self, window, GameVersion):

        # KI Boolean-Werte holen

        Settings.listPlayers[0].isKi = self.KI_Check_dict[self.player_1.get()]
        Settings.listPlayers[1].isKi = self.KI_Check_dict[self.player_2.get()]
        Settings.listPlayers[2].isKi = self.KI_Check_dict[self.player_3.get()]
        Settings.listPlayers[3].isKi = self.KI_Check_dict[self.player_4.get()]

        # Spielernamen holen

        PlayerName1 = self.entry1.get()
        PlayerName2 = self.entry2.get()
        PlayerName3 = self.entry3.get()
        PlayerName4 = self.entry4.get()

        # Überprüfung leeren Namen

        if PlayerName1 != "":
            Settings.listPlayers[0].name = PlayerName1
        if PlayerName2 != "":
            Settings.listPlayers[1].name = PlayerName2
        if PlayerName3 != "":
            Settings.listPlayers[2].name = PlayerName3
        if PlayerName4 != "":
            Settings.listPlayers[3].name = PlayerName4

        # Ki_Namen
        for i in range(4):
            if Settings.listPlayers[i].isKi:
                Settings.listPlayers[i].name = f"KI_{i+1}"
        
        def hex_to_rgb(value):
            value = value.lstrip('#')
            lv = len(value)
            return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

        # Kontrolle der Farben Gleichheit

        # hier wird die Differenz bestimmt
        def colormath(rgb, rgb2):
            r1, g1, b1 = rgb
            r2, g2, b2 = rgb2

            return math.sqrt((r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2)

        # hier geht die Suche mit den Farben ähnlichkeit los
        stop = False
        startgame = False
        for i in range(len(Settings.listPlayers)):
            if stop:
                break
            for j in range(i + 1, len(Settings.listPlayers)):
                print(Settings.listPlayers[j].color)
                distanz = colormath(
                    Settings.listPlayers[i].color, Settings.listPlayers[j].color
                )
                if (
                    distanz < Settings.COLOR_DISTANCE
                ):  # Schwellenwert: Je höher, desto strenger
                    messagebox.showinfo(
                        "Info",
                        f"Die Farben von {Settings.listPlayers[i].name} und {Settings.listPlayers[j].name} sind zu ähnlich.",
                    )
                    stop = True
                    startgame = False

                    break
                else:
                    # Musik beenden
                    pygame.mixer.music.stop()
                    startgame = True
                    # tkfenster.destroy()

                    # game = Game()
                    # game.runGame()

        # print(self.color_list)

        # Settings.listPlayers[0].name= self.Namefield.get()
        # Settings.listPlayers[1].name= self.Namefield2.get()
        # Settings.listPlayers[2].name= self.Namefield3.get()
        # Settings.listPlayers[3].name= self.Namefield4.get()
        if startgame:
            window.destroy()
            if GameVersion == 2:
                loadedState = self.gameState.loadGameState()
                self.callBackStartGame(loadedState)
            if GameVersion == 3:
                sameColorMode = True

                for i in range(4):
                    Settings.listPlayers[i].color = Settings.RED

                self.callBackStartGame(None, sameColorMode)
            else:
                self.callBackStartGame()
