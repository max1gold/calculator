#################################################################
# Name: Grant Cooper
# Date: 2/1/2023
# Description: RPi 03 - calculator
#################################################################
from tkinter import *
# the main GUI
class MainGUI(Frame):
    #the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        parent.attributes("-fullscreen", True)
        self.setupGUI()
        self.state = False
    
    #sets up the GUI
    def setupGUI(self):
        #add a normal state

        # the calculator uses the TexGyreAdventor font (see
        # https://www.fontsquirrel.com/fonts/tex-gyre-adventor)
        # on most Linux system, simply double-click the font files and install them on the RPi, copy them to /usr/local/share/fonts (with sudo):
        # sudo cp tex*.otf /usr/local/share/fonts
        # then reboot
        # the display
        # right-align text in the display; and set its background to white, its height to 2 characters, and its font to 50 point TexGyreAdventor
        self.display = Label(self, text="", anchor=E, bg="white", height=2, width=14, font=("TexGyreAdventor", 45))
        # put it in the top row, spanning across all four columns, and expand it on all four sides
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)


        # the button layout
        # ( ) AC **
        # 7 8 9 /
        # 4 5 6 *
        # 1 2 3 -
        # 0 . = +

        # configure the rows and columns of the Frame to adjust to the window
        # there are 6 rows (0 through 5)
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        # there are 4 columns (0 through 3)
        for col in range(4):
            Grid.columnconfigure(self, col, weight=1)

        # the first row
        # (
        # first, fetch and store the image
        # to work best on the RPi, images should be 115x115 pixels otherwise, may need to add .subsample(n)
        img = PhotoImage(file="lpr.png")
        # next, create the button (white background, no border, no highlighting, no color when clicked)
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("("))
        # set the button's image
        button.image = img
        # put the button in its proper row and column
        button.grid(row=1, column=0, sticky=N+S+E+W)
        # the same is done for the rest of the buttons
        # )
        img = PhotoImage(file="rpr.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N+S+E+W)
        # AC
        img = PhotoImage(file="clr.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("AC"))
        button.image = img
        button.grid(row=1, column=2, sticky=N+S+E+W)
        # **
        img = PhotoImage(file="pow.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("**"))
        button.image = img
        button.grid(row=6, column=3, sticky=N+S+E+W)

        # the second row
        # 7
        img = PhotoImage(file="7.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N+S+E+W)
        # 8
        img = PhotoImage(file="8.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N+S+E+W)
        # 9
        img = PhotoImage(file="9.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N+S+E+W)
        # /
        img = PhotoImage(file="div.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("/"))
        button.image = img
        button.grid(row=2, column=3, sticky=N+S+E+W)
        # the third row
        # 4
        img = PhotoImage(file="4.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("4"))
        button.image = img
        button.grid(row=3, column=0, sticky=N+S+E+W)
        # 5
        img = PhotoImage(file="5.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("5"))
        button.image = img
        button.grid(row=3, column=1, sticky=N+S+E+W)
        # 6
        img = PhotoImage(file="6.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("6"))
        button.image = img
        button.grid(row=3, column=2, sticky=N+S+E+W)
        # *
        img = PhotoImage(file="mul.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("*"))
        button.image = img
        button.grid(row=3, column=3, sticky=N+S+E+W)
        # the fourth row
        # 1
        img = PhotoImage(file="1.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("1"))
        button.image = img
        button.grid(row=4, column=0, sticky=N+S+E+W)
        # 2
        img = PhotoImage(file="2.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("2"))
        button.image = img
        button.grid(row=4, column=1, sticky=N+S+E+W)
        # 3
        img = PhotoImage(file="3.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("3"))
        button.image = img
        button.grid(row=4, column=2, sticky=N+S+E+W)
        # -
        img = PhotoImage(file="sub.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("-"))
        button.image = img
        button.grid(row=4, column=3, sticky=N+S+E+W)
        # the fifth row
        # 0
        img = PhotoImage(file="0.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("0"))
        button.image = img
        button.grid(row=5, column=0, sticky=N+S+E+W)
        # .
        img = PhotoImage(file="dot.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("."))
        button.image = img
        button.grid(row=5, column=1, sticky=N+S+E+W)
        # =
        img = PhotoImage(file="eql-wide.png")
        button = Button(self, bg="#437bf9", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("="))
        button.image = img
        button.grid(row=6, column=0, columnspan=2, sticky=N+S+E+W)
        # +
        img = PhotoImage(file="add.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("+"))
        button.image = img
        button.grid(row=5, column=3, sticky=N+S+E+W)
        # %
        img = PhotoImage(file="mod.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("%"))
        button.image = img
        button.grid(row=6, column=2, sticky=N+S+E+W)
        # <-
        img = PhotoImage(file="bak.png")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("<-"))
        button.image = img
        button.grid(row=6, column=3, sticky=N+S+E+W)



        # pack the GUI
        self.pack(fill=BOTH, expand=1)
    #processes button presses
    def process(self, button):
        #AC clears the display
        if (button == "AC"):
            #clear the display
            self.display["text"] = ""
        elif (button == "<-"):
            self.display["text"] = self.display["text"][:-1]
        elif (button == "="):
            #get the expression in the display
            expr = self.display["text"]
            #the evaluation may return an error
            try:
                #evaluate the expression
                result = eval(expr)
                #store the result to the display
                if len(str(result)) > 14:
                    self.display["text"] = str(result)[:11] + "..."
                else:
                    self.display["text"] = str(result)

                self.state = True
            except:
                #note the error in the display
                self.display["text"] = "ERROR"
                self.state = True

        elif len(self.display["text"]) > 14:
            self.display["text"] += ''
        else:
            if (self.state):
                self.display["text"] = ""
                self.state = False

            self.display["text"] += button
        print("Button {} pressed!".format(button))

##############################
# the main part of the program
##############################
# create the window
window = Tk()
# set the window title
window.title("The Reckoner")
# generate the GUI
p = MainGUI(window)
# display the GUI and wait for user interaction
window.mainloop()