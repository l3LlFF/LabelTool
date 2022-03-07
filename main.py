from tkinter import Canvas, Tk, Button, LabelFrame
from PIL import Image, ImageTk
import shutil
import logging
import time
from config import *
import os

logFile = 'sample.log'
logging.basicConfig(filename=LOG_FILE, filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')


def create_folders():
    """
    Creates folders for categories
    """
    if not os.path.exists(INPUT_FOLDER):
        os.mkdir(INPUT_FOLDER)
    if os.path.exists(OUTPUT_FOLDER):
        for path in PATHES:
            if not os.path.exists(path):
                os.mkdir(path)
    else:
        os.mkdir(OUTPUT_FOLDER)
        for path in PATHES:
            os.mkdir(path)


def left_click(event, row, col):
    """
    Left click handler
    """
    if event.widget.master['bg'] != TARGET_COLOR:
        event.widget.master.configure(bg=TARGET_COLOR)
        data[row][col]['category'] = CATEGORY_TARGET
    else:
        event.widget.master.configure(bg=DEFAULT_COLOR)
        data[row][col]['category'] = CATEGORY_DEFAULT


def right_click(event, row, col):
    """
    Right click handler
    """
    if event.widget.master['bg'] != DROP_COLOR:
        event.widget.master.configure(bg=DROP_COLOR)
        data[row][col]['category'] = CATEGORY_DROP
    else:
        event.widget.master.configure(bg=DEFAULT_COLOR)
        data[row][col]['category'] = CATEGORY_DEFAULT


def submit():
    time_end = time.time()
    global time_start
    difference = time_end - time_start
    time_start = time_end
    logging.info(difference)
    for i in range(ROWS):
        for j in range(COLS):
            if "filepath" not in data[i][j]:
                break
            if data[i][j]['category'] == CATEGORY_DEFAULT:
                shutil.copy(data[i][j]['filepath'], DEFAULT_PATH)
            elif data[i][j]['category'] == CATEGORY_TARGET:
                shutil.copy(data[i][j]['filepath'], TARGET_PATH)
            elif data[i][j]['category'] == CATEGORY_DROP:
                shutil.copy(data[i][j]['filepath'], DROP_PATH)
            os.remove(data[i][j]['filepath'])
            data[i][j] = {}
    grid_update()


def chunks(lst, n):
    """
    Yield successive n-sized chunks from lst.
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def grid_update():
    files_chunk = next(files, [])
    if not files_chunk:
        root.quit()
    for row in range(ROWS):
        for col in range(COLS):
            data[row][col] = {}
            data[row][col]['category'] = CATEGORY_DEFAULT
            border = LabelFrame(canvas, bd=6, bg="white")
            border.grid(columnspan=1, row=row, column=col)
            data[row][col]['border'] = border
            if row * COLS + col >= len(files_chunk):
                btn = Button(border, image=white)
                btn.grid(columnspan=1)
            else:
                filepath = f'{INPUT_FOLDER}/{files_chunk[row * COLS + col]}'
                img_file = Image.open(filepath)
                data[row][col]['filepath'] = filepath
                img_file = img_file.resize((IMG_H, IMG_W))
                img = ImageTk.PhotoImage(img_file)
                data[row][col]['img'] = img
                btn = Button(border, image=data[row][col]['img'])
                btn.grid(columnspan=1, row=row, column=col)
                btn.bind("<Button-1>", lambda event, row=row, col=col: left_click(event, row, col))
                btn.bind("<Button-2>", lambda event, row=row, col=col: right_click(event, row, col))
    btn = Button(canvas, text='Submit', height=3, width=25, command=submit)
    btn.grid(columnspan=COLS, row=ROWS + 1, column=0)


if __name__ == '__main__':
    root = Tk()
    root.title('LabelTool')
    canvas = Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack()
    create_folders()
    img_white = Image.open('white.jpg')
    img_white = img_white.resize((IMG_H, IMG_W))
    white = ImageTk.PhotoImage(img_white)
    files = [f for f in os.listdir(INPUT_FOLDER) if not f.startswith('.')]
    data = [[{} for x in range(COLS)] for y in range(ROWS)]
    files = chunks(files, ROWS * COLS)
    grid_update()
    time_start = time.time()
    root.mainloop()
