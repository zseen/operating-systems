from tkinter.tix import *
import CommandExecutor as CLE


class FolderPrinter:
    def __init__(self):
        self._commandExecutor = CLE.CommandExecutor()
        self._win = None
        self._buttons = []
        self._isFileOpen = False
        self._isTextWindowVisible = False

    def onClickedOpenTextOtChangeDirectory(self, name):
        locationType = self._commandExecutor.checkIfTypeFileOrDirectory(name)
        self._isFileOpen = True

        if locationType == CLE.EntityType.folder:
            self._commandExecutor.changeDirectory(name)
        else:
            content = self._commandExecutor.getFileContent(str(name))
            textWindow = self.createTextWindowWithContent(content)
            closeButton = Button(self._win, text="Close", fg="black", bg="salmon",
                                    command=lambda: self.onClickCloseTextFileButton(closeButton, textWindow))
            closeButton.grid()
        self.renderUI()

    def createTextWindowWithContent(self, fileName):
        textWindow = Text(self._win, wrap=WORD, width=80, height=20)
        for line in fileName:
            textWindow.insert(INSERT, line)
        textWindow.grid(sticky=N + S + E + W)
        return textWindow

    def onClickBackButton(self):
        self._commandExecutor.goBackOneLevel()
        self.renderButtons()

    def onClickCloseTextFileButton(self, button, window):
        window.destroy()
        button.grid_remove()

    def renderUI(self):
        if self._isFileOpen:
            self._isTextWindowVisible = True
        else:
            self._isTextWindowVisible = False

        self.renderButtons()

    def renderButtons(self):
        for button in self._buttons:
            button.grid_remove()
        folders = self._commandExecutor.listDirectoryContent(self._commandExecutor.getCurrentDirectory())
        for folder in folders:
            b = Button(self._win, text=folder, fg="gray10", bg="old lace", command=lambda folderName=folder: self.onClickedOpenTextOtChangeDirectory(folderName))
            self._buttons.append(b)
            b.grid(sticky=N + S + E + W)

    def mainLoopGUI(self):
        root = Tk()
        frame = Frame(width=500, height=500)
        frame.grid()
        swin = ScrolledWindow(frame, width=600, height=600)

        swin.grid()
        self._win = swin.window

        backButton = Button(frame, text="Back to previous folder", fg="black", bg="salmon",
                            command=self.onClickBackButton)
        backButton.grid()

        self.renderUI()

        root.mainloop()


def main():
    c = FolderPrinter()
    c.mainLoopGUI()

if __name__ == "__main__":
    main()
