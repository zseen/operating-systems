from tkinter.tix import *
from tkinter import filedialog
from pathlib import Path
import CommandExecutor as CLE

class FolderPrinter:
    def __init__(self):
        self.commandExecutor = CLE.CommandExecutor()
        self.location = self.commandExecutor.getCurrentDirectory()

    def printFileNameOnButton(self, name):
        print(name)

    def clickButtonSeeContent(self, button):
        filename = self.commandExecutor.changeDirectory(str(button))

        button.bind("<Mouse-1>", filename)
        button.grid()

    def contentToButtons(self):
        folders = self.commandExecutor.listDirectoryContent(self.location)
        root = Tk()
        frame = Frame(width=500, height=500)
        frame.grid()
        swin = ScrolledWindow(frame, width=600, height=600)
        swin.grid()
        win = swin.window

        for folder in folders:
            f = Button(win, text=folder, fg="gray10", bg="old lace", command=lambda folderName=folder: self.printFileNameOnButton(folderName))
            f.bind("<Mouse-1>", self.commandExecutor.changeDirectory(str(f)))


            f.grid(sticky=N + S + E + W)
            #self.clickButtonSeeContent(f)



        #root = Tk()
        #root.filename = filedialog.askopenfilename(initialdir=self.commandExecutor.getCurrentDirectory(), title="Select file",
        #                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))
        #print(root.filename)



        root.mainloop()






def main():
    c = FolderPrinter()
    c.contentToButtons()

if __name__ == "__main__":
    main()