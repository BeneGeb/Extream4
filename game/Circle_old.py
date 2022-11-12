import pygame

pygame.init()


class Circle_old:
    def __init__(self, color, color_2, screen):
        self.color = color
        self.color_2 = color_2
        self.screen = screen
        self.position_x = 223
        self.position_x2 = 555
        self.position_y = 426
        self.position_y2 = 94
        self.position_x_rot = 223
        self.position_y_rot = 85
        self.erste_reihe(screen)
        self.y_reihe(screen)
        self.rote_kreise(screen, color_2)
        # self.gelbe_kreise(screen,color_2,self.position_x_rot,self.position_y_rot)

    def erste_reihe(self, screen):
        self.position_y -= 83
        zwischen_x = self.position_x
        for i in range(3):
            self.position_y += 83
            self.position_x = zwischen_x
            for j in range(11):
                if self.position_y != 509 or self.position_x != 638:
                    pygame.draw.circle(
                        screen,
                        (255, 255, 255),
                        (self.position_x, self.position_y),
                        30,
                        0,
                    )
                self.position_x += 83

    def y_reihe(self, screen):
        self.position_x2 -= 83
        zwischen_y = self.position_y2
        for i in range(3):
            self.position_x2 += 83
            self.position_y2 = zwischen_y
            for j in range(11):
                if self.position_y2 != 509 or self.position_x2 != 638:
                    pygame.draw.circle(
                        screen,
                        (255, 255, 255),
                        (self.position_x2, self.position_y2),
                        30,
                        0,
                    )
                self.position_y2 += 83

    def rote_kreise(self, screen, color_2):
        zwischen_y_rot = self.position_y_rot
        self.position_y_rot -= 90
        zwischen_x_rot = self.position_x_rot
        for i in range(2):
            self.position_y_rot += 90
            self.position_x_rot = zwischen_x_rot
            for j in range(2):
                pygame.draw.circle(
                    screen, color_2, (self.position_x_rot, self.position_y_rot), 30, 0
                )
                self.position_x_rot += 90

        Circle.gelbe_kreise(self, screen, color_2, zwischen_x_rot, zwischen_y_rot)

    def gelbe_kreise(self, screen, color_2, pos_x, pos_y):
        pos_x += 740
        pos_y -= 90
        zwischen_x = pos_x
        for i in range(2):
            pos_y += 90
            pos_x = zwischen_x
            for j in range(2):
                pygame.draw.circle(screen, color_2, (pos_x, pos_y), 30, 0)
                pos_x += 90
