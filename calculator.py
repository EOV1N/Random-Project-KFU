from tkinter import *


def data():
    main = int(x.get())
    second = int(n.get())
    write = main**second
    lbl1.configure(text=write)

root = Tk()
root.title('Вычислитель')
root.geometry('450x140')
mainlabel = Label(text='Возведение числа X в степень N.', font='Arial 20')
mainlabel.pack()
x = Entry(root)
x.pack()
n = Entry(root)
n.pack()
lbl1 = Label(text='Неактивно.', bg='cyan', font='Arial 14')
lbl1.pack()
update_button = Button(text='Вычислить.', command=data, fg='black', bg='beige', bd='3')
update_button.pack()
ulbl1 = Label(text='Число Х:')
ulbl1.place(relx=0.305, rely=0.33, anchor='c')
ulbl2 = Label(text='Число N:')
ulbl2.place(relx=0.305, rely=0.48, anchor='c')

root.mainloop()
