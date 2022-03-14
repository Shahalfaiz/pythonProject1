

from tkinter import *
def click(event):

    global scvalue



    text=event.widget.cget("text")


    if text=='=':

        if scvalue.get().isdigit():
            value=int(scvalue.get())

        else:
            value=eval(screen.get())
        scvalue.set(value)
        screen.update()

    elif text =='AC':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()


window = Tk()
window.geometry("500x500")
window.minsize(1000,1000)
window.maxsize(1500,1500)
window.config(bg="black")
window.title("calcuator by___> shahal")
window.attributes('-topmost',1)
window.resizable()
window.lift()


scvalue=StringVar()
scvalue.set("")
f=Frame(window, padx=20, pady=20)
screen=Entry(f, textvar=scvalue, font="shahal 50 italic underline bold", bg='orange', fg='green')
screen.pack(fill=X, padx=15, pady=15)
f.pack()




option1=["AC","0","/","="]
option2=["7","8","9","*"]
option3=["4","5","6","-"]
option4=["1","2","3","/"]

f=Frame(window, bg="black", padx=15, pady=15)
for i in option1:
    b=Button(f, text=i , padx=15 , pady=15 , font="shahal 50 bold italic")
    b.pack(side=LEFT, padx=15, pady=15)
    b.bind("<Button-1>", click)
f.pack()
f=Frame(window,bg="black", padx=15, pady=15)
for i in option2:
    b=Button(f, text=i , padx=15 , pady=15 , font="shahal 50 bold italic")
    b.pack(side=LEFT, padx=15, pady=15)
    b.bind("<Button-1>", click)


f.pack()
f = Frame(window, bg="black", padx=15, pady=15)
for i in option3:
    b = Button(f, text=i, padx=15, pady=15, font="shahal 50  bold italic")
    b.pack(side=LEFT, padx=15, pady=15)
    b.bind("<Button-1>", click)

f.pack()
f = Frame(window, bg="black", padx=15, pady=15)
for i in option4:
    b = Button(f, text=i, padx=15, pady=15, font="shahal 50 bold italic")
    b.pack(side=LEFT, padx=15, pady=15)
    b.bind("<Button-1>", click)

f.pack()
window.mainloop()