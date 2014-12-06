#coding=utf-8
Name              = u"Операция \"Гаргантюа\""   # Название игры
MousePos          = [0, 0]                      # Позиция курсора
CurMenu           = 0                           # Текущая сцена
Scenes            = []                          # Все сцены
Game              = False                       # Состояние игры
Diff              = 1                           # Сложность
Player            = None                        # Игрок

# Настройки
options = {"debug"      : True,     # Режим отладки
           "sound"      : 100,      # Громкость звука
           "music"      : 100,      # Громкость музыки
           "MainFont"   : None,     # Основной шрифт
           "HeadFont"   : None,     # Шрифт названия
           "QuoteFont"  : None,     # Шрифт цитат
           }

# Переменные для сцен
scene_create = []

# Список авторов
authors = {"Sergej Belousov \"Brounredo\""  : "Programisto",
           "Anastasija Pronina"             : "Pentristo",
           "Demid Ogorodnikov"              : "Scenaristo",
           "Ekaterina Leonova"              : "Pentristo",
           "Aleksandr Karev"                : "Muzikisto"}