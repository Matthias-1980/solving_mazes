import time
from random import randint
from cells import Cell

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win = None,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = [[Cell(i,j,i+self._cell_size_x,j+self._cell_size_y,self._win) for i in range(self._num_rows)]for j in range(self._num_cols)]
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i,j)

        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        self._animate()

    # j is rows, i is columns
    def _draw_cell(self, i, j):
        (self._cells[j][i])._x1 = self._x1 + j*self._cell_size_x
        (self._cells[j][i])._y1 = self._y1 + i*self._cell_size_y
        (self._cells[j][i])._x2 = self._x1 + (j+1)*self._cell_size_x
        (self._cells[j][i])._y2 = self._y1 + (i+1)*self._cell_size_y
        if self._win is not None:
            (self._cells[j][i]).draw(self._win.canvas_widget, "blue")

    def _animate(self):
        #missing animation on 0.05 sec redraw
        # The animate method is what allows us to visualize what the algorithms 
        # are doing in real time. It should simply call the window's redraw() method, 
        # then sleep for a short amount of time so your eyes keep up with each render 
        # frame. I slept for 0.05 seconds.
        
        if self._win is not None:
            self._win.running = True
            while(self._win.running):
                time.sleep(0.05)
                self._win.redraw()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_rows - 1, self._num_cols - 1)


    #Asumptions
    #Expected behaviour:
    #Encapsulation change
    def _break_walls_r(self, i, j):
        self._cells[j][i].visited = True
        while True:
            visit = []
            if j-1 >= 0:
                if self._cells[j-1][i].visited == False: 
                    visit.append((j-1,i))
            if j+1 < self._num_cols:
                if self._cells[j+1][i].visited == False:
                    visit.append((j+1,i))
            if i-1 >= 0:
                if self._cells[j][i-1].visited == False:
                    visit.append((j,i-1))
            if i+1 < self._num_rows:
                if self._cells[j][i+1].visited == False: 
                    visit.append((j,i+1))

            if len(visit) == 0:
                if self._win is not None:
                    self._cells[j][i].draw(self._win.canvas_widget, "blue")
                return
            
            direc = visit[randint(0, len(visit) - 1)]
            if i == direc[1]:
                if j < direc[0]: 
                    #going left
                    self._cells[j][i].has_right_wall = False
                    self._cells[direc[0]][direc[1]].has_left_wall = False                                      
                elif j > direc[0]: 
                    #going right
                    self._cells[j][i].has_left_wall = False
                    self._cells[direc[0]][direc[1]].has_right_wall = False                     
                else:
                    print("case 3a")
                    return
            elif j == direc[0]:
                if i < direc[1]: 
                    #going down
                    self._cells[j][i].has_bottom_wall = False
                    self._cells[direc[0]][direc[1]].has_top_wall = False                    
                elif i > direc[1]: 
                    #going up
                    self._cells[j][i].has_top_wall = False
                    self._cells[direc[0]][direc[1]].has_bottom_wall = False                    
                else:
                    print("case 3b")
                    return
            else:
                print("case 3")
                return
                        
            self._break_walls_r(direc[1], direc[0])

    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
                        