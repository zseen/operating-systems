from tkinter.tix import *
from pathlib import Path

class FolderPrinter:
    def __init__(self):
        self.location = str(Path.home())

    def getDirectories(self, location):
        return os.listdir(location)

    def contentToButtons(self):
        folders = self.getDirectories(self.location)
        root = Tk()
        frame = Frame(width=500, height=500)
        frame.grid()
        swin = ScrolledWindow(frame, width=600, height=600)
        swin.grid()
        win = swin.window

        for folder in folders:
            f = Button(win, text=folder, fg="gray10", bg="old lace", command=lambda folderName=folder: self.printFileNameOnButton(folderName))
            f.grid(sticky=N+S+E+W)

        root.mainloop()

    def printFileNameOnButton(self, name):
        print(name)


def main():
    c = FolderPrinter()
    c.contentToButtons()

if __name__ == "__main__":
    main()