from tkinter import *
from tkinter import ttk 
from tkinter.ttk import Checkbutton
import tkinter.messagebox as mb
from tkinter.ttk import Combobox


window = Tk()
window.title("Назаров Яков Александрович УБ-22")
window.geometry('470x200') 

tab_control = ttk.Notebook(window)


tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Calculator')

def vichisleniya():
    a=combo.get()
    b=int(txt1.get())
    c=int(txt2.get())
    if a == '-':
        l=b-c
        lbl.configure(text=l)
    elif a == '+':
        l=b+c
        lbl.configure(text=l)
    elif a == '*':
        l=b*c
        lbl.configure(text=l)
    elif a== '/':
        l=b/c
        lbl.configure(text=l)


txt1 = Entry(tab1, justify=CENTER,  font=("Times New Romane", 30))
txt1.place(x = 10, y = 60, width=100, height=50,)

combo = Combobox(tab1, font=("Times New Romane", 20))
combo.place(x=120, y = 65, width=50, height=40)
combo['values'] = ('+', '-', '*', '/')

txt2 = Entry(tab1, justify=CENTER,  font=("Times New Romane", 30))
txt2.place(x = 180, y = 60, width=100, height=50)

btn1 = Button(tab1, text="=", font=("Times New Romane", 30), command=vichisleniya)
btn1.place(x=290, y = 65, width=50, height=40)

lbl = Label(tab1, text="", font=("Times New Romane", 30))
lbl.place(x=350, y = 60, width=100, height=50 )


tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text='Checkbox')

def clicked():
    a=chk_state1.get()
    if a == True:
        mb.showinfo('Info', 'Выбран первый вариант!')
    b=chk_state2.get()
    if b == True:
        mb.showinfo('Info', 'Выбран второй вариант!')
    c=chk_state3.get()
    if c == True:
        mb.showinfo('Info', 'Выбран третий вариант!')
    if a != True and b != True and c!= True:
        mb.showwarning('Предупреждение', ' Вы не выбрали ни один вариант ответа!!!')   

chk_state1 = BooleanVar()
chk_state1.set(0) 
chk1 = Checkbutton(tab2, text='Первый', var=chk_state1, onvalue=1, offvalue=0,)
chk1.grid(column=2, row=0)

chk_state2 = BooleanVar()
chk_state2.set(0) 
chk2 = Checkbutton(tab2, text='Второй', var=chk_state2, onvalue=1, offvalue=0)
chk2.grid(column=3, row=0) 

chk_state3 = BooleanVar()
chk_state3.set(0) 
chk3 = Checkbutton(tab2, text='Третий', var=chk_state3, onvalue=1, offvalue=0)
chk3.grid(column=4, row=0) 

btn = Button(tab2, text="Готово", command=clicked)
btn.grid(column=5, row=0)


tab3 = ttk.Frame(tab_control)
tab_control.add(tab3,text="Text")
lb3=ttk.Label(tab3)
tab_control.pack(expand=1,fill="both")
my_text = Text(tab3, width=60, height=20)
my_text.pack(pady=20)

def f():
    with open('Copy.txt') as f:
        z=""
        for line in f.readlines():
            z+=line
        lbl5.configure(text=z)
btn5 = Button(tab3, text="Копировать из...", font=("Times New Romane", 30), command=f)
btn5.place(x=0, y = 0, width=30, height=60)
lbl5 = Label(tab3, text='', font=("Times New Romane", 30))
lbl5.place(x=0, y = 0, width=30, height=60)

window.mainloop()
