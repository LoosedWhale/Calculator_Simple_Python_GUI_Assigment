from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(False, False)

#The input box at the top of the calculator. e is short for entry, the varible is used allot so the shorter the better in this case.
e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#e.insert(0, "")
#Gets the current number that is clicked/ the button pressed
#Clears the entry box when a new function or number is enterd
def buttonClick(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

#When a button is clicked with this function it clears the entry box
def buttonClear():
    e.delete(0, END)

#Takes the first number that is inputed by the user.
#With this number is stored so that a function can be called such as devision, then another number.
#If onther function is not called between the two number inputs addition is applied by deafualt.
def buttonAdd():
    firstNumber = e.get()
    global fNum
    global math
    math = "addition"
    fNum = int(firstNumber)
    e.delete(0, END)

#A function like the additon but for substraction
#Same code as above. Only diffrence is what the math varible is equal to.
#Sofia I know I should not use global but it saved time and in this case very useful :)
#The subsraction itselfs happens in the eqaul funnction, this is a way of stroing the values and to a button so that the eqaul function can check what the user wants.
def buttonSubtract():
    firstNumber = e.get()
    global fNum
    global math
    math = "subtraction"
    fNum = int(firstNumber)
    e.delete(0, END)


#Same code as the additon and subsraction only diffrence is that math is eqaul to multiplication.
def buttonMultiply():
    firstNumber = e.get()
    global fNum
    global math
    math = "multiplication"
    fNum = int(firstNumber)
    e.delete(0, END)

#Same code as the additon and subsraction only diffrence is that math is eqaul to division.
def buttonDivide():
    firstNumber = e.get()
    global fNum
    global math
    math = "division"
    fNum = int(firstNumber)
    e.delete(0, END)



#Gets the second inputed number after a function has been called.
#Also checks which function that was called
#Gets the fNum (first number) and applies the function (example subsraction or multiplication) and then adds that to the second number.
def buttonEqual():
    secondNumber = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, fNum + int(secondNumber))

    if math == "subtraction":
        e.insert(0, fNum - int(secondNumber))

    if math == "multiplication":
        e.insert(0, fNum * int(secondNumber))

    if math == "division":
        e.insert(0, fNum / int(secondNumber))

# Define Buttons
#Assigenst a button to a text and command
#lambda is used so that a function can use; example functionName()
#Instead of tkinters deafult of just the functionName
#Makes the code able to use one function with multiple assigend values
#Aka makes the code SOOOOOOOOOOOOOO much easier
#I think I love lambda for this <3

#Yea I know that I'm using numbers in the varible name but it makes it so much cleaner, show some mercy :)
#button 0 to 9

button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonClick(0))

#Math function keys

buttonAdd = Button(root, text="+", padx=39, pady=20, command=buttonAdd)
buttonEqual = Button(root, text="=", padx=86, pady=20, command=buttonEqual)
buttonClear = Button(root, text="Clear", padx=77, pady=20, command=buttonClear)
buttonSubtract = Button(root, text="- ", padx=39, pady=20, command=buttonSubtract)
buttonMultiply = Button(root, text="*", padx=40, pady=20, command=buttonMultiply)
buttonDivide = Button(root, text="/", padx=40, pady=20, command=buttonDivide)

#Places the buttons on the screen in a grid like way
#Makes it less painful then .pack
#pack is a bit cringe honestly #packIsCringe  #gridForTheWin

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)
buttonClear.grid(row=4, column=1, columnspan=2)
buttonAdd.grid(row=5, column=0)
buttonEqual.grid(row=5, column=1, columnspan=2)

buttonSubtract.grid(row=6, column=0)
buttonMultiply.grid(row=6, column=1)
buttonDivide.grid(row=6, column=2)

#This fella right here makes the code work, we like this one. <3
root.mainloop()



#Note to Sofia
#Koden är inte 100% min då jag följde en youtube tutarial som jag kommer länka till.
#Men ändrade såklart om i koden och annpassade den för detta arbete/skrev den själv men kollade på hur jag bäst skulle göra visa functioner.
#https://youtu.be/YXPyB4XeYLA?t=2460 länken till video jag följde.
#Ps hoppas att du förstår :)
