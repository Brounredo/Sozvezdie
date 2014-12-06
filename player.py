#coding=utf-8
import vars

class Player:
    ############
    # Свойства #
    ############
    Name           = u"Имя"      # Имя
    Surname        = u"Фамилия"  # Фамилия
    Otchestvo      = u"Отчество" # Отчество
    Age            = 14          # Возраст
    level          = 1           # Уровень
    exp            = 0           # Опыт
    hp             = 100         # Здоровье
    hungry         = 0           # Голод
    talents        = []          # Таланты (пассивные способности) (Способности.txt)
    spells         = []          # Активные способности (Способности.txt)
    specialization = 0           # Специализация (Специализации.txt)

    #################
    # Инициализация #
    #################
    def __init__(self, name, surname, age, otch):
        self.Name      = name
        self.Surname   = surname
        self.Age       = age
        self.Otchestvo = otch

    ##############
    # Обновление #
    ##############
    def update(self):
        if vars.Game:
            if self.hungry < 100:
                self.hungry += 1
            if self.hungry == 100:
                self.hp -= 1