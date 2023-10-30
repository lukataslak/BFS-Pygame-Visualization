# made by tale#9706
import pygame
from pygame.locals import *
from bfsAlgoritam import *


# windows
width,height = 1920, 1080
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Level Maker')


# varables and colors
black_bg = (22,22,22)
black_sc = (38,38,38)
white = (101,101,101)
fps = 60
cubeSize = 25
rows = 32
green = (120, 192, 145)
yellow = (255, 200, 87)
red = (240, 93, 35)
green1 = (5, 130, 90)
purple = (170, 140, 230)


def grid():
    x = 75
    y = 50
    for i in range(rows):
        x += cubeSize
        y += cubeSize
        pygame.draw.line(win, white, (x, 50), (x, 849))
        pygame.draw.line(win, white, (75, y), (874, y))
        pygame.draw.rect(win, white, [75,50, 800,800],2)


def drawWindow():
    win.fill(black_bg)
    pygame.draw.rect(win, black_sc, [75,50, 800,800])
    pygame.draw.rect(win, white, [75,50, 800,800],2)
    grid()
    
    pygame.display.update()


pygame.font.init()
baseFont = pygame.font.Font(None, 32)

def main():

    drawWindow()

    # SizeButton
    inputRect = pygame.Rect(1000, 50, 100, 32)
    inputRectHide = pygame.Rect(1000, 50, 100, 32)
    userText = 'Size: '
    activeButton = False

    # Begin
    beginRect = pygame.Rect(1000, 100, 100, 32)
    activeBeginButton = False

    # End
    endRect = pygame.Rect(1000, 150, 100, 32)
    activeEndButton = False

    # Wall
    wallRect = pygame.Rect(1000, 200, 100, 32)
    activeWallButton = False

    # Erase
    eraseRect = pygame.Rect(1000, 250, 100, 32)
    activeEraseButton = False

    # RunButton
    runButtonRect = pygame.Rect(725, 875, 150, 64)
    activeRunButton = False
    activeRunColorButton = False
    pathReset = False

    # escButton
    escButtonRect = pygame.Rect(1870, 0, 50, 50)


    clock = pygame.time.Clock()
    run = True
    numFromSizeButton = 32
    while run == True:
        clock.tick(fps)


        for event in pygame.event.get():
    
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE):
                run = False


            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                # sizeSelectButton
                if inputRect.collidepoint(event.pos):
                    activeButton = True
                else:
                    activeButton = False

                # Begin Button
                if beginRect.collidepoint(event.pos):
                    activeBeginButton = True
                    activeEndButton = False
                    activeWallButton = False
                    activeEraseButton = False


                # End Button
                if endRect.collidepoint(event.pos):
                    activeBeginButton = False
                    activeEndButton = True
                    activeWallButton = False
                    activeEraseButton = False


                # Wall Button
                if wallRect.collidepoint(event.pos):
                    activeBeginButton = False
                    activeEndButton = False
                    activeWallButton = True
                    activeEraseButton = False

                # Erase Button
                if eraseRect.collidepoint(event.pos):
                    activeBeginButton = False
                    activeEndButton = False
                    activeWallButton = False
                    activeEraseButton = True

                # Run Button
                if runButtonRect.collidepoint(event.pos) and 'mapa' in locals():
                    activeRunButton = True
                    if activeRunColorButton == True: 
                        activeRunColorButton = False
                        pathReset = True
                    else:
                        activeRunColorButton = True
                
                # esc Button
                if escButtonRect.collidepoint(event.pos):
                    run = False


                #grid
                mx, my = pygame.mouse.get_pos()
                if mx <= (75 + numFromSizeButton*25) and my <= (50 + numFromSizeButton*25) and mx >= 75 and my >= 50 and 'mapa' in locals() and activeRunColorButton == False:
                    grid_num = (mx - 75)//25, (my - 50)//25
                    oneGridRect = pygame.Rect(grid_num[0]*25 + 75, grid_num[1]*25 + 50, 25, 25)
                    colors = white
                    if activeBeginButton == True: colors = green; mapa[grid_num[1]][grid_num[0]] = 'B'; pygame.draw.rect(win, colors, oneGridRect)
                    if activeEndButton == True: colors = red; mapa[grid_num[1]][grid_num[0]] = 'E'; pygame.draw.rect(win, colors, oneGridRect)
                    if activeWallButton == True: colors = yellow; mapa[grid_num[1]][grid_num[0]] = 'W'; pygame.draw.rect(win, colors, oneGridRect)
                    if activeEraseButton == True: colors = black_sc; mapa[grid_num[1]][grid_num[0]] = '_'; pygame.draw.rect(win, colors, oneGridRect)
                    
                    if activeEraseButton == True: 
                        oneGridRect = pygame.Rect(grid_num[0]*25 + 75, grid_num[1]*25 + 50, 26, 26)
                        pygame.draw.rect(win, white, oneGridRect, 1)

                    
                    pygame.draw.line(win, (255,255,255), (sizeX, 50), (sizeX, sizeY))
                    pygame.draw.line(win, (255,255,255), (75, sizeY), (sizeX, sizeY))
                    pygame.draw.line(win, (255,255,255), (75, 50), (sizeX, 50))
                    pygame.draw.line(win, (255,255,255), (75, 50), (75, sizeY))
                    
                    
        
                    # for i in range(len(mapa)):
                    #     print(mapa[i])
                    # print()
                    # print(grid_num)

            if event.type == pygame.KEYDOWN:

                # sizeSelectButton
                if activeButton == True:
                    if event.key == pygame.K_BACKSPACE:
                        if len(userText) > 6:
                            grid() 
                            userText = userText[:-1]
                    elif event.key == pygame.K_RETURN:
                        activeButton = False
                    else:
                        if len(userText) < 8:
                            grid()
                            userText += event.unicode


        # SizeButton
        pygame.draw.rect(win, black_bg, inputRectHide)
        if activeButton == True:
            pygame.draw.rect(win, white, inputRect, 2)
        else:
            pygame.draw.rect(win, (black_bg), inputRect, 2)
        textSurface = baseFont.render(userText, True, white)
        win.blit(textSurface, (inputRect.x + 5, inputRect.y + 5))
        inputRect.w = max(100, textSurface.get_width() + 10)
    

        # Begin Button
        pygame.draw.rect(win, black_bg, beginRect)
        if activeBeginButton == True:      
            pygame.draw.rect(win, green, beginRect, 2)
        else:
            pygame.draw.rect(win, black_bg, beginRect, 2)
        textSurfaceBegin = baseFont.render('Begin', True, white)
        win.blit(textSurfaceBegin, (beginRect.x + 5, beginRect.y +5 ))
        
        # End Button
        pygame.draw.rect(win, black_bg, endRect)
        if activeEndButton == True:
            pygame.draw.rect(win, red, endRect, 2)
        else:
            pygame.draw.rect(win, black_bg, endRect, 2)
        textSurfaceEnd = baseFont.render('End', True, white)
        win.blit(textSurfaceEnd, (endRect.x + 5, endRect.y + 5))

        # Wall Button
        pygame.draw.rect(win, black_bg, wallRect)
        if activeWallButton == True:
            pygame.draw.rect(win, yellow, wallRect, 2)
        else:
            pygame.draw.rect(win, black_bg, wallRect, 2)
        textSurfaceWall = baseFont.render('Wall', True, white)
        win.blit(textSurfaceWall, (wallRect.x + 5, wallRect.y + 5))

        # Erase Button
        pygame.draw.rect(win, black_bg, eraseRect)
        if activeEraseButton == True:
            pygame.draw.rect(win, white, eraseRect, 2)
        else:
            pygame.draw.rect(win, black_bg, eraseRect, 2)
        textSurfaceErase = baseFont.render('Erase', True, white)
        win.blit(textSurfaceErase, (eraseRect.x + 5, eraseRect.y + 5))


        # Run Button
        pygame.draw.rect(win, green1, runButtonRect)

        
        if activeRunColorButton == True:
            pygame.draw.rect(win, green, runButtonRect, 5)
            textSurfaceRun = baseFont.render('Run', True, green)
        else:
            pygame.draw.rect(win, green1, runButtonRect, 5)
            textSurfaceRun = baseFont.render('Run', True, black_bg)
        win.blit(textSurfaceRun, (runButtonRect.x + 53, runButtonRect.y + 20))

        # escButton
        pygame.draw.rect(win, black_sc, escButtonRect)
        pygame.draw.line(win, white, (1880, 10), (1910, 40), 3)
        pygame.draw.line(win, white, (1910, 10), (1880, 40), 3)

        # run bfs
        if 'mapa' in locals() and activeRunButton == True:
            path = reconstructPath(mapa, bfs(mapa))
            path.pop()
            path.pop(0)
            while path:
                grid_num = path.pop()
                oneGridRect = pygame.Rect(grid_num[1]*25 + 75, grid_num[0]*25 + 50, 26, 26)
                pygame.draw.rect(win, purple, oneGridRect)


                pygame.draw.line(win, (255,255,255), (sizeX, 50), (sizeX, sizeY))
                pygame.draw.line(win, (255,255,255), (75, sizeY), (sizeX, sizeY))
                pygame.draw.line(win, (255,255,255), (75, 50), (sizeX, 50))
                pygame.draw.line(win, (255,255,255), (75, 50), (75, sizeY))
            activeRunButton = False

        if pathReset == True:
            path = reconstructPath(mapa, bfs(mapa))
            path.pop()
            path.pop(0)
            while path:
                grid_num = path.pop()
                oneGridRect = pygame.Rect(grid_num[1]*25 + 75, grid_num[0]*25 + 50, 26, 26)
                
                pygame.draw.rect(win, black_sc, oneGridRect)
                pygame.draw.rect(win, white, oneGridRect,1)

                pygame.draw.line(win, (255,255,255), (sizeX, 50), (sizeX, sizeY))
                pygame.draw.line(win, (255,255,255), (75, sizeY), (sizeX, sizeY))
                pygame.draw.line(win, (255,255,255), (75, 50), (sizeX, 50))
                pygame.draw.line(win, (255,255,255), (75, 50), (75, sizeY))
            pathReset = False
            
            
        
        if userText[6:].isnumeric() and (int(userText[6:]) != numFromSizeButton):
            numFromSizeButton = int(userText[6:])
            if numFromSizeButton < 33:
                sizeX = 75 + numFromSizeButton*cubeSize
                sizeY = 50 + numFromSizeButton*cubeSize

                pygame.draw.rect(win, black_sc, [75,50, 800,800])
                pygame.draw.rect(win, white, [75,50, 800,800],2)
                grid()
                pygame.display.update()
                activeRunColorButton = False

                pygame.draw.line(win, (255,255,255), (sizeX, 50), (sizeX, sizeY))
                pygame.draw.line(win, (255,255,255), (75, sizeY), (sizeX, sizeY))
                pygame.draw.line(win, (255,255,255), (75, 50), (sizeX, 50))
                pygame.draw.line(win, (255,255,255), (75, 50), (75, sizeY))
        
                
                mapa = []
                for i in range(numFromSizeButton):
                    k = []
                    for j in range(numFromSizeButton):
                        k.append('_')
                    mapa.append(k)

        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()
