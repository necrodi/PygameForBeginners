from tkinter import Y
import pygame
import os

#modifiable CONSTANTS
SIZE = WIDTH, HEIGHT = 900,500
BORDER_WIDTH = 10
FPS = 60
VEL = 5

#immutable CONSTANTS
BORDER_START = WIDTH/2 - BORDER_WIDTH/2
BORDER_END = WIDTH/2 + BORDER_WIDTH/2
SPACESHIP_SIZE = SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

#COLORS
BORDER_COLOR = (255, 255, 255)
BACKGROUND = (10, 10, 10)

#WINDOW Objects
BORDER = pygame.Rect(BORDER_START, 0, BORDER_WIDTH, HEIGHT)
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("First Game")

#loading Player Images
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, SPACESHIP_SIZE), 90)
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, SPACESHIP_SIZE), -90)


def draw_window(yellow, red):
    WIN.fill(BACKGROUND)
    pygame.draw.rect(WIN, BORDER_COLOR, BORDER)
    WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y))
    pygame.display.update()
    
def yellow_move(keys_pressed, rect):
    if keys_pressed[pygame.K_a]: #LEFT
        rect.x -= VEL
    if keys_pressed[pygame.K_d]: #RIGHT
        rect.x += VEL
    if keys_pressed[pygame.K_w]: #UP
        rect.y -= VEL
    if keys_pressed[pygame.K_s]: #DOWN
        rect.y += VEL

def red_move(keys_pressed, rect):
    if keys_pressed[pygame.K_LEFT]: #LEFT
        rect.x -= VEL
    if keys_pressed[pygame.K_RIGHT]: #RIGHT
        rect.x += VEL
    if keys_pressed[pygame.K_UP]: #UP
        rect.y -= VEL
    if keys_pressed[pygame.K_DOWN]: #DOWN
        rect.y += VEL
        
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    clock = pygame.time.Clock()
    
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys_pressed = pygame.key.get_pressed()
        yellow_move(keys_pressed, yellow)
        red_move(keys_pressed, red)
        
                
        draw_window(yellow, red)
    pygame.quit()

if __name__ == "__main__":
    main()