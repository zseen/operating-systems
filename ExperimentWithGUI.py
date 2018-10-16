from tkinter import *


def alignColouredLabels():
    root=Tk()
    one = Label(root, text="Hi", bg="black", fg="red")
    two = Label(root, text="tiny", bg="yellow", fg="green")
    three = Label(root, text="little", bg="orange", fg="purple")
    four = Label(root, text="Ladybug", bg="pink", fg="blue")

    one.pack(fill=X)
    two.pack(side = LEFT, fill = Y)
    three.pack(fill=X)
    four.pack(side=RIGHT, fill=Y)
    root.mainloop()

def createButtons():
    root = Tk()

    topFrame = Frame(root)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM)

    button1 = Button(topFrame, text="Hello", fg="red")
    button2 = Button(bottomFrame, text="Ladybug", fg="orange")

    button1.pack()
    button2.pack()
    root.mainloop()

def crateGridLayout():
    root = Tk()
    label1 = Label(root, text="From:")
    label2 = Label(root, text="Message:")

    entry1 = Entry(root)
    entry2 = Entry(root)

    label1.grid(row=0, sticky=E)
    label2.grid(row=1, sticky=E)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)

    box = Checkbutton(root, text="Would you like to see a tick?")
    box.grid(columnspan=2)

    root.mainloop()



def printName(event):
    print("My name is Ladybug")

root = Tk()
button1 = Button(root, text="Print my name!")
button1.bind("<Button-1>", printName)
button1.pack()
root.mainloop()
