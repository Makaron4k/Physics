from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidget, QLineEdit, QTextEdit, QButtonGroup, QGroupBox, QMessageBox, QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QInputDialog, QMainWindow
from random import shuffle, randint, random
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
import json

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Решу ФИЗИКУ!')
main_win.resize(1024, 600)
app.setStyleSheet("QLabel{font-size: 40pt; font-weight: bold; font-family: Comic Sans MS;} QPushButton{font-size: 13pt; font-weight: bold; font-family: Arial;}")
main_win.setObjectName('win')
main_win.setStyleSheet('#win{background-color: BurlyWood;} QLabel{color: rgb(220,20,60)} QPushButton{color: rgb(0,0,205); background-color: rgb(205,133,63);} QLineEdit{color: rgb(178,34,34); background-color: rgb(222,184,135); font-size: 17pt; font-weight: bold; font-family: Comic Sans MS;} QRadioButton{color: rgb(178,34,34); background-color: rgb(222,184,135); font-size: 17pt; font-weight: bold; font-family: Comic Sans MS}')
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap("RF.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
main_win.setWindowIcon(icon)

class Question():
    def __init__(self, question, right, wrong1, wrong2, wrong3):
        self.question = question
        self.right = right
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

class Item():
    def __init__(self, name, second_name, c, max_t, max_t2, min_t, m, l, s, s2, q_type, cur_quest):
        self.name = name
        self.second_name = second_name
        self.c = c
        self.max_t = max_t
        self.min_t = min_t
        self.m = m
        self.l = l
        self.s = s
        self.type = q_type
        self.cur_quest = cur_quest
        self.max_t2 = max_t2
        self.s2 = s2

#Список вопросов теста
t_q1 = Question('Каким процессом является сгорание?', 'Химическим', 'Физическим', 'Плавительным', 'Утеплительным')
t_q12 = Question('Как называется велечина, показывающая выделяющееся кол-во теплоты при сгорании топлива?', 'Удельная теплота сгорания', 'Удельная энергие сгорания', 'Удельная теплота топлива', 'Удельная теплота')
t_q13 = Question('Что из перечисленного не является топливом?', 'Кварц', 'Нефть', 'Торф', 'Нет верного ответа')
t_q14 = Question('Что происходит, если атомы соединяются в молекулу?', 'Энергия выделяется', 'Энергия поглощается', 'Ничего не происходит', 'Нет верного ответа')
t_q15 = Question('Удельная теплота сгорания топлива измеряется в', 'Дж/кг', 'Дж/с', 'Дж/кг*Градусы Цельсия', 'Дж')
t_q21 = Question('Единица электрического заряда (количество электронов) равна', '1 Кл = 1 А · 1 с', '1 Кл = 1 А · 1 мин', '1 Кл = 1 А · 1 ч', 'Нет верного ответа')
t_q22 = Question('Как названа единица силы тока?', 'Ампер', 'Джоуль', 'Ватт', 'Кулон')
t_q23 = Question('По какой формуле определяют силу тока?', 'I = q/t', 'N = A/t', 'Уm = Q/λ', 'm = Q/L')
t_q24 = Question('Что из перечисленного не является заряженной частицей?', 'Фотон', 'Протон', 'Электрон', 'Нет верного ответа')
t_q25 = Question('В честь какого учёного названа единица силы тока?', 'Ампер', 'Вольт', 'Тесла', 'Франклин')
t_q3 = Question('От чего НЕ зависит внутренняя энергия тела?', 'Положение тела', 'Температура тела', 'Агрегатное состояние тела', 'Скорость тела')
t_q32 = Question('Какая энергия изменяется при подбрасывании тела?', 'Потенциальная', "Кинетическая", "Понтенциальная и кинетическая", "Внутренняя.")
t_q33 = Question('Какими двумя способами можно изменить внутреннюю энергию?', "Совершая работу и нагревая", "Подкидывая и нагревая", "Охлождая и держа на месте", "Совершая работу и охлождая")
t_q34 = Question('Изменится ли внутренняя энергия морской воды когда наступит ночь?', "Да, она уменьшится", "Нет, останется той же", "Да, она увеличтся", "У воды нет внутренней энергии")
t_q35 = Question('Когда автомобиль расходует больше топлива?', "Когда едет медленно, с остановками", "Быстро и без остановок", "Медленно без остановок", "Быстро с остановками")
t_q4 = Question("Как обозначается вольтметр в цепи?", "Буква V в окружности", "Буква W в окружности", "Буква A в окружности", "Буква Vm в окружности")
t_q42 = Question("Какие знаки стоят на клемах вольтметра?", "Плюс и минус", "Плюс и плюс", "Минус и минус", "Нет правильного ответа")
t_q43 = Question("Как включается вольметр в цепь?", "Паралельно", "Последовательно", "И последовательно и паралельно", "Нет верного ответа")
t_q44 = Question("Cилу тока измеряют", "Амперметром", "Вольтметром", "Гальванометром", "Нет правильного ответа")
t_q45 = Question("Как обозначается амперметр в цепи?", "Буква A в окружности", "Буква W в окружности", "Буква A в квадрате", "Буква A в треугольнике")
t_q5 = Question('Температура тела зависит от?', "Скорости движения молекул", "Размеров тела", "Скорости движенрия тела", "Положения тела относительно Земли")
t_q5_2 = Question('Количетсво теплоты обозначается в?', 'Джоулях', 'Килограммах', 'Дж/кг', 'Градусах цельсия')
t_q6 = Question('Каким знаком обозначается количество теплоты?', "Q", "q", "L", "c")
t_q6_2 = Question('Формула расчёта количества теплоты, необходимого для нагревания тела.', "cm(t2-t1)", "qm", "E = Eк + Eп", "Lm")
t_q6_3 = Question('В чугунный сосуд налили только что расплавленное золото, что произойдёт?', 'Золото начнёт охлажджаться и твердеть', 'Сосуд расплавится', 'Ничего не произайдёт', 'Золото охладится')
t_q5_3 = Question('Какого вида теплопередачи не существует?', "Ветрянное", "Излучение", "Конвекция", "Теплопроводность")
t_q5_4 = Question('Какой воздух тяжелее?', "Холодный", "Тёплый", "Они одинаковы", "Воздух не имеет массы")
q_list = []
queue = []

#Создание виджетов
welcome_text = QLabel('Решу Физику!')
welcome_text.setWordWrap(True)
begin_btn1 = QPushButton('Теория')
begin_btn2 = QPushButton('Практика')
main_layout = QVBoxLayout()
button_layout = QHBoxLayout()
#music_btn = QPushButton('Выключить музыку')
music_layout = QHBoxLayout()
group_layout = QHBoxLayout()
#Выбор темы
group_box = QGroupBox()
theme1 = QRadioButton("Сгорание. Удельная теплота сгорания")
theme2 = QRadioButton("Ток. Сила тока.")
theme3 = QRadioButton("Внутренняя и механическая энергия тела")
theme4 = QRadioButton("Температура")
group_box.hide()
group = QButtonGroup()
group.addButton(theme1)
group.addButton(theme2)
group.addButton(theme3)
group.addButton(theme4)
group.setExclusive(False)
b3_layout1 = QVBoxLayout()
b3_layout2 = QVBoxLayout()
b3_layout3 = QHBoxLayout()
b3_layout4 = QHBoxLayout()
b3_layout5 = QHBoxLayout()
#Виджеты задач
Line_Tag = QLineEdit('')
Line_Tag.setPlaceholderText('Введите ответ: ')
Line_Tag.hide()
line_layout = QHBoxLayout()
#Виджеты для теста
btn = QPushButton("Ответить")
btn.hide()
layout_2b = QVBoxLayout()
layout_b1 = QHBoxLayout()
layout_b2 = QVBoxLayout()
layout_b3 = QVBoxLayout()
RadioGroupBox = QGroupBox("Варианты")
rbtn1 = QRadioButton()
rbtn2 = QRadioButton()
rbtn3 = QRadioButton()
rbtn4 = QRadioButton()
RadioGroupBox.hide()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
ResultGroup = QGroupBox('Результат')
right_ans = QLabel('Будет правильный ответ')
resu = QLabel('Правильный ответ!')
ResultGroup.hide()
answer = [rbtn1, rbtn2, rbtn3, rbtn4]
main_win.cur_quest = -1
thing = Item('', "", 0, 0, 0, randint(0, 1), randint(1, 10), 0, 0, 0, 0, 0)
#Теория
theory_layout = QHBoxLayout()
list_theme = QListWidget()
theory_text = QTextEdit()
list_theme.hide()
theory_text.hide()
data = {'тест': ''}
    #theory = {
    #    'Основные формулы курса физики 8го класса': 'Формулы:\n\n Расчёт количества теплоты, необходимого для нагревания тела или выделяемого им при охлаждении - Q = cm(t2-t1)\n\n Расчёт количества теплоты, выделяемого при сгорании топлива - Q = qm \n\n Закон сохранения и превращения энергии в механ. и тепловых процессах - E = Ек + Еп\n\n Сила тока - I = q/t\n\n Напряжение - U = A/q. Следствия: A = Uq; q = A/U\n\n Закон Ома - I = U/R. Следствия: U = IR, R = U/I\n\n hj',
    #    'Температура': 'Тепловое движение. Температура.\n\n В окружающем нас мире происходят различные физические явления, которые связаны с нагреванием и охлаждением тел. Мы знаем, что при нагревании холодная вода вначале становится тёплой, а затем горячей. Такими словами, как «холодный», «тёплый» и «горячий», мы указываем на различную степень нагретости тел, или, как говорят в физике, на различную температуру тел. Температуру тел измеряют с помощью термометра и выражают в градусах Цельсия (°С). Диффузия при более высокой температуре происходит быстрее.',
    #    'Внутренняя энергия': "При изучении физики рассматриваются механические, тепловые, световые, электрические и другие явления. С некоторыми механическими явлениями мы уже познакомились. Известно также, что существует два вида механической энергии: кинетическая и потенциальная.",
    #    'Теплопроводность': "",
    #    'Конвекция': "",
    #    'Излучение': "",
    #    'Количество теплоты': "",
    #    'Удельная теплоёмкость': "",
    #    'Таблица удельной теплоемкости некоторых веществ': 'Вещество  с, Дж/кг*C\n\n Золото 130\n Ртуть 138\n Свинец 140\n Олово 230\n Серебро 250\n Медь 400\n Цинк 400\n Латунь 400\n Железо 460\n Сталь 500\n Чугун 540\n Графит 750\n Стекло лабораторное 840\n Кирпич 880\n Алюминий 920\n Масло подсолнечное 1700\n Лёд 2100\n Керосин 2100\n Эфир 2350\n Дерево(Дуб) 2400\n Спирт 2500\n Вода 4200',
    #    'Таблица удельной теплоты сгорания некоторых видов топлива': 'Вещество  q, Дж/кг\n\n Порох  0.38 * 10^7\n Дрова сухие 1.0 * 10^7\n Торф 1.4 * 10^7\n Каменный уголь 2.7 * 10^7\n Спирт 2.7 * 10^7\n Антрацит 3.0 * 10^7\n Древесный уголь 3.4 * 10^7\n Природный газ 4.4 * 10^7\n Нефть 4.4 * 10^7\n Бензин 4.6 * 10^7 \n Керосин 4.6 * 10^7\n Водород 12 * 10^7',
    #    'Таблица температуры плавления некоторых веществ(при нормальном атм. давлении)': 'tпл, *C\n\n Водород -259\n Кислород -219\n Азот -210\n Спирт -114\n Ртуть -39\n Лёд 0\n Цезий 29\n Калий 63\n Натрий 98\n Олово 232\n Свинец 327\n Янтарь 360\n Цинк 420\n Алюминий 660\n Серебро 962\n Латунь 1000\n Золото 1064\n Медь 1085\n Чугун 1200\n Сталь 1500\n Железо 1539\n Платина 1772\n Осмий 3045\n Вольфрам 3387',
    #    'Таблица температуры кипения некоторых веществ': 'tкип, *C\n\n Водород -238\n Кислород -183\n Молоко 100\n Эфир 35\n Спирт 78\n Вода 100\n Ртуть 357\n Свинец 1740\n Медь 2567 \n Железо 2750',
    #    'Таблица удельной теплоты парообразования некоторых веществ': 'L, дж*кг\n\n Вода 2.3 * 10^6\n Амиак(жидкий) 1.4 * 10^6\n Спирт 0.9 * 10^6\n Эфир 0.4 * 10^6\n Ртуть 0.3 * 10^6\n Воздух(жидкий) 0.2 * 10^6',
    #    'Таблица удельной теплоты плавления некоторых веществ(при нормальном атм. дав)': 'λ, Дж/кг\n\n Алюминий 3.9 * 10^5\n Лёд 3.4 * 10^5\n Железо 2.7 * 10^5\n Медь 2.1 * 10^5\n Парафин 1.5 * 10^5\n Спирт 1.1 * 10^5\n Серебро 0.87 * 10^5\n Сталь 0.84 * 10^5\n Золото 0.84 * 10^5\n Водород 0.59 * 10^5\n Олово 0.59 * 10^5\n Свинец 0.25 * 10^5\n Кислород 0.14 * 10^5\n Ртуть 0.12 * 10^5',
    #    'Таблица удельного электрического сопротивления некоторых тел': '',
    #    'Реостаты': '',
    #    'Напряжение': '',
    #    'КПД теплового двигателя': '',
    #    'Амперметр': '',
    #    'Вольтметр. Измерение напряжения': '',
    #    'Направление элекрического тока': '',
    #    'Действия электрического тока': '',
    #    'Электрическая цепь и её составные части': '',
    #    'Кипение': '',
    #    'Агрегатные состояния вещества': ''}

    #with open('text.json', 'w', encoding = "utf-8") as file:
        #json.dump(theory, file)

with open('text.json', 'r', encoding = "utf-8") as file:
    data = json.load(file)

#Функции
def p_theme_select():
    if theme1.isChecked() == True:
        queue.append('1')
    if theme2.isChecked() == True:
        queue.append('2')
    if theme4.isChecked() == True:
        queue.append('4')
    if queue[0] == '1':
        p_type1()
        queue.remove('1')
    elif queue[0] == '2':
        p_type2()
        queue.remove('2')
    elif queue[0] == '4':
        p_type4()
        queue.remove('4')

def test_theme_select():
    q_list.clear()
    if theme1.isChecked() == True:
        q_list.append(t_q1)
        q_list.append(t_q12)
        q_list.append(t_q13)
        q_list.append(t_q14)
        q_list.append(t_q15)
        q_list.append(t_q6)
        q_list.append(t_q6_2)
        theme1.setChecked(False)
    if theme2.isChecked() == True:
        q_list.append(t_q21)
        q_list.append(t_q22)
        q_list.append(t_q23)
        q_list.append(t_q24)
        q_list.append(t_q25)
        q_list.append(t_q4)
        q_list.append(t_q42)
        q_list.append(t_q43)
        q_list.append(t_q44)
        q_list.append(t_q45)
        theme2.setChecked(False)
    if theme3.isChecked() == True:
        q_list.append(t_q3)
        q_list.append(t_q32)
        q_list.append(t_q33)
        q_list.append(t_q34)
        q_list.append(t_q35)
        theme3.setChecked(False)
    if theme4.isChecked() == True:
        q_list.append(t_q5)
        q_list.append(t_q5_2)
        q_list.append(t_q5_2)
        q_list.append(t_q6_3)
        q_list.append(t_q5_3)
        q_list.append(t_q5_4)
        theme4.setChecked(False)
    shuffle(q_list)
    group_box.hide()

def theory_start():
    global data
    begin_btn2.setText('Сохранить текст')
    welcome_text.hide()
    begin_btn1.setText('Вернуться на главный экран')
    list_theme.addItems(data)
    list_theme.show()
    theory_text.show()

def add_text():
    theory_text.clear()
    theory_text.setText(data[list_theme.selectedItems()[0].text()])

def check_screen1():
    if begin_btn1.text() == 'Теория':
        theory_start()
    elif begin_btn1.text() == 'Тест':
        test_theme_select()
        btn.show()
        begin_btn1.hide()
        begin_btn2.hide()
        main_win.cur_quest = -1
        main_win.score = 0
        next_quest()
    elif begin_btn1.text() == 'Вернуться на главный экран':
        btn.hide()
        theory_text.hide()
        list_theme.hide()
        Line_Tag.hide()
        begin_btn1.show()
        begin_btn1.setText('Теория')
        begin_btn2.show()
        begin_btn2.setText('Практика')
        welcome_text.setText('Решу ФИЗИКУ!')
        welcome_text.show()
        Line_Tag.clear()
        q_list.clear()

def check_screen2():
    if begin_btn2.text() == 'Практика':
        practice_screen()
    elif begin_btn2.text() == 'Задачи':
        group_box.hide()
        p_theme_select()
        theme1.setChecked(False)
        theme2.setChecked(False)
        theme3.setChecked(False)
        theme4.setChecked(False)
    elif begin_btn2.text() == 'Сохранить текст':
        data[list_theme.selectedItems()[0].text()] = theory_text.toPlainText()
        with open('text.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)

def practice_screen():
    group_box.show()
    welcome_text.setText('Выбери тип практики и темы')
    begin_btn1.setText('Тест')
    begin_btn2.setText('Задачи')

def check_p_ans():
    global thing
    if len(queue) < 1:
        btn.setText('Новая задача')
    else:
        btn.setText('Следующая задача')
    begin_btn1.show()
    begin_btn1.setText('Вернуться на главный экран')
    answer = str(Line_Tag.text())
    if thing.type == 1:
        if answer == str(thing.m*thing.c*(thing.max_t - thing.min_t)) and thing.cur_quest == 1:
            welcome_text.setText("Правильно!")
        elif answer != str(thing.m*thing.c*(thing.max_t - thing.min_t)) and thing.cur_quest == 1:
            welcome_text.setText('Неправильно! Правильный ответ:' + str(thing.m*thing.c*(thing.max_t - thing.min_t)))
        elif answer == str(thing.c) and thing.cur_quest == 2:
            welcome_text.setText('Правильно!')
        elif answer != str(thing.c) and thing.cur_quest == 2: 
           welcome_text.setText('Неправильно! Правильный ответ:' + str(thing.c))
        elif answer == str(thing.m) and thing.cur_quest == 3:
           welcome_text.setText('Правильно!')
        elif answer != str(thing.m) and thing.cur_quest == 3:
           welcome_text.setText('Неправильно! Праввильный ответ:' + str(thing.m))
        elif answer == str(round((((thing.max_t-thing.min_t)*thing.m*thing.c+thing.m*thing.max_t2)/thing.l), 2)):
            welcome_text.setText('Правильно!')
        elif answer != str(round((((thing.max_t-thing.min_t)*thing.m*thing.c+thing.m*thing.max_t2)/thing.l), 2)):
            welcome_text.setText('Неправильно! Правильный ответ:' + str(round((((thing.max_t-thing.min_t)*thing.m*thing.c+thing.m*thing.max_t2)/thing.l), 2)))
    if thing.type == 2:
        if answer == str(thing.min_t) and (thing.cur_quest == 1 or thing.cur_quest == 2):
            welcome_text.setText('Правильно!')
        elif answer != str(thing.min_t) and (thing.cur_quest == 1 or thing.cur_quest == 2):
            welcome_text.setText('Неправильно! Правильный ответ: ' + str(thing.min_t))
        elif answer == str(thing.max_t) and (thing.cur_quest == 3 or thing.cur_quest == 4):
            welcome_text.setText('Правильно!')
        elif answer != str(thing.min_t) and (thing.cur_quest == 3 or thing.cur_quest == 4):
            welcome_text.setText('Неправильно! Правильный ответ: ' + str(thing.max_t))
        elif answer == str(thing.m) and (thing.cur_quest == 5 or thing.cur_quest == 6):
            welcome_text.setText('Правильно!')
        elif answer != str(thing.m) and (thing.cur_quest == 5 or thing.cur_quest == 6):
            welcome_text.setText('Неправильно! Правильный ответ: ' + str(thing.m))
        elif answer != str(thing.s) and thing.cur_quest == 7:
            welcome_text.setText('Неправильно! Правильный ответ: ' + str(thing.s))
        elif answer == str(thing.s) and thing.cur_quest == 7:
            welcome_text.setText('Правильно!')
        elif answer != str(thing.l) and thing.cur_quest == 8:
            welcome_text.setText('Неправильно! Правильный ответ: ' + str(thing.l))
        elif answer == str(thing.l) and thing.cur_quest == 8:
            welcome_text.setText('Правильно!')
        elif answer != str(thing.c) and thing.cur_quest == 9:
            welcome_text.setText('Неправильно! Правильный ответ: ' + str(thing.c))
        elif answer == str(thing.c) and thing.cur_quest == 9:
            welcome_text.setText('Правильно!')
    elif thing.type == 4:
        if answer == str(thing.max_t2):
            welcome_text.setText('Правильно!')
        else:
            welcome_text.setText('Неправильно! Правильный ответ: ' + str(thing.max_t2))

def p_type1():
    global thing
    Line_Tag.show()
    btn.show()
    begin_btn1.hide()
    begin_btn2.hide()
    btn.setText('Проверить')
    thing.name = randint(1,5)
    if thing.name == 1:
        thing = Item('воды', "Воду", 4200, 100, 0, randint(0, 99), randint(1, 10), 0, 0, 0, 1, 0)
    elif thing.name == 2:
        thing = Item('серебра', "Серебро", 450, 962, 0, randint(-100, 961), randint(1, 10), 0, 0, 0, 1, 0)
    elif thing.name == 3:
        thing = Item('латуни', "Латунь", 400, 1000, 0, randint(-100, 999), randint(1, 10), 0, 0, 0, 1, 0)
    elif thing.name == 4:
        thing = Item('стали', "Сталь", 500, 1500, 0, randint(-100, 1499), randint(1, 10), 0, 0, 0, 1, 0)    
    elif thing.name == 5:
        thing = Item('льда', "Лёд", 2100, 0, 0, randint(-100, -1), randint(1, 10), 0, 0, 0, 1, 0)

    thing.cur_quest = randint(1, 4)
    if thing.cur_quest == 1:
        welcome_text.setText(thing.second_name + ' с температурой ' + str(thing.min_t) + " градусов и массой " + str(thing.m) + " кг нагрели до " + str(thing.max_t) + " градусов. Найдите выделенную энергию, если удельная теплота равна " + str(thing.c) + " джоулей/кг*грудсов цельсия.")
    elif thing.cur_quest == 2:
        welcome_text.setText(thing.second_name + ' массой ' + str(thing.m) + " кг при нагревании с " + str(thing.min_t) + ' градусов до ' + str(thing.max_t) + ' градусов выделяет ' + str(thing.m*thing.c*(thing.max_t - thing.min_t)) + ' джоулей. Найдите удельную теплоёмкость.')
    elif thing.cur_quest == 3:
        welcome_text.setText(thing.second_name + ' с ' + str(thing.min_t) + ' градусов нагрели до ' + str(thing.max_t) + ' градусов. Найдите массу ' + thing.name + ' если удельная теплоёмкость равна ' + str(thing.c) + ' джоулей/кг*граудсов цельсия.')
    elif thing.cur_quest == 4:
        p_type1_4()
    return(thing)

def p_type2():
    global thing
    Line_Tag.show()
    btn.show()
    begin_btn1.hide()
    begin_btn2.hide()
    btn.setText('Проверить')
    thing = Item('меди', "", 0.017, randint(0, 10), round(random(), 2), randint(1, 200), 0, randint(1, 20), randint(0, 3), round(random(), 2), 2, 0)
    thing.name = randint(1, 5)
    if thing.name == 1:
        thing.name = 'серебра'
        thing.c = 0.016
    elif thing.name == 2:
        thing.name = 'меди'
        thing.c = 0.017
    elif thing.name == 3:
        thing.name = 'вольфрама'
        thing.c = 0.055
    elif thing.name == 4:
        thing.name = 'никелина'
        thing.c = 0.4
    elif thing.name == 5:
        thing.name = 'графита'
        thing.c = 13
    thing.max_t = thing.max_t + thing.max_t2
    thing.m = round(thing.min_t/thing.max_t, 2)
    thing.s = thing.s + thing.s2

    thing.cur_quest = randint(1, 9)
    if thing.cur_quest == 1:
        welcome_text.setText('Через проводник проходит ток с силой ' + str(thing.max_t) + ' ампер. Найдите напряжение, если сопротивление равно ' + str(thing.m) + ' Ом.')
    elif thing.cur_quest == 2:
        welcome_text.setText('Через проводник из ' + thing.name + ' с площадью поперечного сечения ' + str(thing.s) + ' мм^2 и длинной ' + str(thing.l) + ' м. Найдите напряжение, если сила тока равна ' + str(thing.max_t) + ' ампер.')
    elif thing.cur_quest == 3:
        welcome_text.setText('Напряжение проводника равно ' + str(thing.min_t) + ' вольт. Найдите силу тока, если сопротивление равно ' + str(thing.m) + ' Ом.')
    elif thing.cur_quest == 4:
        welcome_text.setText('Через проводник из ' + thing.name + ' с площадью поперечного сечения ' + str(thing.s) + ' мм^2 и длинной ' + str(thing.l) + ' м. Найдите силу тока, если напряжение равно ' + str(thing.min_t) + 'вольт.')
    elif thing.cur_quest == 5:
        welcome_text.setText('Напряжение проводника равно ' + str(thing.min_t) + ' вольт. Найдите сопротивление, если сила тока равно ' + str(thing.max_t) + ' ампер.')
    elif thing.cur_quest == 6:
        welcome_text.setText('Дан проводник из ' + thing.name + ' с площадью поперечного сечения ' + str(thing.s) + ' мм^2 и длинной ' + str(thing.l) + ' м. Найдите сопротивление.')
    elif thing.cur_quest == 7:
        welcome_text.setText('Через проводник из ' + thing.name + ' с длинной ' + str(thing.l) + ' м проходит ток с силой в ' + str(thing.max_t) + ' ампер и напряжение проводника равно ' + str(thing.min_t) + ' вольт. Найдите площадь поперечного сечения.')
    elif thing.cur_quest == 8:
        welcome_text.setText('Через проводник из ' + thing.name + ' с поперечным сечением ' + str(thing.s) + ' мм^2 проходит ток с силой в ' + str(thing.max_t) + ' ампер и напряжение проводника равно ' + str(thing.min_t) + ' вольт. Найдите длину проводнику.')
    elif thing.cur_quest == 9:
        welcome_text.setText('Через проводник с длинной ' + str(thing.l) + ' и площадью поперечного сечения ' + str(thing.s) + 'проходит ток с силой в ' + str(thing.max_t) + ' ампер и напряжение проводника равно ' + str(thing.min_t) + ' вольт. Найдите удельное сопротивление проводника.')
    
def p_type1_4():
    global thing
    thing = Item('', '', 0, 1, 0, randint(0, 1), randint(0, 10), 0, 0, 0, 1, 4)
    thing.name = randint(1, 5)
    thing.second_name = randint(1, 5)
    if thing.name == 1:
        thing.name = 'каменного угля'
        thing.l = 27*10**6
    elif thing.name == 2:
        thing.name = 'природного газа'
        thing.l = 44*10**6
    elif thing.name == 3:
        thing.name = 'сухих дров'
        thing.l = 10**7
    elif thing.name == 4:
        thing.name = 'торфа'
        thing.l = 14*10**6
    elif thing.name == 5:
        thing.name == 'древесного угля'
        thing.l = 34*10**76
    if thing.second_name == 1:
        thing.second_name = 'воды'
        thing.c = 4200
        thing.max_t = 100
        max_t2 = 23*10**5
        thing.min_t = randint(0, 99)
    elif thing.second_name == 2:
        thing.second_name = 'железа'
        thing.c = 460
        thing.max_t = 1539
        thing.max_t2 = 27 * 10**4
        thing.min_t = randint(0, 1538)
    elif thing.second_name == 3:
        thing.second_name = 'золота'
        thing.c = 130
        thing.max_t = 1064
        thing.max_t2 = 67 * 10**3
        thing.min_t = randint(0, 1063)
    elif thing.second_name == 4:
        thing.second_name = 'алюминия'
        thing.c = 920
        thing.max_t = 660
        thing.max_t2 = 39 * 10**4
        thing.min_t = randint(0, 659)
    elif thing.second_name == 5:
        thing.second_name = 'меди'
        thing.c = 400
        thing.max_t = 1085
        thing.max_t2 = 21 * 10**4
        thing.min_t = randint(0, 1084)

    if thing.second_name == 'воды':
        welcome_text.setText('Сколько потребуется ' + thing.name + ' для кипичения и параобразовния воды и с начальной температурой ' + str(thing.min_t) + ' градусов цельсия и массой ' + str(thing.m) + ' кг. При надобности, округлите ответ до сотен, даже если он будт равен 0.00')
    else:
        welcome_text.setText('Сколько потребуется ' + str(thing.name) + ' для плавления ' + str(thing.second_name) + ' с начальной температурой ' + str(thing.min_t) + ' градусов цельсия и массой ' + str(thing.m) + ' кг. При надобности, округлите ответ до сотен, даже если он будт равен 0.00')

def p_type4():
    global thing
    Line_Tag.show()
    btn.show()
    begin_btn1.hide()
    begin_btn2.hide()
    btn.setText('Проверить')
    thing = Item('', "", 4200, randint(50, 99), 0, randint(0, 50), randint(1, 10), randint(1 ,10), 0, 0, 4, 0)
    thing.max_t2 = round((thing.min_t*thing.m + thing.max_t*thing.l)/(thing.m+thing.l))
    welcome_text.setText('В воду с температурой ' + str(thing.min_t) + ' градусов и объёмом ' + str(thing.m) + ' литров добавили ещё воды объёмом ' + str(thing.l) + " литров и температурой " + str(thing.max_t) + "градусов. Найдите новую температуру, ответ при надобности округлите до целого числа.")    

def show_result():
    RadioGroupBox.hide()
    ResultGroup.show()
    btn.setText('Следующий вопрос')

def show_quest():
    ResultGroup.hide()
    RadioGroupBox.show()
    btn.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_correct(res):
    resu.setText(res)
    right_ans.setText(q_list[main_win.cur_quest].right)
    show_result()

def click_ok():
    if btn.text() == 'Ответить':
        check_ans()
    elif btn.text() == 'Следующий вопрос':
        next_quest()
    elif btn.text() == 'Проверить':
        check_p_ans()
    elif btn.text() == 'Новая задача':
        if thing.type == 1:
            p_type1()
        elif thing.type == 2:
            p_type2()
        elif thing.type == 4:
            p_type4()
        Line_Tag.clear()
    elif btn.text() == 'Следующая задача':
        if queue[0] == '1':
            p_type1()
            queue.remove("1")
        elif queue[0] == '2':
            p_type2()
            queue.remove("2")
        elif queue[0] == '4':
            p_type4()
            queue.remove('4')

    else:
        btn.hide()
        begin_btn1.show()
        begin_btn1.setText('Теория')
        begin_btn2.show()
        begin_btn2.setText('Практика')
        welcome_text.setText('Решу ФИЗИКУ!')

def ask(q):
    shuffle(answer)
    answer[0].setText(q.right)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    welcome_text.setText(q.question)
    show_quest()

def check_ans():
    if answer[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
    else:
        show_correct('Неправильно!')

def next_quest():
    if main_win.cur_quest < len(q_list) - 1:
        main_win.cur_quest += 1
        q = q_list[main_win.cur_quest]
        ask(q)
    else:
        test_score()

def test_score():
    ResultGroup.hide()
    RadioGroupBox.hide()
    welcome_text.show()
    welcome_text.setText('Ты набрал ' + str(main_win.score) + ' из ' + str(len(q_list)))
    btn.setText('Вернуться на главный экран')
    main_win.cur_quest = -1
    main_win.score = 0


#Лэйауты
main_layout.addWidget(welcome_text, alignment = Qt.AlignCenter)
main_layout.addLayout(theory_layout)
main_layout.addLayout(group_layout)
main_layout.addLayout(line_layout)
main_layout.addLayout(button_layout)
main_layout.addLayout(music_layout)
#music_layout.addWidget(music_btn)
theory_layout.addWidget(theory_text)
theory_layout.addWidget(list_theme)
line_layout.addWidget(Line_Tag)
group_layout.addWidget(group_box)
button_layout.addWidget(begin_btn1)
button_layout.addWidget(begin_btn2)
button_layout.addWidget(btn)
group_layout.addWidget(RadioGroupBox)
group_layout.addWidget(ResultGroup)

#Первой группы теста
layout_b2.addWidget(rbtn1)
layout_b2.addWidget(rbtn2)
layout_b3.addWidget(rbtn3)
layout_b3.addWidget(rbtn4)
layout_b1.addLayout(layout_b2)
layout_b1.addLayout(layout_b3)
RadioGroupBox.setLayout(layout_b1)
#Второй группы теста
layout_2b.addWidget(resu)
layout_2b.addWidget(right_ans, alignment = Qt.AlignCenter)
ResultGroup.setLayout(layout_2b)
#Выбор темы
b3_layout2.addWidget(theme1)
b3_layout2.addWidget(theme2)
b3_layout1.addWidget(theme3)
b3_layout1.addWidget(theme4)
b3_layout3.addLayout(b3_layout2)
b3_layout3.addLayout(b3_layout1)
group_box.setLayout(b3_layout3)

#Нажатия на кнопки
list_theme.itemPressed.connect(add_text)
btn.clicked.connect(click_ok)
begin_btn1.clicked.connect(check_screen1)
begin_btn2.clicked.connect(check_screen2)

#Финал
main_win.setLayout(main_layout)
main_win.show()
app.exec_()