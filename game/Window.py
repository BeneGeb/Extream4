from tkinter import *
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

        labelSpieleranzahl = Label(
            master=tkFenster, text="Spieleranzahl", bg="white", font=("Arial", 14)
        )
        labelSpieleranzahl.place(x=45, y=80)

        labelMehrspieler = Label(
            master=tkFenster, text="Mehrspieler", bg="white", font=("Arial", 14)
        )
        labelMehrspieler.place(x=45, y=140)

        labelSolospieler = Label(
            master=tkFenster, text="Solo", bg="white", font=("Arial", 14)
        )
        labelSolospieler.place(x=220, y=140)

        labelEigenschaftenspieler = Label(
            master=tkFenster,
            text="Spielereigenschaften einstellen",
            bg="white",
            font=("Arial", 14),
        )
        labelEigenschaftenspieler.place(x=45, y=210)

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

        Solobutton = Radiobutton(tkFenster, variable=v, bg="white", value=1)
        Solobutton.place(x=300, y=140)

        Mehrbutton = Radiobutton(tkFenster, variable=v, bg="white", value=2)
        Mehrbutton.place(x=175, y=140)

        # Aktivierung des Fensters
        tkFenster.mainloop()

    def startGame(self, tkfenster):
        tkfenster.quit()
        game = Game(1142, 1008, ["red", "yellow", "blue", "green"])
        game.runGame()
