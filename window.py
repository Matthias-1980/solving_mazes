from tkinter import Tk, BOTH, Canvas
from cells import *
from maze import *


class Window():
    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title = "Maze Solver"
        self.canvas_widget = Canvas()
        self.canvas_widget.pack()
        self.running = False
        self.root_widget.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while(self.running):
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas_widget, fill_color)

    def draw_cell(self, cell, fill_color):
        cell.draw(self.canvas_widget, fill_color)


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        self.canvas = canvas
        self.fill_color = fill_color
        self.canvas.create_line(
            self.point_a.x, self.point_a.y, 
            self.point_b.x, self.point_b.y, 
            fill=fill_color, width=2
        )

win = Window(800, 600)

#main_maze = Maze(20,20,5,8,10,10,win)
main_maze = Maze(20,20,10,13,15,15,win)

cell1 = Cell(50,50,60,60,win,True,True,True,True)
cell2 = Cell(90,50,100,60,win,True,True,True,True)
cell3 = Cell(100,210,110,220,win,True,True,True,True)
cell1.draw(win.canvas_widget, "blue")
cell2.draw(win.canvas_widget, "blue")
cell3.draw(win.canvas_widget, "blue")

cell1.draw_move(cell2)
cell2.draw_move(cell3)

point_a = Point(3,3)
point_b = Point(33,33)
line_a = Line(point_a, point_b)
win.draw_line(line_a, "blue")

win.wait_for_close()
