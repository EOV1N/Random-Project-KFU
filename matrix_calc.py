from tkinter import *

def open_interface():
    def hea():
        a1 = cell1.get()
        a2 = cell2.get()
        a3 = cell3.get()
        b1 = cell4.get()
        b2 = cell5.get()
        b3 = cell6.get()
        c1 = cell7.get()
        c2 = cell8.get()
        c3 = cell9.get()
        detPart1 = int(a1)*int(b2)*int(c3) + int(a3)*int(b1)*int(c2) + int(a2)*int(b3)*int(c1)
        detPart2 = int(a3)*int(b2)*int(c1) + int(a2)*int(b1)*int(c3) + int(a1)*int(b3)*int(c2)
        detA = detPart1 - detPart2
        labe.configure(text = detA)
    calc = ''
    newWindow = Toplevel(calc)
    cell1 = Entry(newWindow, font='Arial 10', width = '5')
    cell1.place(x=1, y=1)
    cell2 = Entry(newWindow, font="Arial 10", width = '5')
    cell2.place(x=50, y=1)
    cell3 = Entry(newWindow, font="Arial 10", width = '5')
    cell3.place(x=100, y = 1)
    cell4 = Entry(newWindow, font="Arial 10", width = '5')
    cell4.place(x=1, y = '30')
    cell5 = Entry(newWindow, font="Arial 10", width = '5')
    cell5.place(x=50, y = '30')
    cell6 = Entry(newWindow, font="Arial 10", width = '5')
    cell6.place(x=100, y = '30')
    cell7 = Entry(newWindow, font="Arial 10", width = '5')
    cell7.place(x=1, y = '60')
    cell8 = Entry(newWindow, font="Arial 10", width = '5')
    cell8.place(x=50, y = '60')
    cell9 = Entry(newWindow, font="Arial 10", width = '5')
    cell9.place(x=100, y = '60')
    buttik = Button(newWindow, text = 'Вычислить detA.', bg = 'red', bd = '5', font = 'Arial 12', command = hea)
    buttik.place(x=10, y=120)
def matrix2x2():
    def hea():
        a1 = cell1.get()
        a2 = cell2.get()
        b1 = cell3.get()
        b2 = cell4.get()
        detA = int(a1)*int(b2) - int(a2)*int(b1)
        labe.configure(text = detA)
    calc = ''
    newWindow = Toplevel(calc)
    cell1 = Entry(newWindow, font='Arial 10', width = '5')
    cell1.place(x=1, y=1)
    cell2 = Entry(newWindow, font="Arial 10", width = '5')
    cell2.place(x=50, y=1)
    cell3 = Entry(newWindow, font="Arial 10", width = '5')
    cell3.place(x=1, y = 30)
    cell4 = Entry(newWindow, font="Arial 10", width = '5')
    cell4.place(x=50, y = 30)
    buttik = Button(newWindow, text = 'Вычислить detA.', bg = 'red', bd = '5', font = 'Arial 12', command = hea)
    buttik.place(x=10, y=60)

def reference():
    a = var.get()
    if a == 0:
        open_interface()
    elif a ==1:
        matrix2x2()

root = Tk()
root.title('Калькулятор матриц.')

main_label1 = Label(text = 'Размерность матрицы:', font = 'Arial 12')
main_label1.pack()

var = IntVar()
var.set(1)
rad0 = Radiobutton(text = 'Матрица 3x3', variable = var, value = 0)
rad0.pack()
rad1 = Radiobutton(text = 'Матрица 2x2', variable = var, value = 1)
rad1.pack()
but = Button(text = 'Открыть интерфейс.', bg = 'red', font = 'Arial 18', command = reference)
but.pack()

labe = Label(text = 'Определитель:', bg = 'beige', font = 'Arial 16')
labe.pack()

root.mainloop()