#coding=utf-8
import pyglet
import vars
import colors
import random
import quotes
import text
import os
import sys
import screen

###########################
# Проверка нажатия кнопки #
###########################
def check_button_click(menu, mx, my):
    # Главное меню
    if menu == 0:
        if vars.Scenes[0].buttons[0].check_click(mx, my): # Новая смена...
            vars.CurMenu = 3
        if vars.Scenes[0].buttons[1].check_click(mx, my): # Загрузить игру...
            vars.CurMenu = 2
        if vars.Scenes[0].buttons[2].check_click(mx, my): # Настройки игры
            vars.CurMenu = 1
        if vars.Scenes[0].buttons[3].check_click(mx, my): # Суровый совет
            vars.Scenes[0].buttons[6].text = random.choice(quotes.advices)
            vars.Scenes[0].buttons[6].render = pyglet.text.Label(vars.Scenes[0].buttons[6].text, font_name=vars.options["QuoteFont"][0], font_size=vars.options["QuoteFont"][1], x=vars.Scenes[0].buttons[6].pos[0], y=vars.Scenes[0].buttons[6].pos[1], color=vars.Scenes[0].buttons[6].color, bold=True)
        if vars.Scenes[0].buttons[4].check_click(mx, my): # Выход =(
            sys.exit()
    # Меню настроек
    elif menu == 1:
        if vars.Scenes[1].buttons[0].check_click(mx, my): # Режим отладки
            vars.options["debug"] = not vars.options["debug"]
            vars.Scenes[1].buttons[0] = text.Text(u"Режим отладки - " + str(vars.options["debug"]), [100, 450], colors.Yellow)
        if vars.Scenes[1].buttons[1].check_click(mx, my): # Громкость звука
            pass
        if vars.Scenes[1].buttons[2].check_click(mx, my): # Громкость музыки
            pass
        if vars.Scenes[1].buttons[3].check_click(mx, my): # Основной шрифт
            pass
        if vars.Scenes[1].buttons[4].check_click(mx, my): # Назад
            vars.CurMenu = 0
    # Меню загрузки игры
    elif menu == 2:
        if vars.Scenes[2].buttons[1].check_click(mx, my): # Назад
            vars.CurMenu = 0
    # Меню создания персонажа
    elif menu == 3:
        if vars.Scenes[3].buttons[0].check_click(mx, my): # Сложность
            if vars.Diff < 3:
                vars.Diff += 1
            else:
                vars.Diff = 1
            vars.Scenes[3].buttons[0] = text.Text(u"Сложность: " + str(vars.Diff), [100, 450], colors.Yellow)
        if vars.Scenes[3].buttons[2].check_click(mx, my): # Удаление имени
            vars.Player.Name = u""
            vars.Scenes[3].buttons[1] = text.Text(u"Имя: " + vars.Player.Name, [100, 400], colors.Yellow)
        if vars.Scenes[3].buttons[4].check_click(mx, my): # Удаление фамилии
            vars.Player.Surname = u""
            vars.Scenes[3].buttons[3] =  text.Text(u"Фамилия: " + vars.Player.Surname, [100, 350], colors.Yellow)
        if vars.Scenes[3].buttons[6].check_click(mx, my): # Удаление отчества
            vars.Player.Otchestvo = u""
            vars.Scenes[3].buttons[5] = text.Text(u"Отчество: " + vars.Player.Otchestvo, [100, 300], colors.Yellow)
        if vars.Scenes[3].buttons[8].check_click(mx, my): # Назад
            vars.CurMenu = 0

######################
# Инициализация сцен #
######################
def init_scenes():
    ################
    # Главное меню #
    ################
    vars.Scenes.append(screen.Screen(pyglet.image.load(os.path.dirname(os.path.abspath(__file__)) + "/Images/main_menu.jpg"),
                                     [text.Text(u"Новая смена...",    [250, 400], colors.Blue3),
                                      text.Text(u"Загрузить игру...", [250, 325], colors.Yellow),
                                      text.Text(u"Настройки игры",    [250, 250], colors.Blue3),
                                      text.Text(u"Суровый совет...",  [250, 175], colors.Yellow),
                                      text.Text(u"Выход =(",          [250, 100], colors.Blue3),
                                      text.Text(vars.Name,            [125, 500], colors.Bisque),
                                      text.Text(u"",                  [ 25,  50], colors.Red)],
                                     []))
    vars.Scenes[0].buttons[5].font = vars.options["HeadFont"]
    vars.Scenes[0].buttons[5].upd_render()
    vars.Scenes[0].buttons[6].font = vars.options["QuoteFont"]
    vars.Scenes[0].buttons[6].upd_render()

    #############
    # Настройки #
    #############
    vars.Scenes.append(screen.Screen(pyglet.image.load(os.path.dirname(os.path.abspath(__file__)) + "/Images/main_menu.jpg"),
                                     [text.Text(u"Режим отладки - " + str(vars.options["debug"]), [100, 450], colors.Yellow),
                                      text.Text(u"Громкость звука - " + str(vars.options["sound"]), [100, 375], colors.Yellow),
                                      text.Text(u"Громкость музыки - " + str(vars.options["music"]), [100, 300], colors.Blue3),
                                      text.Text(u"Основной шрифт - " + str(vars.options["MainFont"]), [100, 225], colors.Yellow),
                                      text.Text(u"Назад", [100, 70], colors.Blue3)],
                                     []))

    #################
    # Загрузка игры #
    #################
    vars.Scenes.append(screen.Screen(pyglet.image.load(os.path.dirname(os.path.abspath(__file__)) + "/Images/main_menu.jpg"),
                                     [text.Text(u"Ещё не готово!", [250, 450], colors.Yellow),
                                      text.Text(u"Назад", [100, 70], colors.Blue3)],
                                     []))

    ######################
    # Создание персонажа #
    ######################
    vars.Scenes.append(screen.Screen(pyglet.image.load(os.path.dirname(os.path.abspath(__file__)) + "/Images/create.jpg"),
                                     [text.Text(u"Сложность: " + str(vars.Diff), [100, 450], colors.Yellow),
                                      text.Text(u"Имя: " + vars.Player.Name, [100, 400], colors.Yellow),
                                      text.Text(u"⬅︎", [50, 400], colors.Yellow),
                                      text.Text(u"Фамилия: " + vars.Player.Surname, [100, 350], colors.Yellow),
                                      text.Text(u"⬅︎", [50, 350], colors.Yellow),
                                      text.Text(u"Отчество: " + vars.Player.Otchestvo, [100, 300], colors.Yellow),
                                      text.Text(u"⬅︎", [50, 300], colors.Yellow),
                                      text.Text(u"В путь!", [500, 70], colors.Yellow),
                                      text.Text(u"Назад", [100, 70], colors.Yellow)],
                                     []))