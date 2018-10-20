from tkinter.tix import *
from tkinter import filedialog
from pathlib import Path
import CommandExecutor as CLE

class FolderPrinter:
    def __init__(self):
        self.commandExecutor = CLE.CommandExecutor()
        self._win = None
        self.buttons = []

    def onClicked(self, name):
        self.commandExecutor.changeDirectory(name)
        self.renderButtons()

    def renderButtons(self):
        for button in self.buttons:
            button.grid_remove()
        folders = self.commandExecutor.listDirectoryContent(self.commandExecutor.getCurrentDirectory())
        for folder in folders:
            b = Button(self.win, text=folder, fg="gray10", bg="old lace", command=lambda folderName=folder: self.onClicked(folderName))
            b.bind("<Mouse-1>", self.commandExecutor.changeDirectory(str(b)))
            self.buttons.append(b)
            b.grid(sticky=N + S + E + W)

    def GUImainloop(self):
        root = Tk()
        frame = Frame(width=500, height=500)
        frame.grid()
        swin = ScrolledWindow(frame, width=600, height=600)
        swin.grid()
        self.win = swin.window

        self.renderButtons()

        root.mainloop()


def main():
    c = FolderPrinter()
    c.GUImainloop()

if __name__ == "__main__":
    main()
