from tkinter import *

class Window_RageQuit:
    def __init__(self, callBackStartWindow, player_name):
        self.callBackStartWindow = callBackStartWindow
        tkFenster = Tk()
        tkFenster.title("Mensch ärgere dich nicht")
        tkFenster.geometry("400x200")
        tkFenster["background"] = "white"
        
        window_width = 400
        window_height = 200

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
            text=f"Spieler {player_name} just ragequitted!",
            bg="white",
            font=("Arial", 18, "bold"),
        )
        labelMenue.place(x=50, y=50)

        buttonStart = Button(
            tkFenster,
            text="Neustart",
            bg="white",
            font=("Arial", 14),
            command=lambda: self.Restart(tkFenster),
        )
        buttonStart.place(x=50, y=100, width=100, height=50)

        buttonEnd = Button(
            tkFenster,
            text="Beenden",
            bg="white",
            font=("Arial", 14),
            command=lambda: self.Quit(tkFenster),
        )
        buttonEnd.place(x=250, y=100, width=100, height=50)

        # Aktivierung des Fensters
        tkFenster.mainloop()

    def Restart(self, tkfenster):

        tkfenster.destroy()
        self.callBackStartWindow()

    def Quit(self, tkfenster):

        tkfenster.destroy()
