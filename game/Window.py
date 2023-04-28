from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import Canvas
import math
import pygame
from .settings import Settings


class Window:
    def __init__(self, callBackStartGame):
        # Erzeugung des Fensters
        tkFenster = Tk()
        pygame.mixer.init()
        tkFenster.title("Mensch ärgere dich nicht")
        tkFenster.geometry("673x366")
        tkFenster["background"] = "white"
        p1 = PhotoImage(file="Extream4.png")
        tkFenster.iconphoto(True, p1)

        self.callBackStartGame = callBackStartGame

        window_width = 673
        window_height = 366

        screen_width = tkFenster.winfo_screenwidth()
        screen_height = tkFenster.winfo_screenheight()

        # x- und y-Position für das Fenster
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)

        # Setzen der Größe und Position des Fensters
        tkFenster.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

        # Beschriftung
        labelMenue = Label(
            master=tkFenster, text="Menü", bg="white", font=("Arial", 18, "bold")
        )
        labelMenue.place(x=45, y=30)

        for i in range(1, 5):

            labelplayer = Label(
                master=tkFenster,
                text="Player " + str(i),
                bg="white",
                font=("Arial", 10),
            )
            labelplayer.place(x=45, y=45 + (i * 45))

        # Button
        v = IntVar()

        # Hintergrund Musik
        pygame.mixer.music.load("Menü_Sound.mp3")
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.5)

        # Hier ist der Startbutton/ mit der Funktion command beschreibt man die aktion, die ausgeführt werden soll.
        # im Command wird die Aktion aufgerufen
        buttonStart = Button(
            tkFenster,
            text="Start",
            bg="white",
            bd=2,
            font=("Arial", 14),
            command=lambda: self.startGame(tkFenster),
        )
        buttonStart.place(x=300, y=280, width=70, height=50)

        # Dropdown Menü
        # OPTIONS = ["Mensch", "KI"]
        self.KI_Check_dict = {"Mensch": False, "KI": True}
        OPTIONS = list(self.KI_Check_dict.keys())

        self.player_1 = StringVar(tkFenster)
        self.player_1.set(OPTIONS[0])  # default value

        self.player_2 = StringVar(tkFenster)
        self.player_2.set(OPTIONS[0])  # default value

        self.player_3 = StringVar(tkFenster)
        self.player_3.set(OPTIONS[0])  # default value

        self.player_4 = StringVar(tkFenster)
        self.player_4.set(OPTIONS[0])  # default value

        drop0 = OptionMenu(tkFenster, self.player_1, *OPTIONS)
        drop1 = OptionMenu(tkFenster, self.player_2, *OPTIONS)
        drop2 = OptionMenu(tkFenster, self.player_3, *OPTIONS)
        drop3 = OptionMenu(tkFenster, self.player_4, *OPTIONS)
        drop0.pack()
        drop1.pack()
        drop2.pack()
        drop3.pack()

        # def ok():
        # print("value is:" + player_1.get())

        # button = Button(tkFenster, text="OK", command=ok)
        # button.pack()
        # button.place(x=175, y=180)

        drop0.place(x=140, y=85)
        drop1.place(x=140, y=130)
        drop2.place(x=140, y=175)
        drop3.place(x=140, y=220)

        # Farbraster

        # self.color_list=[]

        def color(button_id):
            the_color = colorchooser.askcolor()[0]
            if the_color == None:
                return

            # Switch Cases um zu erkennen, welcher Button betätigt wurde und die Farben der Spieler zu bestimmen

            match button_id:
                case 1:
                    Settings.listPlayers[0].color = the_color
                    SquareColor(button_id, the_color)
                    # self.color_list.insert(0,(the_color))

                case 2:
                    Settings.listPlayers[1].color = the_color
                    SquareColor(button_id, the_color)
                    # self.color_list.insert(1,(the_color))

                case 3:
                    Settings.listPlayers[2].color = the_color
                    SquareColor(button_id, the_color)
                    # self.color_list.insert(2,(the_color))

                case 4:
                    Settings.listPlayers[3].color = the_color
                    SquareColor(button_id, the_color)
                    # self.color_list.insert(3,(the_color))

        collor_button_player1 = Button(
            tkFenster, text="Farbe", command=lambda: color(1)
        )
        collor_button_player1.pack()
        collor_button_player1.place(x=275, y=85)

        collor_button_player2 = Button(
            tkFenster, text="Farbe", command=lambda: color(2)
        )
        collor_button_player2.pack()
        collor_button_player2.place(x=275, y=130)

        collor_button_player3 = Button(
            tkFenster, text="Farbe", command=lambda: color(3)
        )
        collor_button_player3.pack()
        collor_button_player3.place(x=275, y=175)

        collor_button_player4 = Button(
            tkFenster, text="Farbe", command=lambda: color(4)
        )
        collor_button_player4.pack()
        collor_button_player4.place(x=275, y=220)

        # Farbraster kleines Vorschau Quadrat
        def SquareColor(id, the_color):
            square = Canvas(tkFenster, width=20, height=20)
            square.pack()
            player_color = "#%02x%02x%02x" % (the_color)

            x1, y1 = 0, 0
            x2, y2 = x1 + 20, y1 + 20
            square.create_rectangle(x1, y1, x2, y2, fill=player_color)

            match id:
                case 1:
                    square.place(x=340, y=90)

                case 2:
                    square.place(x=340, y=135)

                case 3:
                    square.place(x=340, y=180)

                case 4:
                    square.place(x=340, y=225)

        # Vorschau Quadrate
        for j, k in zip(range(1, 5), range(4)):
            SquareColor(j, Settings.listPlayers[k].color)

        # Namen input Filed
        NameLabel = Label(tkFenster, text="Name:")
        NameLabel2 = Label(tkFenster, text="Name:")
        NameLabel3 = Label(tkFenster, text="Name:")
        NameLabel4 = Label(tkFenster, text="Name:")
        NameLabel.place(x=380, y=85)
        NameLabel2.place(x=380, y=130)
        NameLabel3.place(x=380, y=175)
        NameLabel4.place(x=380, y=220)

        self.Namefield = Entry(tkFenster, borderwidth=2, relief="solid")
        self.Namefield2 = Entry(tkFenster, borderwidth=2, relief="solid")
        self.Namefield3 = Entry(tkFenster, borderwidth=2, relief="solid")
        self.Namefield4 = Entry(tkFenster, borderwidth=2, relief="solid")
        # self.Namefield.insert(0,"text")
        self.Namefield.place(x=440, y=85)
        self.Namefield2.place(x=440, y=130)
        self.Namefield3.place(x=440, y=175)
        self.Namefield4.place(x=440, y=220)

        # Aktivierung des Fensters
        tkFenster.mainloop()

        # Spielstarten

    def startGame(self, tkfenster):

        # KI Boolean-Werte holen

        Settings.listPlayers[0].isKi = self.KI_Check_dict[self.player_1.get()]
        Settings.listPlayers[1].isKi = self.KI_Check_dict[self.player_2.get()]
        Settings.listPlayers[2].isKi = self.KI_Check_dict[self.player_3.get()]
        Settings.listPlayers[3].isKi = self.KI_Check_dict[self.player_4.get()]

        # Spielernamen holen

        PlayerName1 = self.Namefield.get()
        PlayerName2 = self.Namefield2.get()
        PlayerName3 = self.Namefield3.get()
        PlayerName4 = self.Namefield4.get()

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
            tkfenster.destroy()

            self.callBackStartGame()
