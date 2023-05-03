from tkinter import *
from .settings import Settings


class Window_Finished:
    def __init__(self, callBackStartWindow, placement):
        self.callBackStartWindow = callBackStartWindow
        tkFenster = Tk()
        tkFenster.title("Mensch ärgere dich nicht")
        tkFenster.geometry("673x366")
        tkFenster["background"] = "white"
        p1 = PhotoImage(file="Extream4.png")

        tkFenster.iconphoto(True, p1)

        window_width = 673
        window_height = 366

        # Breite und Höhe des Bildschirms
        screen_width = tkFenster.winfo_screenwidth()
        screen_height = tkFenster.winfo_screenheight()

        # x- und y-Position für das Fenster
        x = (screen_width / 2) - (window_width / 2)
        y = (screen_height / 2) - (window_height / 2)

        # Setzen der Größe und Position des Fensters
        tkFenster.geometry("%dx%d+%d+%d" % (window_width, window_height, x, y))

        # Beschriftung
        labelMenue = Label(
            master=tkFenster,
            text=f"Glückwünsch {Settings.listPlayers[placement].name}",
            bg="white",
            font=("Arial", 18, "bold"),
        )
        labelMenue.place(x=45, y=30)

        # Liste der Spieler
        for i in range(1, 5):

            labelplayer = Label(
                master=tkFenster,
                # text=str(i) + "." + " " + "Player " + str(i),
                text=str(i) + "." + Settings.listPlayers[i - 1].name,
                bg="white",
                font=("Arial", 10),
            )
            labelplayer.place(x=45, y=40 + (i * 40))

        buttonStart = Button(
            tkFenster,
            text="Neustart",
            bg="white",
            font=("Arial", 14),
            command=lambda: self.Restart(tkFenster),
        )
        buttonStart.place(x=45, y=250, width=100, height=50)

        buttonEnd = Button(
            tkFenster,
            text="Beenden",
            bg="white",
            font=("Arial", 14),
            command=lambda: self.Quit(tkFenster),
        )
        buttonEnd.place(x=165, y=250, width=100, height=50)

        # Aktivierung des Fensters
        tkFenster.mainloop()

    def Restart(self, tkfenster):

        tkfenster.destroy()
        self.callBackStartWindow()

    def Quit(self, tkfenster):

        tkfenster.destroy()
