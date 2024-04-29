import pygame

pygame.font.init()

screen = pygame.display.set_mode((950, 700))
pygame.display.set_caption("The SUDOKU AI Adviser (with Backtracking!)")


x = 0
y = 0
dif = 500 / 9
val = 0
FPS = 30

#Default Board
grid = [
    [0, 0, 9, 3, 5, 0, 0, 0, 2],
    [6, 0, 2, 7, 4, 1, 5, 0, 9],
    [5, 0, 7, 2, 0, 9, 0, 6, 3],
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [2, 5, 0, 8, 0, 4, 0, 0, 0],
    [8, 0, 0, 0, 0, 5, 9, 4, 0],
    [0, 9, 0, 4, 1, 0, 0, 2, 0],
    [0, 2, 4, 9, 6, 3, 8, 0, 5],
    [0, 6, 0, 5, 7, 0, 3, 0, 0]
    ]

#Font Information
font1 = pygame.font.SysFont("arial", 40)
font2 = pygame.font.SysFont("arial", 25)

def get_cord(pos):
    global x
    x = pos[0]//dif
    global y
    y = pos[1]//dif
 

#Shows the Selected Cell 
def draw_box():
    for i in range(2):
        pygame.draw.line(screen, (45, 250, 10), (x * dif - 3, (y + i) * dif), (x * dif + dif + 3, (y + i) * dif), 7)
        pygame.draw.line(screen, (45, 250, 10), ( (x + i) * dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)   
         
#Draws the Grid Lines and fills the Colors and Numbers
def draw():
    for i in range (9):
        for j in range (9):
            if grid[i][j] != 0:
 
                pygame.draw.rect(screen, (0, 250, 250), (i * dif, j * dif, dif + 1, dif + 1))
 
                place1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
                screen.blit(place1, (i * dif + 20, j * dif + 5))

    for i in range(10):
        if i % 3 == 0:
            thick = 8
        else:
            thick = 3
        pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
        pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)      

#Inputs the Numbers done by the User
def draw_val(val):
    num1 = font1.render(str(val), 1, (0, 0, 0))
    screen.blit(num1, (x * dif + 15, y * dif + 15))    

#Error is raised if inputed value is invalid
def raise_error1():
    error1 = font1.render("INVALID", 1, (0, 0, 0))
    screen.blit(error1, (20, 550))  
def raise_error2():
    error2 = font1.render("INVALID INPUT", 1, (0, 0, 0))
    screen.blit(error2, (20, 550))  

#Validates the inputed value
def valid(m, i, j, val):
    for ii in range(9):
        if m[i][ii] == val:
            return False
        if m[ii][j] == val:
            return False
    ii = i//3
    jj = j//3
    for i in range(ii * 3, ii * 3 + 3):
        for j in range (jj * 3, jj * 3 + 3):
            if m[i][j] == val:
                return False
    return True

#Solves the Board with the help of the Backtracking Algorithm
def solve(grid, i, j):
    while grid[i][j]!= 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()    
    
    for ii in range(1, 10):
        if valid(grid, i, j, ii) == True:
            grid[i][j] = ii
            global x, y
            x = i
            y = j

            screen.fill((255, 255, 255))
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(20)
            if solve(grid, i, j) == 1:
                return True
            else:
                grid[i][j]= 0
            
            
            screen.fill((255, 255, 255))
         
            draw()
            draw_box()
            pygame.display.update()
            pygame.time.delay(45)  

    return False  

#Presents the Rules/Tips of the game
def rules():
    info1 = font2.render("TIPS:", 1, (0, 0, 0))
    info2 = font2.render("1. PRESS THE ENTER KEY TO START", 1, (0, 0, 0))
    info3 = font2.render("THE GAME", 1, (0, 0, 0))
    info4 = font2.render("2. PRESS R TO RESET, OR E TO EMPTY", 1, (0, 0, 0))
    info5 = font2.render("THE GRID", 1, (0, 0, 0))
    info6 = font2.render("3. YOU CAN USE THE ARROW KEYS", 1, (0, 0, 0))
    info7 = font2.render("OR MOUSE TO SELECT A CELL!", 1, (0, 0, 0))
    info8 = font2.render("4. ANY NUMBER YOU INSERT MUST WORK", 1, (0, 0, 0))
    info9 = font2.render("WITHIN THE RULES OF SUDOKU OR ELSE", 1, (0, 0, 0))
    info10 = font2.render("THE NUMBER WILL NOT SHOW!", 1, (0, 0, 0))
    info11 = font2.render("(NO NUMBER CAN BE IN THE SAME ROW ", 1, (0, 0, 0))
    info12 = font2.render("OR COLUMN)", 1, (0, 0, 0))
    screen.blit(info1, (680, 10))
    screen.blit(info2, (510, 35))        
    screen.blit(info3, (510, 55)) 
    screen.blit(info4, (510, 85)) 
    screen.blit(info5, (510, 105)) 
    screen.blit(info6, (510, 135))
    screen.blit(info7, (510, 155))
    screen.blit(info8, (510, 185))
    screen.blit(info9, (510, 205))
    screen.blit(info10, (510, 225))
    screen.blit(info11, (510, 255)) 
    screen.blit(info12, (510, 280)) 
 
#Shows the Final Message
def finish():
    last1 = font1.render("COMPLETION!!!", 1, (0, 0, 0))
    screen.blit(last1, (20, 520))    

run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

while run:
    screen.fill((255, 255, 255))
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False 
           
        if event.type == pygame.MOUSEBUTTONDOWN:
            flag1 = 1
            pos = pygame.mouse.get_pos()
            get_cord(pos)
           
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x -= 1
                flag1 = 1
            if event.key == pygame.K_RIGHT:
                x += 1
                flag1 = 1
            if event.key == pygame.K_UP:
                y -= 1
                flag1 = 1
            if event.key == pygame.K_DOWN:
                y += 1
                flag1 = 1   
            if event.key == pygame.K_1:
                val = 1
            if event.key == pygame.K_2:
                val = 2   
            if event.key == pygame.K_3:
                val = 3
            if event.key == pygame.K_4:
                val = 4
            if event.key == pygame.K_5:
                val = 5
            if event.key == pygame.K_6:
                val = 6
            if event.key == pygame.K_7:
                val = 7
            if event.key == pygame.K_8:
                val = 8
            if event.key == pygame.K_9:
                val = 9 
            if event.key == pygame.K_RETURN:
                flag2 = 1  
            
            if event.key == pygame.K_e:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]

            if event.key == pygame.K_r:
                rs = 0
                error = 0
                flag2 = 0
                grid = [
                [0, 0, 9, 3, 5, 0, 0, 0, 2],
                [6, 0, 2, 7, 4, 1, 5, 0, 9],
                [5, 0, 7, 2, 0, 9, 0, 6, 3],
                [0, 0, 0, 0, 0, 0, 0, 0, 8],
                [2, 5, 0, 8, 0, 4, 0, 0, 0],
                [8, 0, 0, 0, 0, 5, 9, 4, 0],
                [0, 9, 0, 4, 1, 0, 0, 2, 0],
                [0, 2, 4, 9, 6, 3, 8, 0, 5],
                [0, 6, 0, 5, 7, 0, 3, 0, 0]
                ]
                
    if flag2 == 1:
        if solve(grid, 0, 0) == False:
            error = 1
        else:
            rs = 1
        flag2 = 0 

    if val != 0:            
        draw_val(val)
        
        if valid(grid, int(x), int(y), val) == True:
            grid[int(x)][int(y)] = val
            flag1 = 0
        else:
            grid[int(x)][int(y)] = 0
            raise_error2()   
        val = 0   
       
    if error == 1:
        raise_error1()  
    if rs == 1:
        finish()        
    draw()  
    if flag1 == 1:
        draw_box()       
    rules()
        
    pygame.display.update()  

pygame.quit()     