from tkinter import *
from tkinter.messagebox import *
import re
import math as mt
root = Tk()
root.title("ZE OS NATIVES")

val = str()
Answers = ['0']
Last_Input = []
Main = Entry(root, justify="right",  width=25, font=("ariel", 20), bg="powder blue", fg="darkgreen", borderwidth=5)
Main.grid(row=0, column=1, columnspan=4, padx=0, pady=2)
input_label = Label(root, text="Input: ")
input_label.grid(row=0, column=0, padx=2, pady=2)
Main_output = Entry(root, justify="right", width=25, font=("ariel", 20), bg="light green", fg="blue", borderwidth=5)
Main_output.grid(row=1, column=1, columnspan=3, padx=0, pady=2)
Output_label = Label(root, text="Output: ")
Output_label.grid(row=1, column=0, padx=2, pady=2)
e = Main
Output = Main_output
def button_click(number):
   global e
   b = number.widget
   text = b['text']
   if text == '=':
       try:
           Output.delete(0, END)
           val = str(e.get())
           x = val
           Last_Input.append(val)
           val = val.replace(f'{chr(175)}\u00b9', '**(-1)')
           val = val.replace('√(', 'mt.sqrt(')
           val = val.replace('Ans', str(Answers[-1]))
           val = val.replace(f'{chr(710)}', '**')
           val = val.replace('π', 'mt.pi')
           val = val.replace('\u00b2', '**2')
           val = val.replace('sin', f'mt.sin')
           val = val.replace('cos', f'mt.cos')
           val = val.replace('tan', f'mt.tan')

           pattern4 = re.compile(r'(\d+[\.]?\d*)˚(\d*[\.]?\d*)\'?(\d*[\.]?\d*)"?')

           matches4 = pattern4.finditer(x)

           for match in matches4:
               if match:
                   text = match[0]
                   a, b, c = 0, 0, 0
                   try:
                       a = float(match.group(1))
                   except:
                       a = 0
                   try:
                       b = float(match.group(2)) / 60
                   except:
                       b = 0
                   try:
                       c = float(match.group(3)) / 3600
                   except:
                       c = 0
                   deg = a + b + c
                   rad = mt.radians(deg)
                   val = val.replace(text, f'{rad}')
           result = str(round(eval(val), 4))
           Output.insert(0, result)
           Answers.append(result)
       except:
           showerror("Error : ", e)
       return
   e.insert(END, text)

def button_clear1():
    global Ans
    Ans = Output.get()
    e.delete(0, END)
    Output.delete(0, END) 

def bkspc():
    stri = e.get()
    length = len(stri) - 1
    e.delete(length, END)

def button_Ans():
    val1 = str(e.get()) + 'Ans'
    e.delete(0, END)
    e.insert(0, val1)

def button_last_input():
    val1 = str(e.get())
    e.delete(0, END)
    val1 = str(val1) + Last_Input[-1]
    e.insert(0, val1)

def button_x2():
    x = str(e.get())
    x2 = x + '\u00b2'
    e.delete(0, END)
    e.insert(0, x2)

def button_xinv():
    x = str(e.get())
    x2 = x + f'{chr(175)}\u00b9'
    e.delete(0, END)
    e.insert(0, x2)

def button_xn():
    x = str(e.get())
    e.delete(0, END)
    xn = x + f'{chr(710)}'
    e.insert(0, xn)

def button_dms():
    x = str(e.get())
    pattern1 = re.compile(r'(^\d|\+|\*|-|/|\()\d*[\.]?\d*$')
    pattern2 = re.compile(r'˚\d+[\.]?\d*$')
    pattern3 = re.compile(r'\'\d+[\.]?\d*$')

    matches1 = pattern1.finditer(x)
    matches2 = pattern2.finditer(x)
    matches3 = pattern3.finditer(x)
    for match in matches1:
        if match:
            e.insert(END, '˚')
    for match in matches2:
        if match:
            e.insert(END, '\'')
    for match in matches3:
        if match:
            e.insert(END, '"')


m = True

def button_CONV():
    def reverse():
        global m
        m = False
    global Output
    root_CONV = Tk()
    text1 = Output.get()
    conv_window = Entry(root_CONV, justify="right", font=("ariel", 20), bg="powder blue", fg="darkgreen", borderwidth=5)
    conv_window.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    e = conv_window
    e.insert(0, text1)
    def button_click1(number):
        global m
        b = number.widget
        text = b['text']
        words = text.split()
        words_rev = list(reversed(words))
        text_rev = " ".join(words_rev)
        if m:
            e.insert(END, text)
        else:
            e.insert(END, text_rev)
            m = True

    def convert():
        text2 = re.finditer(r'(^\d+\.?\d*)', e.get())
        text3 = 0
        for match in text2:
            text3 = match.group(1)

        if 'Acre to m\u00b2' in e.get():
            number = float(text3)
            out = number * 4046.85642
            button_clear1()
            Output.insert(0, out)
        if 'm\u00b2 to Acre' in e.get():
            number = float(text3)
            out = number/4046.85642
            button_clear1()
            Output.insert(0, out)

        if 'm to ft' in e.get():
            number = float(text3)
            out = number * 3.2808399
            button_clear1()
            Output.insert(0, out)
        if 'ft to m' in e.get():
            number = float(text3)
            out = number/3.2808399
            button_clear1()
            Output.insert(0, out)
        if 'kgs to lbs' in e.get():
            number = float(text3)
            out = number * 2.20462262
            button_clear1()
            Output.insert(0, out)
        if 'lbs to kgs' in e.get():
            number = float(text3)
            out = number/2.20462262
            button_clear1()
            Output.insert(0, out)
        if 'atm to kPa' in e.get():
            number = float(text3)
            out = number * 101.325
            button_clear1()
            Output.insert(0, out)
        if 'kPa to atm' in e.get():
            number = float(text3)
            out = number/101.325
            button_clear1()
            Output.insert(0, out)
        if 'gal(US) to Ltr' in e.get():
            number = float(text3)
            out = number * 4.54609
            button_clear1()
            Output.insert(0, out)
        if 'Ltr to gal(US)' in e.get():
            number = float(text3)
            out = number/4.54609
            button_clear1()
            Output.insert(0, out)
        if '˚C to ˚F' in e.get():
            number = float(text3)
            out = number * 9/5 + 32
            button_clear1()
            Output.insert(0, out)
        if '˚F to ˚C' in e.get():
            number = float(text3)
            out = (number -32) * 5/9
            button_clear1()
            Output.insert(0, out)

    root_CONV.title("Converter")
    button_len = Button(root_CONV, text="m to ft",  width=12, height=3)
    button_len.grid(row=1, column=0)
    button_len.bind('<Button-1>', button_click1)
    button_weight = Button(root_CONV, text="kgs to lbs",  width=12, height=3)
    button_weight.grid(row=1, column=1)
    button_weight.bind('<Button-1>', button_click1)
    button_area = Button(root_CONV, text="Acre to m\u00b2",  width=12, height=3)
    button_area.grid(row=1, column=2)
    button_area.bind('<Button-1>', button_click1)
    button_pressure = Button(root_CONV, text="atm to kPa",  width=12, height=3)
    button_pressure.grid(row=2, column=0)
    button_pressure.bind('<Button-1>', button_click1)
    button_vol = Button(root_CONV, text="gal(US) to Ltr", width=12, height=3)
    button_vol.grid(row=2, column=1)
    button_vol.bind('<Button-1>', button_click1)
    button_temp = Button(root_CONV, text="˚C to ˚F", width=12, height=3)
    button_temp.grid(row=2, column=2)
    button_temp.bind('<Button-1>', button_click1)
    button_convert = Button(root_CONV, text="convert", width=22, height=3, activebackground='light green', fg="red", command = convert)
    button_convert.grid(row=3, column=1, columnspan=2)
    button_reverse = Button(root_CONV, text="Reverse", width=12, height=3, activebackground='purple', fg="red",
                            command= reverse)
    button_reverse.grid(row=3, column=0)

temp = 1

for i in range(2, 5):
    for j in range(3):
        btn = Button(root, text = str(temp), font=("Ariel", 15, "bold"), width=12, height=3, highlightbackground='light blue', activeforeground='red', activebackground='white')
        btn.grid(row=i, column=j)
        btn.bind('<Button-1>', button_click)
        temp += 1

button_0 = Button(root, text="0", font=("Ariel", 15, "bold"),  width=12, height=3, highlightbackground='light blue')
button_0.bind('<Button-1>', button_click)
button_equal = Button(root, text="=", fg="blue", font=("Ariel", 15, "bold"),highlightbackground='light green',  width=12, height=3)
button_equal.bind('<Button-1>', button_click)
button_clear = Button(root, text="Clear", fg="red", font=("Ariel", 15, "bold"), highlightbackground='light yellow',  width=12, height=3, command=button_clear1)
button_pi = Button(root, text="π", font=("Ariel", 15, "bold"),  width=12, height=3, highlightbackground='light blue')
button_pi.bind('<Button-1>', button_click)
button_bkspc = Button(root, text="bksps", fg="red", font=("Ariel", 15, "bold"),  width=12, height=3, command= bkspc)

button_add = Button(root, text="+", fg="green", highlightbackground='pink', font=("Ariel", 15, "bold"),  width=12, height=3)
button_add.bind('<Button-1>', button_click)
button_sub = Button(root, text="-", fg="brown", highlightbackground='pink', font=("Ariel", 15, "bold"),  width=12, height=3)
button_sub.bind('<Button-1>', button_click)
button_mul = Button(root, text="*", fg="dark green", highlightbackground='pink', font=("Ariel", 15, "bold"),  width=12, height=3)
button_mul.bind('<Button-1>', button_click)
button_div = Button(root, text=" /", fg="purple", highlightbackground='pink', font=("Ariel", 15, "bold"),  width=12, height=3)
button_div.bind('<Button-1>', button_click)
button_sqrt = Button(root, text="√(", fg="red", font=("Ariel", 15, "bold"),  width=12, height=3)
button_sqrt.bind('<Button-1>', button_click)

button_Ans = Button(root, text="Last Output", highlightbackground='yellow', fg="dark green", font=("Ariel", 15, "bold"),  width=12, height=3, command= button_Ans)
button_last_input = Button(root, text="Last Input", highlightbackground='yellow', fg="dark green", font=("Ariel", 15, "bold"),  width=12, height=3, command= button_last_input)
button_CONV = Button(root, text="CONV", fg="grey", font=("Ariel", 15, "bold"),  width=12, height=3, command=button_CONV)
button_x2 = Button(root, text="x\u00b2", fg="grey", font=("Ariel", 15, "bold"),  width=12, height=3, command=button_x2)
button_xn = Button(root, text=f"x{chr(710)}n", fg="grey", font=("Ariel", 15, "bold"),  width=12, height=3, command=button_xn)
button_left_brace = Button(root, text="(", fg="red", font=("Ariel", 15, "bold"),  width=12, height=3)
button_left_brace.bind('<Button-1>', button_click)
button_right_brace = Button(root, text=")", fg="red", font=("Ariel", 15, "bold"),  width=12, height=3)
button_right_brace.bind('<Button-1>', button_click)
button_sin = Button(root, text="sin(", fg="brown", font=("Ariel", 15, "bold"),  width=12, height=3)
button_sin.bind('<Button-1>', button_click)
button_cos = Button(root, text="cos(", fg="brown", font=("Ariel", 15, "bold"),  width=12, height=3)
button_cos.bind('<Button-1>', button_click)
button_tan = Button(root, text="tan(", fg="brown", font=("Ariel", 15, "bold"),  width=12, height=3)
button_tan.bind('<Button-1>', button_click)
button_dms = Button(root, text="˚'\"", fg="brown", font=("Ariel", 15, "bold"),  width=12, height=3, command= button_dms)
button_dot = Button(root, text=".", fg="brown", font=("Ariel", 15, "bold"),  width=12, height=3)
button_dot.bind('<Button-1>', button_click)
button_xinv = Button(root, text=f"x{chr(175)}\u00b9", font=("Ariel", 15, "bold"),  width=12, height=3, command=button_xinv)

button_xinv.grid(row=2, column=3)
button_x2.grid(row=3, column=3)
button_xn.grid(row=4, column=3)

button_0.grid(row=5, column=0)
button_add.grid(row=5, column=1)
button_div.grid(row=5, column=2)
button_pi.grid(row=5, column=3)


button_dot.grid(row=6, column=0)
button_sub.grid(row=6, column=1)
button_mul.grid(row=6, column=2)
button_last_input.grid(row=6, column=3)


button_left_brace.grid(row=7, column=0)
button_dms.grid(row=7, column=1)
button_sqrt.grid(row=7, column=2)
button_Ans.grid(row=7, column=3)

button_right_brace.grid(row=8, column=0)
button_CONV.grid(row=8, column=1)
button_clear.grid(row=8, column=3)
button_bkspc.grid(row=8, column=2)



button_sin.grid(row=9, column=0)
button_cos.grid(row=9, column=1)
button_tan.grid(row=9, column=2)
button_equal.grid(row=9, column=3)



fontMenu = ('', 15)
menubar = Menu(root)
mode = Menu(menubar, font=fontMenu)
mode.add_command(label="Scientific Calculator")
menubar.add_cascade(label="Mode", menu=mode)

root.config(menu=menubar)

root.mainloop()