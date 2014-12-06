#coding=utf-8
import pyglet               # Библиотека PyGlet
import sys                  # Системная библиотека
import vars                 # Переменные и константы
import colors               # Цвета
import gui                  # Функции пользовательского интерфейса
import player               # Класс игрока

#################
# Создание окна #
#################
window = pyglet.window.Window(800, 600, "Sozvezdie", False)
pyglet.gl.glClearColor(1, 1, 1, 1)

##########
# Шрифты #
##########
if sys.platform == "win32":
    vars.options["MainFont"] = ["Impact", 30]
    vars.options["HeadFont"] = ["Segoe Script", 40]
    vars.options["QuoteFont"] = ["None", 30]
else:
    vars.options["MainFont"]  = ["Luminari", 30]
    vars.options["HeadFont"]  = ["Comic Sans MS", 40]
    vars.options["QuoteFont"] = ["Snell Roundhand", 30]

# Инициализация игрока
vars.Player = player.Player(u"", u"", 14, u"")
# Инициализация сцен
gui.init_scenes()

#############
# Рисование #
#############
@window.event
def on_draw():
    window.clear()
    vars.Scenes[vars.CurMenu].background.blit(0, 0, 0)
    for i in vars.Scenes[vars.CurMenu].buttons:
        i.render.draw()
    for i in vars.Scenes[vars.CurMenu].sprites:
        i.draw()
    if vars.options["debug"]:
        LabelMouse = pyglet.text.Label(str(vars.MousePos), font_name=vars.options["MainFont"][0], font_size=vars.options["MainFont"][1], x=10, y=550, color=colors.Black)
        LabelMouse.draw()

#################
# Движение мыши #
#################
@window.event
def on_mouse_motion(x, y, dx, dy):
    vars.MousePos[0] = x
    vars.MousePos[1] = y

################
# Нажатие мыши #
################
@window.event
def on_mouse_press(x, y, button, modifiers):
    gui.check_button_click(vars.CurMenu, x, y)

# Запуск приложения
pyglet.app.run()