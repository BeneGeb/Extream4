from tkinter import *
from tkinter import colorchooser
from .Game import Game


class Window:
    def __init__(self):
        # Erzeugung des Fensters
        tkFenster = Tk()
        tkFenster.title("Mensch ärgere dich nicht")
        tkFenster.geometry("673x366")
        tkFenster["background"] = "white"
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
            labelplayer.place(x=45, y=40 + (i * 40))

        # Button
        v = IntVar()
        # Hier ist der Startbutton/ mit der Funktion command beschreibt man die aktion, die ausgeführt werden soll.
        # im Command wird die Aktion aufgerufen
        buttonStart = Button(
            tkFenster,
            text="Start",
            bg="white",
            font=("Arial", 14),
            command=lambda: self.startGame(tkFenster),
        )
        buttonStart.place(x=45, y=250, width=50, height=50)

        # Dropdown Menü
        OPTIONS = ["Mensch", "KI"]

        player_1 = StringVar(tkFenster)
        player_1.set(OPTIONS[0])  # default value

        player_2 = StringVar(tkFenster)
        player_2.set(OPTIONS[0])  # default value

        player_3 = StringVar(tkFenster)
        player_3.set(OPTIONS[0])  # default value

        player_4 = StringVar(tkFenster)
        player_4.set(OPTIONS[0])  # default value

        drop0 = OptionMenu(tkFenster, player_1, *OPTIONS)
        drop1 = OptionMenu(tkFenster, player_2, *OPTIONS)
        drop2 = OptionMenu(tkFenster, player_3, *OPTIONS)
        drop3 = OptionMenu(tkFenster, player_4, *OPTIONS)
        drop0.pack()
        drop1.pack()
        drop2.pack()
        drop3.pack()

        def ok():
            print("value is:" + player_1.get())

        # button = Button(tkFenster, text="OK", command=ok)
        # button.pack()
        # button.place(x=175, y=180)

        drop0.place(x=130, y=80)
        drop1.place(x=130, y=120)
        drop2.place(x=130, y=160)
        drop3.place(x=130, y=200)

        # Farbraster

        def color():
            the_color = colorchooser.askcolor()
            print(the_color)

        collor_button_player1 = Button(
            tkFenster, text="Wähle deine Farbe", command=color
        )
        collor_button_player1.pack()
        collor_button_player1.place(x=230, y=80)

        collor_button_player2 = Button(
            tkFenster, text="Wähle deine Farbe", command=color
        )
        collor_button_player2.pack()
        collor_button_player2.place(x=230, y=120)

        collor_button_player3 = Button(
            tkFenster, text="Wähle deine Farbe", command=color
        )
        collor_button_player3.pack()
        collor_button_player3.place(x=230, y=160)

        collor_button_player4 = Button(
            tkFenster, text="Wähle deine Farbe", command=color
        )
        collor_button_player4.pack()
        collor_button_player4.place(x=230, y=200)

        # Namen input Filed
        # Label(tkFenster, text="Name")
        # Label(tkFenster, text="Name")

        e1 = Entry(tkFenster, width=15)
        e2 = Entry(tkFenster, width=15)

        e1.pack()
        e2.pack()
        e1.place(x=320, y=80)
        e1.place(x=320, y=120)

        # Aktivierung des Fensters
        tkFenster.mainloop()

        # Spielstarten

    def startGame(self, tkfenster):
        tkfenster.destroy()

        game = Game()
        game.runGame()
