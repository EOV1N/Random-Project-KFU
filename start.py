from tkinter import *
from math import *


def calculate():
    a = int(ent1.get())
    b = int(ent2.get())
    ab = pow(a, b)
    c = int(ab)
    lbl1.configure(text = c)


root = Tk()
root.title('Калькулятор степеней')

main_label1 = Label(text = 'Число:', font = 'Arial 12')
main_label1.pack()

ent1 = Entry(bg = 'beige', font = 'Arial 20')
ent1.pack()

main_label2 = Label(text = 'Степень:', font = 'Arial 12')
main_label2.pack()

ent2 = Entry(bg = 'beige', font = 'Arial 20')
ent2.pack()

but1 = Button(text = 'Вычислить!', bg = 'red', bd = '5', font = 'Arial 18', command = calculate) #команда активируетсч кнопкой
but1.pack()

lbl1 = Label(text = 'Здесь появится ответ.', font = 'Arial 14')
lbl1.pack()

root.mainloop()