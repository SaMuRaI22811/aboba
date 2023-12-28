#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QRadioButton,  
        QPushButton, QLabel, QButtonGroup)
from random import shuffle, randint
app = QApplication([])
main_win = QWidget()
main_win.resize(400,300)
main_win.setWindowTitle('Memory Card')
radio_box = QGroupBox('Варианты ответов')
a = QLabel('какой национальности не существует')
b = QRadioButton('Энцы')
c = QRadioButton('Чулымцы')
d = QRadioButton('Смурфы')
e = QRadioButton('Алеуты')
class Question():
        def __init__(self,question,wrong1,wrong2,wrong3,right_answer):
                self.question = question
                self.wrong1 = wrong1
                self.wrong2 = wrong2
                self.wrong3 = wrong3
                self.right_answer = right_answer
question_list = [Question('какой деревни не существует?','Алеуты','Чулымцы','Энцы','Смурфы'),
Question('на каком языке мы говорим?','на английском','на беларуском','на португальском','на русском'),
Question('какие у нас деньги?','USTD','RUB','UAH','BYN'),
Question('кто я?','дима','ваня','баня','матвей'),
Question('где мы учимся програмированию','стэпик','авиасейлс','изучалово.by','algoritmika')]
main_win.total = len(question_list)
def next_question():
        if len(question_list) > 0:
                quest = randint(0,len(question_list) - 1)
                q = question_list[quest]
                question_list.pop(quest)
                ask(q)
        else:
                print(f'Всего вопросов: {main_win.total}')
                print(f'правильных ответов: {main_win.score}')
                print(f'прогресс:',(main_win.score / main_win.total) * 100,'%')
radio_group = QButtonGroup()
radio_group.addButton(b)
radio_group.addButton(c)
radio_group.addButton(d)
radio_group.addButton(e)
g = QPushButton('ответить')
def click_OK():
        if g.text() == 'ответить':
                check_answer()
        else:
                next_question()

an1 = QHBoxLayout()
an2 = QVBoxLayout()
an3 = QVBoxLayout()
an2.addWidget(b)
an2.addWidget(d)
an3.addWidget(c)
an3.addWidget(e)
an3.addWidget(g)
an1.addLayout(an2)
an1.addLayout(an3)
radio_box.setLayout(an1)
ans_box = QGroupBox('Результаты теста')
lb_result = QLabel('правильно/неправильно')
lb_correct = QLabel('правильный ответ')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct,alignment=Qt.AlignCenter)
ans_box.setLayout(layout_res)



lay1 = QHBoxLayout()
lay2 = QHBoxLayout()
lay3 = QHBoxLayout()

lay1.addWidget(a,alignment=(Qt.AlignLeft | Qt.AlignTop))
lay2.addWidget(radio_box)
lay2.addWidget(ans_box)
radio_box.hide()
lay3.addWidget(g, stretch=2)
layout_card = QVBoxLayout()
layout_card.addLayout(lay1)
layout_card.addLayout(lay2)
layout_card.addLayout(lay3)
main_win.setLayout(layout_card)
def show_result():
        radio_box.hide()
        ans_box.show()
        g.setText('следующий вопрос')
def show_question():
        radio_box.show()
        ans_box.hide()
        g.setText('ответить')
        radio_group.setExclusive(False)
        b.setChecked(False)
        c.setChecked(False)
        d.setChecked(False)
        e.setChecked(False)
        radio_group.setExclusive(True)
answers = [b,c,d,e]
main_win.score = 0
def ask(q):
        shuffle(answers)
        answers[0].setText(q.right_answer)
        answers[1].setText(q.wrong1)
        answers[2].setText(q.wrong2)
        answers[3].setText(q.wrong3)
        a.setText(q.question)
        lb_correct.setText(q.right_answer)
        show_question()
def show_correct(res):
        lb_result.setText(res)
        show_result()
def check_answer():
        if answers[0].isChecked():
                show_correct('Правильно')
                main_win.score += 1
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
                show_correct('НЕПРАВИЛЬНО!!!\nправильный ответ:')
next_question()
g.clicked.connect(click_OK)
main_win.show()
app.exec()