from turtle import title
from flask import Flask, render_template 
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    current_hour = datetime.now()

    if  current_hour.hour in range(6,11):
        strHi = 'Доброе утро!'
    elif current_hour.hour in range(12,17):
        strHi = 'Добрый день!'
    elif current_hour.hour in range(18,22) :
        strHi = 'Добрый вечер!'
    else:
        strHi = 'Доброй ночи!'

    return render_template('index.html', title2=strHi)

@app.route('/secondPage')
def secondPage():
    list_ready = ['Основы программирования','Контроль версий Git','Язык программирования C#','Буткемп']
    return render_template('secondPage.html', title='Пройденный материал', list_addon=list_ready,
        title2='Пройденный материал')


@app.route('/thirdPage')
def thirdPage():
    list_addon = ['Знакомство с языком Python (лекции)','Знакомство с языком Python (семинары)','Исключения в программировании и их обработка (лекции)','Исключения в программировании и их обработка (семинары)']
    return render_template('secondPage.html', title='Изучаемый материал', list_addon=list_addon,
        title2 = "Изучаемый материал")


if __name__ == '__main__':
    app.run()
