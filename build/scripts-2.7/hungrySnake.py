import pygame,sys,random,time
from pygame.locals import *


WHITE     = (255, 255, 255)
BLACK     = (0, 0, 0)
CYAN      = (40, 137, 200)
RED       = (185, 0, 0)
GREEN     = (0, 255, 0)
DARKGREEN = (0, 155, 0)
DARKGRAY  = (40, 40, 40)
GRAY      = (70, 70, 70)
COLOR1    = (151, 20, 192)
COLOR2    = (19, 166, 131)
LEVEL = 1
FPS = 15
WIN_WIDTH  = 640
WIN_HEIGHT = 600
CELLSIZE = 20
CELLWIDTH = int(WIN_WIDTH/CELLSIZE)
CELLHEIGHT = int(WIN_HEIGHT/CELLSIZE)
LastScore = 0


#direction
UP    = 'up'
DOWN  = 'down'
LEFT  = 'left'
RIGHT = 'right'

# Driver for Program
def driver():
    global DISPLAY,FPSCLOCK,FONT,FPS,LEVEL,LastScore
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAY  = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    
    FONT     = pygame.font.SysFont('freesansbold.ttf', 24)
    pygame.display.set_caption('Hungry Snake') 
    
    while True:
        pygame.mixer.music.load('game.mid')
        pygame.mixer.music.play(-1)
        StartScreen()
        FPS = 15
        LEVEL = 1        
        LastScore = 0
        difficulty()
        DISPLAY.fill(BLACK)
        levelScreen()      
        game()
        gameOver()


def difficulty():
        global FPS
        DISPLAY.fill(BLACK)
        temp_font  = pygame.font.SysFont('freesansbold.ttf',80)
        temp_title = temp_font.render('Hungry Snake',True,COLOR2,BLACK)
        temp_font = pygame.font.SysFont('freesansbold.ttf',60)
        Surf1 = temp_font.render('EASY', True, COLOR1)
        Surf2 = temp_font.render('DIFFICULT', True, COLOR1)
        Surf3 = temp_font.render('HARD', True, COLOR1)
        titleRect = temp_title.get_rect()
        surf1Rect = Surf1.get_rect()
        surf2Rect = Surf2.get_rect()
        surf3Rect = Surf3.get_rect()
        titleRect.midtop = (WIN_WIDTH / 2, 20)
        surf1Rect.midtop = (WIN_WIDTH / 2, 180)
        surf2Rect.midtop = (WIN_WIDTH / 2, surf1Rect.height + 200)
        surf3Rect.midtop = (WIN_WIDTH / 2, surf2Rect.height + 262)


        DISPLAY.blit(temp_title, titleRect)
        DISPLAY.blit(Surf1, surf1Rect)
        DISPLAY.blit(Surf2, surf2Rect)
        DISPLAY.blit(Surf3, surf3Rect)
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONUP:
                    if surf1Rect.collidepoint(event.pos):
                        FPS = 15
                        return
                    elif surf2Rect.collidepoint(event.pos):
                        FPS = 20
                        return
                    elif surf3Rect.collidepoint(event.pos):
                        FPS = 25
                        return
            if len(pygame.event.get(QUIT)) > 0:   #list of  quit keys
                     Exit()

              
        
def levelScreen():
        temp_font = pygame.font.SysFont('freesansbold.ttf', 70)
        levelSurf = temp_font.render('LEVEL: %d' % LEVEL, True, WHITE)
        levelRect = levelSurf.get_rect()
        levelRect.center = (320, 200)
        DISPLAY.blit(levelSurf, levelRect)
        temp_font = pygame.font.SysFont('freesansbold.ttf', 80)
        scoreSurf = temp_font.render('Score: %s' % LastScore, True, GRAY)
        scoreRect = scoreSurf.get_rect()
        scoreRect.center = (320, 420)
        DISPLAY.blit(scoreSurf, scoreRect)
        temp_surf_font= FONT.render('PRESS SPACEBAR TO RESUME',True,RED)
        temp_surf   = temp_surf_font.get_rect()
        temp_surf.center = (WIN_WIDTH -150,WIN_HEIGHT -30)
        DISPLAY.blit(temp_surf_font , temp_surf)
        pygame.display.update()

        while True: 
            if checkEnter():
                    return

def checkEnter2():
        if len(pygame.event.get(QUIT)) > 0:   #list of  quit keys
             Exit()

        checkKey = pygame.event.get(KEYDOWN)
        if len(checkKey) == 0 :
            return 0
        elif checkKey[0].key == K_ESCAPE:
             Exit()
        elif checkKey[0].key == K_RETURN:
             return 1


def gameOver():
        DISPLAY.fill(BLACK)
        drawFinalScore(LastScore)
        while True:
            temp_font = pygame.font.SysFont('freesansbold.ttf', 140)
            temp_c = (random.randint(1, 255),random.randint(1,255),random.randint(1, 255))
            temp_c1 = (random.randint(1, 255),random.randint(1,255),random.randint(1, 255))
            gameSurf = temp_font.render('Game', True, temp_c)
            overSurf = temp_font.render('Over', True, temp_c1)
            gameRect = gameSurf.get_rect()
            overRect = overSurf.get_rect()
            gameRect.midtop = (WIN_WIDTH / 2, 60)
            overRect.midtop = (WIN_WIDTH / 2, gameRect.height + 60)

            DISPLAY.blit(gameSurf, gameRect)
            DISPLAY.blit(overSurf, overRect)

            temp_surf_font= FONT.render('PRESS ENTER TO PLAY AGAIN',True,RED)
            temp_surf   = temp_surf_font.get_rect()
            temp_surf.center = (WIN_WIDTH -150,WIN_HEIGHT -30)
            DISPLAY.blit(temp_surf_font , temp_surf)
            pygame.display.update()
        
               
            if checkEnter2():
                       return
   

def checkEnter():
        if len(pygame.event.get(QUIT)) > 0:   #list of  quit keys
             Exit()

        checkKey = pygame.event.get(KEYDOWN)
        if len(checkKey) == 0 :
            return 0
        elif checkKey[0].key == K_ESCAPE:
             Exit()
        elif checkKey[0].key in (K_RETURN,K_SPACE):
             return 1
        
    

def drawFinalScore(score):
        temp_font = pygame.font.SysFont('freesansbold.ttf', 90)
        scoreSurf = temp_font.render('Score: %s' % (score), True, GRAY)
        scoreRect = scoreSurf.get_rect()
        scoreRect.center = (320, 420)
        DISPLAY.blit(scoreSurf, scoreRect)


  
def getRandomLocation():
        return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


    
def game():
        global LastScore,LEVEL
        DISPLAY.fill(BLACK)

        temp_surf_font1= FONT.render('PAUSE',True,WHITE)
        temp_surf1   = temp_surf_font1.get_rect()
        temp_surf1.topleft = (WIN_WIDTH -120,35)
        Food = getRandomLocation()
        startx = random.randint(5, CELLWIDTH - 6)
        starty = random.randint(5, CELLHEIGHT - 6)
        snakepos = [{'x': startx, 'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
        
        
        
        direction = RIGHT

        while True:
            flag = 0;
            for event in pygame.event.get(): 
                if event.type == QUIT:
                    terminate()
                elif event.type == MOUSEBUTTONUP:
                    if temp_surf1.collidepoint(event.pos):
                        levelScreen()
                elif event.type == KEYDOWN:
                    if (event.key == K_LEFT) and direction != RIGHT:
                        direction = LEFT
                    elif (event.key == K_RIGHT) and direction != LEFT:
                        direction = RIGHT
                    elif (event.key == K_UP) and direction != DOWN:
                        direction = UP
                    elif (event.key == K_DOWN ) and direction != UP:
                        direction = DOWN
                    elif event.key == K_ESCAPE:
                        flag = 1
                    elif  event.key == K_SPACE :
                        levelScreen()

            
            
            if snakepos[0]['x'] in (-1,CELLWIDTH) or snakepos[0]['y'] in (-1,CELLHEIGHT):
                        flag = 1
            
            for snakeBody in snakepos[1:]:
                if snakeBody['x'] == snakepos[0]['x'] and snakeBody['y'] == snakepos[0]['y']:
                        flag = 1
                        break

            if flag == 1:
                pygame.mixer.music.load('death.mid')
                pygame.mixer.music.play()
                
                return
            
            if snakepos[0]['x'] == Food['x'] and snakepos[0]['y'] == Food['y']:
                soundObj = pygame.mixer.Sound('hit.wav')
                soundObj.play()
                time.sleep(.01)
    
                Food = getRandomLocation()           
            else:
                del snakepos[-1] 

            global FPS
            if direction == UP:
                newHead = {'x': snakepos[0]['x'],     'y': snakepos[0]['y'] - 1}
            elif direction == DOWN:
                newHead = {'x': snakepos[0]['x'],     'y': snakepos[0]['y'] + 1}
            elif direction == LEFT:
                newHead = {'x': snakepos[0]['x'] - 1, 'y': snakepos[0]['y']}
            elif direction == RIGHT:
                newHead = {'x': snakepos[0]['x'] + 1, 'y': snakepos[0]['y']}
                
                
            snakepos.insert(0, newHead)
            DISPLAY.fill(BLACK)           
            drawGrid()
            
            DISPLAY.blit(temp_surf_font1 , temp_surf1)
            drawSnake(snakepos)
            drawFood(Food)
                    
            drawScore(len(snakepos) - 3)
            if LastScore != (len(snakepos) - 3):
                LastScore = len(snakepos) - 3
                if LastScore % 10 == 0:
                    FPS += 5
                    LEVEL+=1
                    levelScreen()
            
            pygame.display.update()
            FPSCLOCK.tick(FPS)
      


def drawScore(score):
            scoreSurf = FONT.render('Score: %s' % (score), True, WHITE)
            scoreRect = scoreSurf.get_rect()
            scoreRect.topleft = (WIN_WIDTH - 120, 10)
            DISPLAY.blit(scoreSurf, scoreRect)


def drawSnake(snakepos):
            for coord in snakepos:
                x = coord['x'] * CELLSIZE
                y = coord['y'] * CELLSIZE
                pygame.draw.circle(DISPLAY, DARKGREEN, (x+10,y+10), CELLSIZE/2 + 3, 0)
                SnakeInnerRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
                pygame.draw.rect(DISPLAY, GREEN, SnakeInnerRect)
    

def drawFood(pos):
            x = pos['x'] * CELLSIZE
            y = pos['y'] * CELLSIZE
            pygame.draw.circle(DISPLAY, (random.randint(1, 255),random.randint(1,255),random.randint(1, 255)), (x+10,y+10), CELLSIZE/2 + 2, 0)
            

def drawGrid():
            for x in range(0, WIN_WIDTH, CELLSIZE):
                pygame.draw.line(DISPLAY, DARKGRAY, (x, 0), (x, WIN_HEIGHT))
            for y in range(0, WIN_HEIGHT, CELLSIZE): 
                pygame.draw.line(DISPLAY, DARKGRAY, (0, y), (WIN_WIDTH, y))



def StartScreen():
            Img = pygame.image.load('snake1.png')
            temp_font  = pygame.font.SysFont('freesansbold.ttf',110)
            temp_title1 = temp_font.render('Hungry Snake',True,COLOR2,(15,14,13))
            temp_title2 = temp_font.render('Hungry Snake',True,COLOR1)
            temp_surf_font= FONT.render('PRESS A KEY TO PLAY',True,RED)
            temp_surf   = temp_surf_font.get_rect()
            temp_surf.center = (WIN_WIDTH -110,WIN_HEIGHT -30)
            temp_font1  = pygame.font.SysFont('freesansbold.ttf',35)
            temp_surf_font1= FONT.render('ABOUT',True,RED)
            temp_surf1   = temp_surf_font1.get_rect()
            temp_surf1.center = (50,570)
            angle1 = 0
            angle2 = 10
            
            while True:
                DISPLAY.fill(BLACK)
                #DISPLAY.blit(Img,(70,50))
                rotated_surf1 = pygame.transform.rotate(temp_title1,angle1)
                rotated_rec1  = rotated_surf1.get_rect()
                rotated_rec1.center = (WIN_WIDTH/2, WIN_HEIGHT/2)
                
                
                rotated_surf2 = pygame.transform.rotate(temp_title2,angle2)
                rotated_rec2  = rotated_surf2.get_rect()
                rotated_rec2.center = (WIN_WIDTH/2, WIN_HEIGHT/2)
                
                DISPLAY.blit(rotated_surf1,rotated_rec1)
                DISPLAY.blit(rotated_surf2,rotated_rec2)
                DISPLAY.blit(temp_surf_font1,temp_surf1)
                DISPLAY.blit(temp_surf_font,temp_surf)
                pygame.display.update()
                FPSCLOCK.tick(FPS)
                        
                angle1 += 3
                angle2 += 5
                
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONUP:
                        if temp_surf1.collidepoint(event.pos):
                            about()
                    elif event.type == QUIT:  
                            Exit()
                    elif event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                 Exit()                           
                            return
                
def printString(string,x,y):
    font1       = pygame.font.SysFont('freesansbold.ttf',21)
    temp_font   = font1.render(string,True,GREEN)
    temp1       = temp_font.get_rect()
    temp1.topleft = (x,y)                       
    DISPLAY.blit(temp_font,temp1)
    
def about():
    Img1 = pygame.image.load('snake1.png')
    Img2 = pygame.image.load('Creator1.jpg')
    DISPLAY.fill(BLACK)        
    DISPLAY.blit(Img1,(8,20))
    DISPLAY.blit(Img2,(450,370))
    font1       = pygame.font.SysFont('freesansbold.ttf',35)
    temp_font   = font1.render('GamePlay',True,RED)
    temp1       = temp_font.get_rect()
    temp1.center = (420,24)                       
    DISPLAY.blit(temp_font,temp1)

    printString('A sole player attempts to eat apple by running into them',220,50)
    printString('with the  head of  the snake. Each apple eaten makes the ',220,76)
    printString('snakelonger and also increases running speed of snake,',220,102)
    printString('so  maneuvering is  progressively  more  difficult. Player',220,128)
    printString('controls  a  square  on a bordered plane. As  it  moves',220,154)
    printString('forward, it leaves trail behind, resembling moving snake.',220,180)

    font1       = pygame.font.SysFont('freesansbold.ttf',35)
    temp_font   = font1.render('Developer',True,RED)
    temp1       = temp_font.get_rect()
    temp1.center = (200,370)                       
    DISPLAY.blit(temp_font,temp1)

    printString('NAME             :   Peeyush yadav ',25,400)
    printString('CONNECT     :   in.linkedin.com/in/peeyushy95/en ',25,452)
    printString('CONTECT     :   peeyushy95@gmail.com ',25,426)
    printString('FACEBOOK   :   www.facebook.com/thegreatpeeyush ',25,478)
    pygame.display.update()
        
    while True:   
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    return
                elif event.type == QUIT:  
                            Exit()

def checkEvent():
            if len(pygame.event.get(QUIT)) > 0:   #list of  quit keys
                 Exit()

            checkKey = pygame.event.get(KEYUP)
            if len(checkKey) == 0 :
                return 0
            elif checkKey[0].key == K_ESCAPE:
                 Exit()
            else:
                return 1

def Exit():
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
            driver()
