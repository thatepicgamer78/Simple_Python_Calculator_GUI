from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Calculator")
window.resizable(False, False)

icon = PhotoImage(file="favicon.png")
window.iconphoto(True, icon)
window.config(background="purple")

def clearNumPressed():
    global bo1
    global bo2
    global op
    currentNum.config(text="0")
    bo1 = 0
    bo2 = 0
    op = "0"

def Num9Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="9")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "9")

def Num8Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="8")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "8")

def Num7Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="7")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "7")

def Num6Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="6")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "6")

def Num5Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="5")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "5")

def Num4Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="4")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "4")

def Num3Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="3")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "3")

def Num2Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="2")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "2")

def Num1Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="1")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "1")

def Num0Pressed():
    if currentNum.cget("text") in ("0", "+", "-", "*", "/"):
        currentNum.config(text="0")
    else:
        if len(currentNum.cget("text")) != 26:
            currentNum.config(text=currentNum.cget("text") + "0")

bo1 = 0 
bo2 = 0
op = "0"

def PlusPressed():
    global bo1
    global bo2
    global op
    bo1 = int(currentNum.cget("text"))
    op = "+"
    currentNum.config(text="+")

def MinusPressed():
    global bo1
    global bo2
    global op
    bo1 = int(currentNum.cget("text"))
    op = "-"
    currentNum.config(text="-")

def MultiPressed():
    global bo1
    global bo2
    global op
    bo1 = int(currentNum.cget("text"))
    op = "*"
    currentNum.config(text="*")

def DividePressed():
    global bo1
    global bo2
    global op
    bo1 = int(currentNum.cget("text"))
    op = "/"
    currentNum.config(text="/")

def EnterPressed():
    global bo1
    global bo2
    global op
    bo2 = int(currentNum.cget("text"))
    if op == "+":
        result = str(bo1 + bo2)
        if len(result) <= 26:
            currentNum.config(text=result)
        else:
            currentNum.config(text="Error")
    elif op == "-":
        result = str(bo1 - bo2)
        if len(result) <= 26:
            currentNum.config(text=result)
        else:
            currentNum.config(text="Error")
    elif op == "*":
        result = str(bo1 * bo2)
        if len(result) <= 26:
            currentNum.config(text=result)
        else:
            currentNum.config(text="Error")
    elif op == "/":
        if bo2 == 0:
            currentNum.config(text="Error")
        else:
            result = str(bo1 / bo2)
            if len(result) <= 26:
                currentNum.config(text=result)
            else:
                currentNum.config(text="Error")



currentNum = Label(window, text="0", font=("Arial", 24), bg="purple", fg="white", relief=RAISED, bd=10, anchor="e")
currentNum.pack(fill=X, padx=5, pady=10)

Num9 = Button(window, text="9", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num9Pressed)
Num9.place(x=0, y=100, width=100, height=100)

Num8 = Button(window, text="8", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num8Pressed)
Num8.place(x=110, y=100, width=100, height=100)

Num7 = Button(window, text="7", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num7Pressed)
Num7.place(x=220, y=100, width=100, height=100)

Num6 = Button(window, text="6", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num6Pressed)
Num6.place(x=0, y=210, width=100, height=100)

Num5 = Button(window, text="5", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num5Pressed)
Num5.place(x=110, y=210, width=100, height=100)

Num4 = Button(window, text="4", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num4Pressed)
Num4.place(x=220, y=210, width=100, height=100)

Num3 = Button(window, text="3", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num3Pressed)
Num3.place(x=0, y=320, width=100, height=100)

Num2 = Button(window, text="2", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num2Pressed)
Num2.place(x=110, y=320, width=100, height=100)

Num1 = Button(window, text="1", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num1Pressed)
Num1.place(x=220, y=320, width=100, height=100)

Num0 = Button(window, text="0", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=Num0Pressed)
Num0.place(x=110, y=430, width=100, height=50)

clearNum = Button(window, text="Clear", font=("Arial", 14), bg="#242424", fg="white", relief=RAISED, bd=10, command=clearNumPressed)
clearNum.place(x=0, y=430, width=100, height=50)

charPlus = Button(window, text="+", font=("Arial", 24), bg="#242424", fg="white", relief=RAISED, bd=10, command=PlusPressed)
charPlus.place(x=330, y=100, width=100, height=100)

charMinus = Button(window, text="-", font=("Arial", 24), bg="#242424", fg="white", relief=RAISED, bd=10, command=MinusPressed)
charMinus.place(x=330, y=210, width=100, height=100)

charMulti = Button(window, text="*", font=("Arial", 24), bg="#242424", fg="white", relief=RAISED, bd=10, command=MultiPressed)
charMulti.place(x=330, y=320, width=100, height=100)

charDivide = Button(window, text="/", font=("Arial", 24), bg="#242424", fg="white", relief=RAISED, bd=10, command=DividePressed)
charDivide.place(x=220, y=430, width=100, height=50)

EnterNum = Button(window, text="=", font=("Arial", 24), bg="#242424", fg="white", relief=RAISED, bd=10, command=EnterPressed)
EnterNum.place(x=330, y=430, width=100, height=50)


window.mainloop()
