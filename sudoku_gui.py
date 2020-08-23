import pygame
import numpy as np;
import sys

board=[
   [0,7,3,0,9,0,0,0,6],
   [0,0,0,0,2,0,0,4,0],
   [0,2,0,0,0,5,0,7,0],
   [0,0,0,6,8,0,0,1,0],
   [5,6,0,0,0,0,0,2,0],
   [0,0,0,0,0,4,6,0,0],
   [2,0,9,0,0,0,7,0,0],
   [7,0,0,1,0,0,0,0,8],
   [6,0,0,4,0,0,0,0,0]
  ];

fps = 10
window_w = 360
window_h = 360
gray=(185,185,185);
black=(0,0,0);






def find_empty(board):

  for i in range(len(board)):
    for j in range(len(board)):

      if(board[i][j]==0):
        return (i,j);

  return (-1,-1);






def validity(board, num, position):
    r, c = position;

    # row
    for j in range(len(board)):
        if board[r][j] == num:
            return False;

    # column
    for i in range(len(board)):
        if board[i][c] == num:
            return False;

    # sub grid
    grid_size = int(np.sqrt(len(board)));
    grid_x = (r // grid_size);
    grid_y = (c // grid_size);

    for i in range(grid_size * grid_x, grid_size * grid_x + grid_size):
        for j in range(grid_size * grid_y, grid_size * grid_y + grid_size):
            if board[i][j] == num:
                return False;

    return True;






def backtrack(board):
    r, c = find_empty(board);

    if (r == -1 and c == -1):
        return True;

    for i in range(1, 10):

        if validity(board, i, (r, c)):
            board[r][c] = i;

            if backtrack(board):
                return True;
            else:
                board[r][c] = 0

    return False;








def create_grid():

    innergrid_h=int(window_h/9);
    innergrid_w=int(window_w/9);

    for i in range(9):
        y= i*innergrid_h;
        x= i*innergrid_w;

        if int(i%3)==0:
            pygame.draw.line(sudoku,black, (0,y) ,(window_w,y) ) ;
            pygame.draw.line(sudoku,black, (x,0) , (x,window_h)  );

        else:
            pygame.draw.line(sudoku, gray, (0, y), (window_w, y));
            pygame.draw.line(sudoku, gray, (x, 0), (x, window_h));





def puzzle():
    font = pygame.font.SysFont('comicsansms', 28);

    for i in range(9):
        y = 40 * i + 10;
        for j in range(9):
            x = 40 * j + 20;
            if board[i][j]!=0:


                value=board[i][j];


                text = font.render(str(value), True, (0, 0, 0));
                sudoku.blit(text, (x, y) );




def find_grid(x,y):
    x_right=x;
    y_right=y;

    x_left=x;
    y_left=y;

    loop=True;

    while loop:
        if x_right%40 == 0 :
            loop=False;
        else:
            x_right=x_right+1;

    loop=True;

    while loop:
        if y_right%40 == 0 :
            loop=False;
        else:
            y_right=y_right + 1 ;

    loop = True;

    while loop:
        if y_left%40 == 0 :
            loop=False;
        else:
            y_left=y_left - 1 ;

    loop = True;

    while loop:
        if x_left%40 == 0 :
            loop=False;
        else:
            x_left=x_left - 1 ;

    return (  x_left,  y_left ) , (x_right , y_right);






def main():
    global clock, sudoku
    pygame.init()
    clock = pygame.time.Clock()
    sudoku = pygame.display.set_mode((window_w,window_h))
    pygame.display.set_caption('Sudoku Solver')

    sudoku.fill((173,216,230))
    create_grid();

    running =True;
    puzzle();               #print initial values


    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False

            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_SPACE:

                    if not backtrack(board):

                        sudoku.fill((0,0,0));
                        font = pygame.font.SysFont('comicsansms', 28);
                        text = font.render('INVALID PUZZLE!', True, (0, 255, 0));
                        sudoku.blit(text, (window_w//3.5, window_h//2.5));

                    else:
                        puzzle();




        pygame.display.update()
        clock.tick(fps)

main();
pygame.quit();
