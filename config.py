import os

# Window size
WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600

# Categories
CATEGORY_DEFAULT = 0
CATEGORY_TARGET = 1
CATEGORY_DROP = 2

# Categories border color
DEFAULT_COLOR = 'white'
TARGET_COLOR = 'green'
DROP_COLOR = 'red'

# Name of image categories
DEFAULT_NAME = 'hat'
TARGET_NAME = 'sport_hat'
DROP_NAME = 'dropped'

# Name of input and output directory
INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'

# Pathes to folders with output images
DEFAULT_PATH = os.path.join(OUTPUT_FOLDER, DEFAULT_NAME)
TARGET_PATH = os.path.join(OUTPUT_FOLDER, TARGET_NAME)
DROP_PATH = os.path.join(OUTPUT_FOLDER, DROP_NAME)

PATHES = [DEFAULT_PATH, TARGET_PATH, DROP_PATH]

# Number of rows and columns in grid
ROWS = 5
COLS = 5

# Size of image in grid
IMG_W, IMG_H = 120, 120

# Logging file
LOG_FILE = 'sample.log'