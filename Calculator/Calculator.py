from tkinter import *
global afterEqual
afterEqual = 0

root = Tk()
root.title("Calculator")
root.geometry("219x319")

screen = Entry(root, width=20, borderwidth=5)
screen.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

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


button0 = Button(root, text="0", padx=20, pady=20, command=lambda: buttonClick(0))
button1 = Button(root, text="1", padx=20, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=20, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=20, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=20, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=20, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=20, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=20, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=20, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=20, pady=20, command=lambda: buttonClick(9))
buttonTimes = Button(root, text="x", padx=20, pady=20, command=buttonTimes)
buttonDivide = Button(root, text="/", padx=20, pady=20, command=buttonDivide)
buttonAdd = Button(root, text="+", padx=20, pady=20, command=buttonAdd)
buttonSubstract = Button(root, text="-", padx=20, pady=20, command=buttonSubstract)
buttonEqual = Button(root, text="=", padx=20, pady=20, command=buttonEqual)


button0.grid(row=4, column=1)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
buttonTimes.grid(row=1, column=3)
buttonDivide.grid(row=0, column=3)
buttonAdd.grid(row=3, column=3)
buttonSubstract.grid(row=2, column=3)
buttonEqual.grid(row=4, column=3)


root.mainloop()
