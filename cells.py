#Assumptions:
#Expected behaviour:
#Encapsulation change:
class Cell():
    def __init__(self, x1, y1, x2, y2, 
                 win = None,
                 left_w = True, 
                 top_w = True, 
                 right_w = True,                  
                 bottom_w = True):
        self.has_left_wall = left_w
        self.has_top_wall = top_w
        self.has_right_wall = right_w
        self.has_bottom_wall = bottom_w
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        
        self.visited = False

    def draw_move(self, to_cell, undo=False):
        diff = abs(self._x1 - self._x2) / 2
        new_self_x = 0
        if self._x1 < self._x2:
            new_self_x = self._x1 + diff
        else:
            new_self_x = self._x2 + diff

        diff = abs(to_cell._x1 - to_cell._x2) / 2
        new_to_x = 0
        if to_cell._x1 < to_cell._x2:
            new_to_x = to_cell._x1 + diff 
        else:
            new_to_x = to_cell._x2 + diff 

        diff = abs(self._y1 - self._y2) / 2
        new_self_y = 0
        if self._y1 < self._y2:
            new_self_y = self._y1 + diff
        else:
            new_self_y = self._y2 + diff

        diff = abs(to_cell._y1 - to_cell._y2) / 2
        new_to_y = 0
        if to_cell._y1 < to_cell._y2:
            new_to_y = to_cell._y1 + diff
        else:
            new_to_y = to_cell._y2 + diff

        if undo == False:
            fill_color = "red"
        else:
            fill_color = "grey"

        self.canvas.create_line(
            new_self_x, new_self_y,
            new_to_x, new_to_y,
            fill=fill_color, width = 2
        )

        
    def draw(self, canvas, fill_color):
        self.canvas = canvas
        self.fill_color = fill_color        
        
        if self.has_left_wall:
            self.canvas.create_line( ##
            self._x1, self._y1, 
            self._x1, self._y2, 
            fill=fill_color, width=2
        )
        else:
            self.canvas.create_line(
            self._x1, self._y1, 
            self._x1, self._y2, 
            fill="white", width=2
        )
        if self.has_top_wall:
            self.canvas.create_line(
            self._x1, self._y1, 
            self._x2, self._y1, 
            fill=fill_color, width=2
        )
        else:
            self.canvas.create_line(
            self._x1, self._y1, 
            self._x2, self._y1, 
            fill="white", width=2
        )
        if self.has_right_wall:
            self.canvas.create_line(
            self._x2, self._y1, 
            self._x2, self._y2, 
            fill=fill_color, width=2
        )
        else:
            self.canvas.create_line(
            self._x2, self._y1, 
            self._x2, self._y2, 
            fill="white", width=2
        )
        if self.has_bottom_wall:
            self.canvas.create_line(
            self._x2, self._y2, 
            self._x1, self._y2, 
            fill=fill_color, width=2
        )
        else:
            self.canvas.create_line(
            self._x2, self._y2, 
            self._x1, self._y2, 
            fill="white", width=2
        )