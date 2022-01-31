# Mert Gulsen
# This application was made in 2018

from tkinter import *

# application frames

window = Tk()

frame = Frame(window)
frame.pack(side=TOP)

center_frame = Frame(window)
center_frame.pack()

bottom_frame = Frame(window)
bottom_frame.pack(side=BOTTOM)


# changing title and icon
window.title("Prime Numbers")
p1 = PhotoImage(file="pi-icon.png")
window.iconphoto(False, p1)


# size
window.geometry("400x400+750+300")
window.resizable(False, False)


# number inputs
data = Entry(frame)
data1 = Entry(frame)
data2 = Entry(frame)


def summon_prime():  # create prime calculator on window
    button1_1.pack_forget()
    button1_2.pack_forget()
    data.pack(pady="50")
    label.pack()
    button2.pack(pady="50")
    button3.pack(side=LEFT, pady=50)
    button4.pack_forget()
    button4.pack(side=LEFT, pady=50)


def summon_relatively_prime():  # create relatively prime calculator on window
    button1_1.pack_forget()
    button1_2.pack_forget()
    data1.pack(side=LEFT, padx=10, pady=20)
    data2.pack(side=LEFT, padx=10, pady=20)
    label2.pack()
    button2_1.pack(side=TOP, pady=50)
    button3.pack_forget()
    button3.pack(side=LEFT, pady=50)
    button4.pack_forget()
    button4.pack(side=LEFT, pady=50)


def summon_menu():  # summon main menu
    data.pack_forget()
    data1.pack_forget()
    data2.pack_forget()
    label2.pack_forget()
    button2_1.pack_forget()
    button2.pack_forget()
    label.pack_forget()
    button3.pack_forget()
    button1_1.pack(side=LEFT, padx=10, pady=75)
    button1_2.pack(side=LEFT, padx=10, pady=75)
    button4.pack_forget()
    button4.pack(pady=75)


def quitting():
    quit()


def relatively_prime():  # function for calculating relative primeness
    try:
        number1 = int(data1.get())
        number2 = int(data2.get())
        label2["fg"] = "black"
        if number1 < 0 or number2 < 0:
            label2["text"] = "Negative numbers can't be relatively prime"

        elif number1 == 0 or number2 == 0:
            label2["text"] = "0 can't be relatively prime"

        elif number1 == number2:
            label2["text"] = "Don't pick same numbers"

        elif number1 == 1 or number2 == 1:
            label2["text"] = "All numbers are relatively prime with 1"

        elif number1 == 2:
            if number2 % 2 == 0:
                label2["text"] = "They are not relatively prime"
            else:
                label2["text"] = "They are relatively prime"
        elif number2 == 2:
            if number1 % 2 == 0:
                label2["text"] = "They are not relatively prime"
            else:
                label2["text"] = "They are relatively prime"

        for i in range(2, number1):
            if number1 == number2:
                break
            if number1 % number2 == 0 or number2 % number1 == 0:
                label2["text"] = "They are not relatively prime"
                break
            elif number1 % i == 0:
                if number2 % i == 0:
                    label2["text"] = "They are not relatively prime"
                    break
            elif number1 % number2 != 0 and number2 % number1 != 0 and number1 == i + 1:
                label2["text"] = "They are relatively prime"
    except ValueError:
        label2["text"] = "Please enter a valid number"
        label2["fg"] = "red"


def prime():  # function for calculating primeness
    try:
        x = int(data.get())
        label["fg"] = "black"
        if x < 0:
            label["text"] = "Negative numbers can't be prime"
        elif x == 0 or x == 1:
            label["text"] = "Not prime"
        elif x == 2:
            label["text"] = "Prime"
        else:
            label["text"] = "Prime"
            for i in range(2, x//2+1):
                if x % i == 0:
                    label["text"] = "Not prime"
                    break
    except ValueError:
        label["text"] = "Please enter a valid number"
        label["fg"] = "red"


# define application buttons and attach functions to them

button1_1 = Button(master=frame, text="Test primeness", command=summon_prime)
button1_1.pack(side=LEFT, padx=10, pady=75)

button1_2 = Button(master=frame, text="Test relatively prime numbers", command=summon_relatively_prime)
button1_2.pack(side=LEFT, padx=10, pady=75)

button4 = Button(master=bottom_frame, text="Quit", command=quitting)
button4.pack(pady=75)

button2 = Button(master=center_frame, text="is prime ?", command=prime)

button2_1 = Button(master=bottom_frame, text="are relatively prime ?", command=relatively_prime)

label = Label(master=frame, text="Please enter a number")

label2 = Label(master=center_frame, text="Please enter 2 different numbers that you want")

button3 = Button(master=bottom_frame, text="Return to menu", command=summon_menu)

# main application loop
while True:
    window.update()
    mainloop()
