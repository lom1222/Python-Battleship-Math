import tkinter
from helper import *


def create_screen(name, screen_size):
    screen = tkinter.Tk()
    screen.title(name)
    screen.geometry(screen_size)
    screen.resizable(False, False)
    return screen

def create_canvas(screen, width, height, background):
    canvas = tkinter.Canvas(screen, width=width, height=height)
    canvas.pack(padx=40,pady=40)
    screen.update()
    return canvas

def draw_game_state(canvas, game_state):
    max_x = canvas.winfo_width()
    max_y = canvas.winfo_height()
    pad_x = 10
    pad_y = 10
    background = to_hex((255, 255, 255))

    canvas.create_rectangle(pad_x, pad_y, max_x - pad_x, max_y - pad_y, fill=background)

    rows = len(game_state)
    cols = len(game_state[0])

    row_width = (max_x - pad_x*2) / rows
    col_height = (max_y - pad_y * 2) / cols

    for row in range(rows):
        for col in range(cols):
            rec_x = pad_x+row*row_width
            rec_y = pad_y+col*col_height
            canvas.create_rectangle()

    return 0