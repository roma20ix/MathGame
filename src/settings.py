"""
"""


import os


# ------------ Главное окно ------------ #
FPS = 60
WIDTH = 500
HEIGHT = 800
TITLE = "MathGame"

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# ------------ Спрайты ------------ #
BG_SPRITE = os.path.abspath("images/bg.png")
LINE_SPRITE = os.path.abspath("images/line.png")
TIME_SPRITE = os.path.abspath("images/time.png")
LEFT_BUTTON_SPRITE = os.path.abspath("images/left_button.png")
UP_BUTTON_SPRITE = os.path.abspath("images/up_button.png")
RIGHT_BUTTON_SPRITE = os.path.abspath("images/right_button.png")

DIGITS = {
	"0": os.path.abspath("images/0.png"),
	"1": os.path.abspath("images/1.png"),
	"2": os.path.abspath("images/2.png"),
	"3": os.path.abspath("images/3.png"),
	"4": os.path.abspath("images/4.png"),
	"5": os.path.abspath("images/5.png"),
	"6": os.path.abspath("images/6.png"),
	"7": os.path.abspath("images/7.png"),
	"8": os.path.abspath("images/8.png"),
	"9": os.path.abspath("images/9.png")
}
