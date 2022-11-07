import pygame
from pygame.locals import *
import random

pygame.init()

ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

laenge = 1142
breite = 1008
screen = pygame.display.set_mode((laenge, breite))

# Würfel Klasse
#Bereich des Würfels
Wuerfelbereich = pygame.Rect(*screen.get_rect().center,0,0).inflate(100,100)

# WürfelAugenbilder mit Skalierung
dice1 = pygame.image.load("Würfel_1.png")
dice1 = pygame.transform.scale(dice1, (100,100))
dice2 = pygame.image.load("Würfel_2.png")
dice2 = pygame.transform.scale(dice2, (100,100))
dice3 = pygame.image.load("Würfel_3.png")
dice3 = pygame.transform.scale(dice3, (100,100))
dice4 = pygame.image.load("Würfel_4.png")
dice4 = pygame.transform.scale(dice4, (100,100))
dice5 = pygame.image.load("Würfel_5.png")
dice5 = pygame.transform.scale(dice5, (100,100))
dice6 = pygame.image.load("Würfel_6.png")
dice6 = pygame.transform.scale(dice6, (100,100))

# Liste der Würfelaugen
all_dice = [ None, dice1, dice2, dice3, dice4, dice5, dice6 ]
pygame.display.set_icon( dice6 )

def Wuerfelwurf():
    wurf   = random.randint( 1, 6 )
    return wurf



# Button für den Würfel
class Button:
 
    def __init__(self, text,  pos, font, bg="black", feedback=""):
        self.x, self.y = pos
        self.font = pygame.font.SysFont("Arial", font)
        if feedback == "":
            self.feedback = "text"
        else:
            self.feedback = feedback
        self.change_text(text, bg)
 
    def change_text(self, text, bg="black"):
        self.text = self.font.render(text, 1, pygame.Color("White"))
        self.size = self.text.get_size()
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg)
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
 
    def show(self):
        screen.blit(button1.surface, (self.x, self.y))
 
    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change_text(self.feedback, bg="red")
                    return True
button1 = Button(
    "Würfeln",
    (100, 100),
    font=30,
    bg="navy",
    feedback="You clicked me")


class Game:
    def runGame(self):
        wurf = 0
        wuerfelaugen = None
        laenge = 1142
        breite = 1008
        screen = pygame.display.set_mode((laenge, breite))
        
        # Position der Maus
        pos = pygame.mouse.get_pos()
        Bereich = Wuerfelbereich.collidedict(pos)

        #Hintergrund
        bg = pygame.image.load("Spielbrett.png")
        bg = pygame.transform.scale(bg,(laenge, breite))

        pygame.display.set_caption("Unser erstes Pygame-Spiel")

        gameActive = True

        # Set up timer
        clock = pygame.time.Clock()


        while gameActive:
            # Hintergrund
            screen.blit(bg,(0,0))
            # UserInteraction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameActive = False
                    print("Spieler hat Quit-Button angeklickt")   
                elif event.type == pygame.KEYDOWN:
                    print("Spieler hat Taste gedrückt")
                    


                elif event.type == pygame.MOUSEBUTTONDOWN:
                    #if button1.click(event):
                    if Bereich:
                            wurf = Wuerfelwurf()
                            wuerfelaugen = all_dice[wurf]
                            print(f"Spieler hat {wurf} gerollt")
                
            # Würfelbild und Koordinaten des Würfels
            if ( wuerfelaugen != None ):
                screen.blit( wuerfelaugen, ( 0, 0) ) 

            # Gamelogic
            button1.show()
            

            # Draw Structures and Figures
            

            # Update Display
            pygame.display.flip()

            # Setupr refreshtimer
            clock.tick(60)

        pygame.quit()


