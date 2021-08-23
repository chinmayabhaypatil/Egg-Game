import pygame
import random
pygame.init()

black=(0,0,0)
white=(255,255,255)
red=(180,0,0)
green=(0,180,0)
bright_red=(255,0,0)
bright_green=(0,255,0)

width=1100
height=650

gameDisplay=pygame.display.set_mode((width,height))
pygame.display.set_caption('An egg game')
clock=pygame.time.Clock()

basImg=pygame.image.load('basket.png')
(bas_width,bas_height)=basImg.get_rect().size

eggImg=pygame.image.load('egg.png')
(egg_width,egg_height)=basImg.get_rect().size

def bas(x,y):
    gameDisplay.blit(basImg,(x,y))
def egg(x1,y1,egg_height,egg_width):    
    gameDisplay.blit(eggImg,(x1,y1))

def unpause():
    global pause
    pause=False

def crash():
    crash1=True
    while crash1:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        text=pygame.font.Font('freesansbold.ttf',115)
        textSurface=text.render('YOU CRASHED',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((width/2),(height/2))
        gameDisplay.blit(textSurface,textRectangle)
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 350<mouse[0]<350+150 and 500<mouse[1]<500+50:
            pygame.draw.rect(gameDisplay,bright_green,(350,500,150,50))
            if click[0]==1:
                game_loop()
        else:
            pygame.draw.rect(gameDisplay,green,(350,500,150,50))

        text=pygame.font.Font('freesansbold.ttf',20)
        textSurface=text.render('PLAY AGAIN',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((350+(150/2)),(500+(50/2)))
        gameDisplay.blit(textSurface,textRectangle)

        if 550<mouse[0]<550+150 and 500<mouse[1]<500+50:
            pygame.draw.rect(gameDisplay,bright_red,(550,500,150,50))
            if click[0]==1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay,red,(550,500,150,50))

        text=pygame.font.Font('freesansbold.ttf',20)
        textSurface=text.render('QUIT',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((550+(150/2)),(500+(50/2)))
        gameDisplay.blit(textSurface,textRectangle)      

        pygame.display.update()



def game_over(point):
    over=True
    while over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        text=pygame.font.Font('freesansbold.ttf',115)
        textSurface=text.render('GAME OVER',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((width/2),(height/2))
        gameDisplay.blit(textSurface,textRectangle)
        
        text=pygame.font.Font('freesansbold.ttf',50)
        textSurface=text.render('YOUR SCORE: '+str(point),True,black)
        gameDisplay.blit(textSurface,(350,425))
        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 350<mouse[0]<350+150 and 500<mouse[1]<500+50:
            pygame.draw.rect(gameDisplay,bright_green,(350,500,150,50))
            if click[0]==1:
                game_loop()
        else:
            pygame.draw.rect(gameDisplay,green,(350,500,150,50))

        text=pygame.font.Font('freesansbold.ttf',20)
        textSurface=text.render('PLAY AGAIN',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((350+(150/2)),(500+(50/2)))
        gameDisplay.blit(textSurface,textRectangle)

        if 550<mouse[0]<550+150 and 500<mouse[1]<500+50:
            pygame.draw.rect(gameDisplay,bright_red,(550,500,150,50))
            if click[0]==1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay,red,(550,500,150,50))

        text=pygame.font.Font('freesansbold.ttf',20)
        textSurface=text.render('QUIT',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((550+(150/2)),(500+(50/2)))
        gameDisplay.blit(textSurface,textRectangle)      

        pygame.display.update()


def paused():
    global pause
    pause=True
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #gameDisplay.fill(white)
        text=pygame.font.Font('freesansbold.ttf',115)
        textSurface=text.render('PAUSED',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((width/2),(height/2))
        gameDisplay.blit(textSurface,textRectangle)


        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 350<mouse[0]<350+150 and 500<mouse[1]<500+50:
            pygame.draw.rect(gameDisplay,bright_green,(350,500,150,50))
            if click[0]==1:
                unpause()
        else:
            pygame.draw.rect(gameDisplay,green,(350,500,150,50))

        text=pygame.font.Font('freesansbold.ttf',20)
        textSurface=text.render('CONTINUE',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((350+(150/2)),(500+(50/2)))
        gameDisplay.blit(textSurface,textRectangle)

        if 550<mouse[0]<550+200 and 500<mouse[1]<500+50:
            pygame.draw.rect(gameDisplay,bright_red,(550,500,150,50))
            if click[0]==1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay,red,(550,500,150,50))

        text=pygame.font.Font('freesansbold.ttf',20)
        textSurface=text.render('QUIT',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((550+(150/2)),(500+(50/2)))
        gameDisplay.blit(textSurface,textRectangle)      

        pygame.display.update()    

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)

        basImg=pygame.image.load('basket.png')
        gameDisplay.blit(basImg,(500,150))

        eggImg=pygame.image.load('egg.png')
        gameDisplay.blit(eggImg,(540,70))

        text=pygame.font.Font('freesansbold.ttf',115)
        textSurface=text.render('EGG GAME',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((width/2),(height/2))
        gameDisplay.blit(textSurface,textRectangle)

        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        
        if 350<mouse[0]<350+100 and 500<mouse[1]<500+50:
            pygame.draw.rect(gameDisplay,bright_green,(350,500,100,50))
            if click[0]==1:
                game_loop()
        else:
            pygame.draw.rect(gameDisplay,green,(350,500,100,50))

        text=pygame.font.Font('freesansbold.ttf',20)
        textSurface=text.render('START',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((350+(100/2)),(500+(50/2)))
        gameDisplay.blit(textSurface,textRectangle)

        if 550<mouse[0]<550+100 and 500<mouse[1]<500+50:
            pygame.draw.rect(gameDisplay,bright_red,(550,500,100,50))
            if click[0]==1:
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(gameDisplay,red,(550,500,100,50))

        text=pygame.font.Font('freesansbold.ttf',20)
        textSurface=text.render('QUIT',True,black)
        textRectangle=textSurface.get_rect()
        textRectangle.center=((550+(100/2)),(500+(50/2)))
        gameDisplay.blit(textSurface,textRectangle)      

        pygame.display.update()

def eggs_left(count,point):

    text=pygame.font.Font('freesansbold.ttf',20)
    textSurface=text.render('EGGS LEFT: '+str(count),True,black)
    gameDisplay.blit(textSurface,(900,0))
    if count==0:
        game_over(point)

def points(point):
    text=pygame.font.Font('freesansbold.ttf',20)
    textSurface=text.render('POINTS: '+str(point),True,black)
    gameDisplay.blit(textSurface,(20,0))
    
    
def game_loop():    
    x=(width*0.45)
    y=(height*0.8)
    x_change=0
    x1=random.randrange(20,1000)
    y1=-600
    egg_speed=7
    point=0
    count=10
    
    crashed=False

    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x_change+=-7
                if event.key==pygame.K_RIGHT:
                    x_change+=7
                if event.key==pygame.K_p:
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    x_change+=7
                if event.key==pygame.K_RIGHT:    
                    x_change+=-7

        x+=x_change

        gameDisplay.fill(white)
        bas(x,y)
        egg(x1,y1,egg_height,egg_width)
        y1+=egg_speed
        eggs_left(count,point)
        points(point)
        if x>width-bas_width or x<0:
            crashed=True
            crash()        
        if y1>height:
            y1=0-110
            x1=random.randrange(20,1000)
            count-=1
        if y1==y:
            if x1>x and x1<x+bas_width:
                point+=10
        pygame.display.update()
game_intro()
game_loop()    
pygame.quit()
quit()
