import tkinter
from tkinter import Tk, Button, Label
from tkinter import messagebox

# global variables
state = 0
count = 0

# Screen
screen = Tk()
screen.title("Tic-Tac_Toe Game")
screen.config(width=350, height=400, background='#800000')

# Label
label = Label(text='Ready...', font=('Arial', 20, 'bold'), background='#800000')
label.grid(row=0, column=1)


# Logic
def win():
    if button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or \
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or \
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or \
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or \
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or \
            button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or \
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or \
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X':
        disable_buttons()
        label.config(text='Winner', foreground='green')
        messagebox.showinfo('Congratulations', "X Wins")

    # O WIns
    elif button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or \
            button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or \
            button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or \
            button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or \
            button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or \
            button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or \
            button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or \
            button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O':
        disable_buttons()
        label.config(text='Winner', foreground='red')
        messagebox.showinfo('Congratulations', "O Wins")

    # Draw
    elif count == 9:
        disable_buttons()
        label.config(text="Tie", foreground='black')
        messagebox.showinfo('Oh', "It's a Draw!")


def x_and_o(x):
    global state, count
    if state == 0:
        if x == 0:
            button1.config(text='X')
            button1["state"] = tkinter.DISABLED
        if x == 1:
            button2.config(text='X')
            button2["state"] = tkinter.DISABLED
        if x == 2:
            button3.config(text='X')
            button3["state"] = tkinter.DISABLED
        if x == 3:
            button4.config(text='X')
            button4["state"] = tkinter.DISABLED
        if x == 4:
            button5.config(text='X')
            button5["state"] = tkinter.DISABLED
        if x == 5:
            button6.config(text='X')
            button6["state"] = tkinter.DISABLED
        if x == 6:
            button7.config(text='X')
            button7["state"] = tkinter.DISABLED
        if x == 7:
            button8.config(text='X')
            button8["state"] = tkinter.DISABLED
        if x == 8:
            button9.config(text='X')
            button9["state"] = tkinter.DISABLED
        state = 1
        count += 1
        label.config(text="O's Turn", foreground='red')

    elif state == 1:
        if x == 0:
            button1.config(text='O')
            button1["state"] = tkinter.DISABLED
        if x == 1:
            button2.config(text='O')
            button2["state"] = tkinter.DISABLED
        if x == 2:
            button3.config(text='O')
            button3["state"] = tkinter.DISABLED
        if x == 3:
            button4.config(text='O')
            button4["state"] = tkinter.DISABLED
        if x == 4:
            button5.config(text='O')
            button5["state"] = tkinter.DISABLED
        if x == 5:
            button6.config(text='O')
            button6["state"] = tkinter.DISABLED
        if x == 6:
            button7.config(text='O')
            button7["state"] = tkinter.DISABLED
        if x == 7:
            button8.config(text='O')
            button8["state"] = tkinter.DISABLED
        if x == 8:
            button9.config(text='O')
            button9["state"] = tkinter.DISABLED
        state = 0
        count += 1
        label.config(text="X's Turn", foreground='green')
    win()


def disable_buttons():
    button1["state"] = tkinter.DISABLED
    button2["state"] = tkinter.DISABLED
    button3["state"] = tkinter.DISABLED
    button4["state"] = tkinter.DISABLED
    button5["state"] = tkinter.DISABLED
    button6["state"] = tkinter.DISABLED
    button7["state"] = tkinter.DISABLED
    button8["state"] = tkinter.DISABLED
    button9["state"] = tkinter.DISABLED


def reset():
    global state, count
    state = 0
    count = 0
    button1["state"] = tkinter.NORMAL
    button2["state"] = tkinter.NORMAL
    button3["state"] = tkinter.NORMAL
    button4["state"] = tkinter.NORMAL
    button5["state"] = tkinter.NORMAL
    button6["state"] = tkinter.NORMAL
    button7["state"] = tkinter.NORMAL
    button8["state"] = tkinter.NORMAL
    button9["state"] = tkinter.NORMAL
    button1.config(text='')
    button2.config(text='')
    button3.config(text='')
    button4.config(text='')
    button5.config(text='')
    button6.config(text='')
    button7.config(text='')
    button8.config(text='')
    button9.config(text='')
    label.config(text='Ready...', foreground='black')


# Buttons
button1 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(0))
button1.grid(row=1, column=0, pady=5, padx=5)

button2 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(1))
button2.grid(row=1, column=1, pady=5, padx=5)

button3 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(2))
button3.grid(row=1, column=2, pady=5, padx=5)

button4 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(3))
button4.grid(row=2, column=0, pady=5, padx=5)

button5 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(4))
button5.grid(row=2, column=1, pady=5, padx=5)

button6 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(5))
button6.grid(row=2, column=2, pady=5, padx=5)

button7 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(6))
button7.grid(row=3, column=0, pady=5, padx=5)

button8 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(7))
button8.grid(row=3, column=1, pady=5, padx=5)

button9 = Button(text='', width=3, height=1, background='#F2EBE9', highlightbackground='lightblue', fg='black',
                 font=('Arial', 36, 'bold'), command=lambda: x_and_o(8))
button9.grid(row=3, column=2, pady=5, padx=5)
cells = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

reset_button = Button(text='New Game', width=9, height=-2, background='#F2EBE9', highlightbackground='lightblue',
                      fg='black', font=('Arial', 15, 'bold'), command=reset)
reset_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

screen.mainloop()
