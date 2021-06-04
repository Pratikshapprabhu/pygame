import pygame

TMR_EVE_1 = pygame.USEREVENT + 1

port = 7777
rows = 5
columns = 30
game_screen_width = 800
game_screen_height = 450
border_x = 20
border_y = 40
border_width = 760
border_height = 390
field_width = 750
field_height = 380
field_x = 25
field_y = 45
paddle_width = 15
paddle_height = 100
paddle_x = 0 #w.r.to 0 offset
paddle_y = 140 #w.r.to 0 offset
ball_radius = 8
ball_x = 180
ball_y = 190
block_width = field_width/columns
block_height = field_height/rows
