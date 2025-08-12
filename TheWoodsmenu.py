import os
import pygame

# Clear terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Initialize Pygame
pygame.init()

# Set up screen
win = pygame.display.set_mode((640, 480), pygame.RESIZABLE)
pygame.display.set_caption("The Woods")

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Font and
font = pygame.font.SysFont('Courier New', 24)

# Create text surface
woods = font.render("The Woods", True, RED)
# Center the text
text_rect = woods.get_rect()
text_rect.center = win.get_rect().center
#Rusable Button function
class Button:
    def __init__(self, x, y, width, height, text, font, base_color, hover_color, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = font.render(text, True, text_color)
        self.base_color = base_color
        self.hover_color = hover_color
        self.text_pos = (
            x + (width - self.text.get_width()) // 2,
            y + (height - self.text.get_height()) // 2
        )

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.base_color
        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.text, self.text_pos)

    def is_clicked(self):
        return self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]
    
# Create a button instance

# Main loop
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.VIDEORESIZE:
            win = pygame.display.set_mode(event.size, pygame.RESIZABLE)
            

#Game Loop start here v
    win.fill(BLACK)
    
    text_rect = woods.get_rect(center=win.get_rect().center)
    win.blit(woods, text_rect)

    
    #--------------------------------------------------------------------------------------------------------------
    pygame.display.flip()
    clock.tick(60)
pygame.quit()