from tkinter import *
import customtkinter
from .settings import Settings


class Window_Finished:
    def __init__(self, callBackStartWindow, placement, gameField):
        self.callBackStartGame = callBackStartWindow

        customtkinter.set_appearance_mode("dark")
        window = customtkinter.CTk()
        window.title("Mensch ärgere dich nicht")
        window.geometry("673x366")
        window.resizable(0, 0)
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0, weight=1)

        window_width = 673
        window_height = 366

        # Breite und Höhe des Bildschirms
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        # x- und y-Position für das Fenster
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)

        # Setzen der Größe und Position des Fensters
        window.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

        frame = customtkinter.CTkFrame(master=window)
        frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        frame.grid_columnconfigure((0, 1), weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame1 = customtkinter.CTkFrame(master=frame)
        frame1.grid(row=0, column=1, rowspan=5, padx=10, pady=10, sticky="nsew")
        frame1.grid_columnconfigure(0, weight=1)
        frame1.grid_rowconfigure((0, 1), weight=1)
        frame2 = customtkinter.CTkFrame(master=frame)
        frame2.grid(row=0, column=0, rowspan=5, padx=10, pady=10, sticky="nsew")
        frame2.grid_columnconfigure((0, 1, 2), weight=1)
        frame2.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        #Beschriftung
        labelMenue = customtkinter.CTkLabel(
            master=frame2,
            text=f"Glückwünsch {Settings.listPlayers[placement].name}",
            width=70,
            height=30,
            font=("Helvetica", 25),
            fg_color="#4d4d4d",
            corner_radius=5,
        )
        labelMenue.grid(row=0, column=0, columnspan= 3, padx=12, pady=12, sticky="nsew")

        # Liste der Spieler
        playerSortedPlacementDict = {}

        for i in range(len(Settings.listPlayers)):
            playerSortedPlacementDict[Settings.listPlayers[i]
                                      .name] = gameField.placementlist[i]

        sorted_dict = dict(
            sorted(playerSortedPlacementDict.items(), key=lambda x: x[1], reverse=True))
        print(sorted_dict)

        # Dict_Keys in Liste
        key_list = list(sorted_dict.keys())

        # Values in Liste
        values_list = list(sorted_dict.values())

        # Liste der Platzierung
        place_list = []
        previous_value = None
        previous_place = None
        for i, value in enumerate(values_list):
            if value != previous_value:
                place = i + 1
                previous_place = place
                place_list.append(previous_place)
            else:
                place = previous_place
                place_list.append(place)
            previous_value = value
        print("hier", place_list)

        # Farben Platzierung 
        placecolor= ("#f7d934",
                     "#aaa9ad",
                     "#cd7f32",
                     "#873e23")
        
        # ListeSpieler Output
        # Platzierung Heckmeck
        for i, j in zip(range(1, 5), range(4)):
            labelplace = customtkinter.CTkLabel(
                master=frame2,
                # text=str(i) + "." + " " + "Player " + str(i),
                text=f"{place_list[j]}.Platz",
                corner_radius=5, 
                fg_color= placecolor[(-1)+place_list[j]],
                font=("Arial", 14),
            )
            labelplace.grid(row=0+i, column=0, padx=12, pady=12, sticky="nsew")

            labelplayer = customtkinter.CTkLabel(
                master=frame2,
                # text=str(i) + "." + " " + "Player " + str(i),
                text=f"{key_list[j]}" + " " + ":" +f"{values_list[j]} Spieler im Hausfeld",
                corner_radius=5, 
                fg_color="#4d4d4d",
                font=("Arial", 14),
            )
            labelplayer.grid(row=0+i, column=1, columnspan = 2, padx=12, pady=12, sticky="nsew")

        buttonStart  = customtkinter.CTkButton(
            master=frame1, 
            text = "Neustart", 
            fg_color= "#31b031",
            font=('Helvetica', 30), 
            hover_color = "#72cf72", 
            corner_radius=10, 
            command= lambda: self.Restart(window))
    
        buttonStart.grid(row=0, column = 0, padx = 35, pady= 35, sticky="nsew")

        buttonEnd  = customtkinter.CTkButton(
            master=frame1, 
            text = "Beenden", 
            fg_color= "#c73636",
            font=('Helvetica', 30), 
            hover_color = "#cc7676",
            corner_radius=10, 
            command= lambda: self.Quit(window))
    
        buttonEnd.grid(row=1, column = 0, padx = 35, pady = 35, sticky="nsew")

        # Aktivierung des Fensters
        window.mainloop()

    def Restart(self, tkfenster):

        tkfenster.destroy()
        self.callBackStartWindow()

    def Quit(self, tkfenster):

        tkfenster.destroy()
