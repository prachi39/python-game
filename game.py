import pygame
import time
import random
pygame.init()

crash_sound = pygame.mixer.Sound("crash.wav")

display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(255,0,0)
green=(0,200,0)
blue=(0,0,200)
bright_green=(0,255,0)
bright_red=(255,0,0)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('racing car')
clock = pygame.time.Clock()

img = pygame.image.load('racecar.png')

def block_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render('dodged:'+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def blocks(blocksx,blocksy,blocksw,blocksh,color):
    pygame.draw.rect(gameDisplay,color,[blocksx,blocksy,blocksw,blocksh])

def car(x,y):
    gameDisplay.blit(img,(x,y))

def text_objects(text,font):
    textSurf = font.render(text,True,black)
    return textSurf,textSurf.get_rect()

def crash():
  pygame.mixer.Sound.play(crash_sound)
  pygame.mixer.music.stop()
  font = pygame.font.SysFont('comicsansms',100)
  textSurf,text_rect = text_objects('You Crashed!!',font)
  text_rect.center = ((display_width/2,(display_height/2)))
  gameDisplay.blit(textSurf,text_rect)

  pygame.display.update()
  time.sleep(2)
  game_loop()

def button(text,x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    font = pygame.font.SysFont('cambria', 20)
    textSurf,text_rect = text_objects(text,font)
    text_rect.center = ((x + w / 2)), ((y + h / 2))
    gameDisplay.blit(textSurf, text_rect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def pause():
    pygame.mixer.music.pause()

    font = pygame.font.SysFont('cambria', 20)
    textSurf, text_rect = text_objects('paused', font)
    text_rect.center = ((display_width / 2)), ((display_height / 2))
    gameDisplay.blit(textSurf, text_rect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("continue",150,450,100,50,green,bright_green,unpause)
        button("continue", 150, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def start():
    start = True
    while start:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        font = pygame.font.SysFont('cambria',115)
        textSurf,text_rect = text_objects('Racing Car',font)
        text_rect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(textSurf,text_rect)

        button("GO",150,450,100,50,green,bright_green,game_loop)
        button("QUIT",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def game_loop():
 global pause

 pygame.mixer.music.load("m.wav")
 pygame.mixer.music.play(-1)

 x=(display_width*0.45)
 y=(display_height*0.8)

 x_change = 0

 block_x = random.randrange(0,display_width)
 block_y = -600
 block_speed = 7
 block_w =100
 block_h = 100

 blockcount = 1

 dodged = 0

 gameExit = False

 while not gameExit:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
          pygame.quit()
          quit()


     if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_LEFT:
             x_change = -5
         elif event.key == pygame.K_RIGHT:
             x_change = 5
     if event.type == pygame.KEYUP:
         if event.key == pygame.K_LEFT:
             x_change = 0
         elif event.key == pygame.K_RIGHT:
             x_change = 0
    x += x_change

    gameDisplay.fill(white)

    #blocks(blocksx, blocksy, blocksw, blocksh, color)
    blocks(block_x,block_y,block_w,block_h,red)
    block_y += block_speed
    car(x,y)
    block_dodged(dodged)

    if x > display_width - car_width or x <0:
       crash()

    if block_y > display_height:
        block_y = 0 - block_h
        block_x = random.randrange(0,display_width)
        dodged += 1
        block_speed += 1
        block_w += (dodged*1.2)

    if y < block_y + block_h:
        print('y crossover')
    if x > block_x and x < block_x + block_w or car_width + x < block_x and car_width + x > block_x:
        print('x crossover')
        crash()

    pygame.display.update()
    clock.tick(60)

start()
game_loop()
pygame.quit()
quit()