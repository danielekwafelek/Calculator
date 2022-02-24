from tkinter import *
global afterEqual
afterEqual = 0

root = Tk()
root.title("Calculator")
root.geometry("290x330")

screen = Entry(root, borderwidth=5, font = "Helvetica 20 bold")
screen.place(width=210, height=80, x=5, y=5)

def buttonClick(number):
    current = screen.get()
    screen.delete(0, END)
    screen.insert(0, str(current) + str(number))

def buttonAdd():
    global clickedAdd
    global fNum
    if afterEqual !=0:
        fNum = float(afterEqual)
        screen.delete(0, End)
        global math
        math = "adding"
    else:
        firstNumber = screen.get()
        fNum = float(firstNumber)
        screen.delete(0, END)
        math = "adding"

def buttonTimes():
    global clickedTime
    global fNum
    if afterEqual !=0:
        fNum = float(afterEqual)
        screen.delete(0, End)
        global math
        math = "timing"
    else:
        firstNumber = screen.get()
        fNum = float(firstNumber)
        screen.delete(0, END)
        math = "timing"

def buttonDivide():
    global clickedDivide
    global fNum
    if afterEqual !=0:
        fNum = float(afterEqual)
        screen.delete(0, End)
        global math
        math = "dividing"
    else:
        firstNumber = screen.get()
        fNum = float(firstNumber)
        screen.delete(0, END)
        math = "dividing"

def buttonSubstract():
    global clickedSubstract
    global fNum
    if afterEqual !=0:
        fNum = float(afterEqual)
        screen.delete(0, End)
        global math
        math = "substracting"
    else:
        firstNumber = screen.get()
        fNum = float(firstNumber)
        screen.delete(0, END)
        math = "substracting"

def buttonUndo():
    screen.delete(len(screen.get())-1,END)

def buttonDelete():
    return none

def buttonEqual():
    secondNumber = screen.get()
    global sNum
    sNum = float(secondNumber)
    screen.delete(0, END)
    global equalTo
    if math == "adding":
        equalTo = fNum + sNum
        screen.insert(0, equalTo)
    elif math == "timing":
        equalTo = fNum * sNum
        screen.insert(0, equalTo)
    elif math == "dividing":
        equalTo = fNum / sNum
        screen.insert(0, equalTo)
    elif math == "substracting":
        equalTo = fNum - sNum
        screen.insert(0, equalTo)
    afterEqual = equalTo


button0 = Button(root, text="0", command=lambda: buttonClick(0))
button1 = Button(root, text="1", command=lambda: buttonClick(1))
button2 = Button(root, text="2", command=lambda: buttonClick(2))
button3 = Button(root, text="3", command=lambda: buttonClick(3))
button4 = Button(root, text="4", command=lambda: buttonClick(4))
button5 = Button(root, text="5", command=lambda: buttonClick(5))
button6 = Button(root, text="6", command=lambda: buttonClick(6))
button7 = Button(root, text="7", command=lambda: buttonClick(7))
button8 = Button(root, text="8", command=lambda: buttonClick(8))
button9 = Button(root, text="9", command=lambda: buttonClick(9))
buttonTimes = Button(root, text="x", command=buttonTimes)
buttonDivide = Button(root, text="/", command=buttonDivide)
buttonAdd = Button(root, text="+", command=buttonAdd)
buttonSubstract = Button(root, text="-", command=buttonSubstract)
buttonEqual = Button(root, text="=", command=buttonEqual)
buttonUndo = Button(root, text = "<-", command=buttonUndo)
buttonDelete = Button(root, text = "DEL", command = buttonDelete)


button0.place(width=72.5, height=60, x=72.5, y=270)
button1.place(width=72.5, height=60, y=210)
button2.place(width=72.5, height=60, x=72.5, y=210)
button3.place(width=72.5, height=60, x=145, y=210)
button4.place(width=72.5, height=60, y=150)
button5.place(width=72.5, height=60, x=72.5, y=150)
button6.place(width=72.5, height=60, x=145, y=150)
button7.place(width=72.5, height=60, y=90)
button8.place(width=72.5, height=60, x=72.5, y=90)
button9.place(width=72.5, height=60, x=145, y=90)
buttonTimes.place(width=72.5, height=60, x=217.5, y=90)
buttonDivide.place(width=72.5, height=60, x=217.5, y=30)
buttonAdd.place(width=72.5, height=60, x=217.5, y=210)
buttonSubstract.place(width=72.5, height=60, x=217.5, y=150)
buttonEqual.place(width=72.5, height=60, x=217.5, y=270)
buttonUndo.place(width=72.5, height=60, x=145, y=270)
buttonDelete.place(width=72.5, height=60, y=270)


root.mainloop()
