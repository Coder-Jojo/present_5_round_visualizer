import pygame 

class Lines:
    def __init__(self):
        self.surface = pygame.Surface((700, 700))
        self.surface.set_colorkey((0, 0, 0))
        self.y = [20, 170, 320, 470, 620]

        self.x = []
        for i in range(30, 30 + 40*16, 40):
            self.x.append(i)

        self.bgcolor = '#444444'
        self.color = (200, 0, 0)

    def add_line(self, x1, y1, x2, y2):
        pygame.draw.line(self.surface, self.color, (self.x[x1 // 4] + 5 + ((x1 % 4) * 7), self.y[y1]), (self.x[x1 // 4] + 5 + ((x1 % 4) * 7), self.y[y1] - 30), 3)
        pygame.draw.line(self.surface, self.color, (self.x[x2 // 4] + 5 + ((x2 % 4) * 7), self.y[y2] + 30), (self.x[x2 // 4] + 5 + ((x2 % 4) * 7), self.y[y2] + 60), 3)
        pygame.draw.line(self.surface, self.color, (self.x[x1 // 4] + 5 + ((x1 % 4) * 7), self.y[y1] - 30), (self.x[x2 // 4] + 5 + ((x2 % 4) * 7), self.y[y2] + 60), 3)
    
    def remove_line(self, x1, y1, x2, y2):
        pygame.draw.line(self.surface, self.bgcolor, (self.x[x1 // 4] + 5 + ((x1 % 4) * 7), self.y[y1]), (self.x[x1 // 4] + 5 + ((x1 % 4) * 7), self.y[y1] - 30), 3)
        pygame.draw.line(self.surface, self.bgcolor, (self.x[x2 // 4] + 5 + ((x2 % 4) * 7), self.y[y2] + 30), (self.x[x2 // 4] + 5 + ((x2 % 4) * 7), self.y[y2] + 60), 3)
        pygame.draw.line(self.surface, self.bgcolor, (self.x[x1 // 4] + 5 + ((x1 % 4) * 7), self.y[y1] - 30), (self.x[x2 // 4] + 5 + ((x2 % 4) * 7), self.y[y2] + 60), 3)