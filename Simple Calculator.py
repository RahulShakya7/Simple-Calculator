from tkinter import *

cc = Tk()
cc.geometry('542x487')
cc.resizable(0, 0)
cc.title('Calculator')
cc.iconbitmap('calc.ico')

# Defining the functions (Click, Clear and Equal)


def btn_clk(n):
    global value
    value = value + str(n)
    v1.set(value)


def clear():
    global value
    value = ''
    v1.set('')


def btn_eql():
    global value
    output = str(eval(value))
    v1.set(output)

# Display and Entry


value = " "
v1 = StringVar()

display = Entry(cc, width=37, bd=1, bg='grey40', fg='ghostwhite', textvariable=v1, font=('Cambria', 20), justify='right')
display.place(x=0, y=0)
display.pack(ipady=20)

# Number buttons (0-9)
Button(cc, text="1", font=('Cambria', 12), bg='grey43', fg='white', relief='flat', padx=45, pady=40, command=lambda: btn_clk(1)).place(x=0, y=265)
Button(cc, text="2", font=('Cambria', 12), bg='grey44', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(2)).place(x=110, y=265)
Button(cc, text="3", font=('Cambria', 12), bg='grey45', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(3)).place(x=220, y=265)

Button(cc, text="4", font=('Cambria', 12), bg='grey45', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(4)).place(x=0, y=160)
Button(cc, text="5", font=('Cambria', 12), bg='grey43', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(5)).place(x=110, y=160)
Button(cc, text="6", font=('Cambria', 12), bg='grey44', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(6)).place(x=220, y=160)

Button(cc, text="7", font=('Cambria', 12), bg='grey43', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(7)).place(x=0, y=55)
Button(cc, text="8", font=('Cambria', 12), bg='grey44', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(8)).place(x=110, y=55)
Button(cc, text="9", font=('Cambria', 12), bg='grey45', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(9)).place(x=220, y=55)

Button(cc, text="0", font=('Cambria', 12), bg='grey44', fg='white',  relief='flat', padx=45, pady=40, command=lambda: btn_clk(0)).place(x=0, y=376)

# Arithmetic Operators and Symbols
Button(cc, text="=", font=('Cambria', 12), bg='aquamarine2', fg='lightcyan',  relief='flat', padx=97, pady=41, command=btn_eql).place(x=328, y=374)

Button(cc, text="C", font=('Cambria', 12), bg='slategrey', fg='white', relief='flat', padx=96, pady=40, command=clear).place(x=330, y=55)

plus = Button(cc, text=' + ', bg='grey33', relief='flat', fg='white',  font='Cambria', command=lambda: btn_clk("+"),  padx=40, pady=37)
plus.place(x=330, y=165)

minus = Button(cc, text=' - ', bg='grey34', relief='flat', fg='white',  font='Cambria', command=lambda: btn_clk("-"),  padx=40, pady=37)
minus.place(x=438, y=165)

multiply = Button(cc, text=' × ', bg='grey35', relief='flat', fg='white',  font='Cambria', command=lambda: btn_clk("*"),  padx=40, pady=37)
multiply.place(x=330, y=270)

divide = Button(cc, text=' ÷ ', bg='grey36', relief='flat', fg='white',  font='Cambria', command=lambda: btn_clk("/"),  padx=38, pady=37)
divide.place(x=438, y=270)

mod = Button(cc, text=' MOD ', bg='grey32', relief='flat', fg='white',  font='Cambria', command=lambda: btn_clk("%"),  padx=28, pady=40)
mod.place(x=110, y=376)

power = Button(cc, text=' ^ ', bg='grey31', relief='flat', fg='white',  font='Cambria', command=lambda: btn_clk("**"),  padx=41, pady=40)
power.place(x=220, y=376)

cc.mainloop()