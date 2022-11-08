import pygame
pygame.init()

class Circle:
    def __init__(self,color,screen) :
        self.color = color
        self.screen = screen
        self.position_x = 223
        #position_x = 223
        self.position_y = 426
        #position_y = 426
        self.width = 30
        self.filing = 0
        self.erste_reihe(screen)
    
    def erste_reihe(self,screen):
        self.position_y -= 83
        zwischen_x= self.position_x 
        for i in range(3):
            self.position_y += 83
            self.position_x = zwischen_x
            for j in range(11):
                if self.position_y != 509 or self.position_x != 638:
                    pygame.draw.circle(screen,(255,255,255),(self.position_x,self.position_y),30,0)
                    self.position_x += 83
                else:
                    print(self.position_x)
