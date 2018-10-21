from tkinter.tix import *
import CommandExecutor as CLE

class FolderPrinter:
    def __init__(self):
        self._commandExecutor = CLE.CommandExecutor()
        self._win = None
        self._buttons = []

    def onClicked(self, name):
        self._commandExecutor.changeDirectory(name)
        self.renderButtons()

    def renderButtons(self):
        for button in self._buttons:
            button.grid_remove()
        folders = self._commandExecutor.listDirectoryContent(self._commandExecutor.getCurrentDirectory())
        for folder in folders:
            b = Button(self._win, text=folder, fg="gray10", bg="old lace", command=lambda folderName=folder: self.onClicked(folderName))
            b.bind("<Mouse-1>", self._commandExecutor.changeDirectory(str(b)))
            self._buttons.append(b)
            b.grid(sticky=N + S + E + W)

    def mainLoopGUI(self):
        root = Tk()
        frame = Frame(width=500, height=500)
        frame.grid()
        swin = ScrolledWindow(frame, width=600, height=600)
        swin.grid()
        self._win = swin.window

        self.renderButtons()

        root.mainloop()


def main():
    c = FolderPrinter()
    c.mainLoopGUI()

if __name__ == "__main__":
    main()
