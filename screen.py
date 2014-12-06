#coding=utf-8

class Screen:
    background  = None  # Задний фон
    buttons     = []    # Кнопки
    sprites     = []    # Спрайты

    def __init__(self, background, buttons, sprites):
        self.background = background
        self.buttons = buttons
        self.sprites = sprites