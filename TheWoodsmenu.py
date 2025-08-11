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