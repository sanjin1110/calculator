from tkinter import *

root = Tk()
root.geometry("475x475")
root.resizable(0, 0)
root.title("Calculator")
root.iconbitmap('Calculator.ico')


def btn_click(num):
    global exp
    exp = exp + str(num)
    input_text.set(exp)


def btn_clear():
    global exp
    exp = ""
    input_text.set("")


def btn_equal():
    global exp
    result = str(eval(exp))
    input_text.set(result)
    exp = ""

exp = ""

input_text = StringVar()

frame = Frame(root, width = 200, bd = 0, highlightbackground = "black", highlightcolor = "LemonChiffon3",
              highlightthickness = 4)

frame.pack(side = TOP)

entry = Entry(frame, font = ('arial', 18, 'bold'), textvariable = input_text, borderwidth = 1, width = 50,
              bg = "CadetBlue1",
              bd = 0, justify = RIGHT)

entry.grid(row = 0, column = 0)

entry.pack(ipady = 10)

btn_frame = Frame(root, width = 600, height = 350, bg = "grey64")
btn_frame.pack()

button_0 = Button(btn_frame, text = "C", fg = "black", width = 32, height = 3, font = 2, bd = 0, bg = "light cyan",
                  cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1,
                                                                        ipadx = 1, pady = 1)

button_1 = Button(btn_frame, text = "/", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "gray",
                  cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

button_2 = Button(btn_frame, text = "7", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                  cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

button_3 = Button(btn_frame, text = "8", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                  cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)

button_4 = Button(btn_frame, text = "9", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                  cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)

button_5 = Button(btn_frame, text = "*", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "gray",
                  cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

button_6 = Button(btn_frame, text = "4", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                  cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

button_7 = Button(btn_frame, text = "5", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                  cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

button_8 = Button(btn_frame, text = "6", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                  cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

button_9 = Button(btn_frame, text = "-", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "gray",
                  cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

button_10 = Button(btn_frame, text = "1", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                   cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

button_11 = Button(btn_frame, text = "2", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                   cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

button_12 = Button(btn_frame, text = "3", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "dim gray",
                   cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

button_13 = Button(btn_frame, text = "+", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "gray",
                   cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

button_14 = Button(btn_frame, text = "0", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "gray",
                   cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, padx = 1, pady = 1)

button_15 = Button(btn_frame, text = ".", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "gray",
                   cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
button_17 = Button(btn_frame, text = "%", fg = "white", width = 10, height = 3, font = 2, bd = 0, bg = "gray",
                   cursor = "hand2", command = lambda: btn_click("%")).grid(row = 4, column = 1, padx = 1, pady = 1)

button_16 = Button(btn_frame, text = "=", fg = "black", width = 10, height = 3, font = 2, bd = 0, bg = "light cyan",
                   cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()
