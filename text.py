#coding=utf-8
import pyglet
import vars

class Text:
    text   = u""                        # Надпись
    font   = vars.options["MainFont"]   # Шрифт
    render = None                       # Отрисованное изображение
    pos    = [0, 0]                     # Позиция
    color  = (0, 0, 0)                  # Цвет текста

    def __init__(self, _text, _pos, _color):
        self.font = vars.options["MainFont"]
        self.text  = _text
        self.pos   = _pos
        self.color = _color
        self.render = pyglet.text.Label(self.text, font_name=self.font[0], font_size=self.font[1], x=self.pos[0], y=self.pos[1], color=self.color, bold=True)

    def upd_render(self):
        self.render = pyglet.text.Label(self.text, font_name=self.font[0], font_size=self.font[1], x=self.pos[0], y=self.pos[1], color=self.color, bold=True)

    def check_click(self, mx, my):
        if ((mx > self.render.x) and (mx < self.render.x + self.render.content_width)) and ((my > self.render.y) and (my < self.render.y + self.render.content_height)):
            return True
        else:
            return False