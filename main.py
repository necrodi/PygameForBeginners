from tkinter import Y
import pygame
import os

from refference import RED, SPACESHIP_HEIGHT, SPACESHIP_WIDTH

SIZE = [900,500]
WIN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("First Game")

WHITE = (255,255,255)
BACKGROUND = (10, 10, 10)

FPS = 60
VEL = 5

SPACESHIP_SIZE = SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))

YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, SPACESHIP_SIZE), 90)
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, SPACESHIP_SIZE), -90)

def draw_window(yellow, red):
    WIN.fill(BACKGROUND)
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