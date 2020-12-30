import pygame
from pygame.locals import *
import sys, os
import time

# Initialize and Create Title
pygame.display.set_caption('Painter')
pygame.display.set_icon(pygame.image.load("app.png"))
pygame.init()

# Sets Window Dimensions
screen_size = (640,640)
window = pygame.display.set_mode(screen_size)
canvas = window.copy()

# Program Colors
BLACK = pygame.Color( 0 ,  0 ,  0 )
WHITE = pygame.Color(255, 255, 255)

# Track User Mouse
mouse = pygame.mouse

# Sets Background
canvas.fill(WHITE)

# Stores color of pen
cur_color = BLACK

# Program
while True:
  # Collect Mouse Values
  left_click, middle_click, right_click = mouse.get_pressed()

  # Checks User Inputs
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_x:
        canvas.fill(WHITE)
    elif left_click:
      pygame.draw.circle(canvas, cur_color, (pygame.mouse.get_pos()),5)
    elif right_click:
      if cur_color == BLACK:
        cur_color = WHITE
      else:
        cur_color = BLACK
  
  window.fill(WHITE)
  window.blit(canvas, (0, 0))
  pygame.draw.circle(window, cur_color, (pygame.mouse.get_pos()), 5)
  pygame.display.update()