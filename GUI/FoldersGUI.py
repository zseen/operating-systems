from tkinter.tix import *
import sys
sys.path.append('../')

from CommandPrompt import CommandExecutor as CLE


class FolderPrinter:
    def __init__(self):
        self._commandExecutor = CLE.CommandExecutor()
        self._mainWindow = None
        self._buttonsForFolderContent = []
        self._currOpenFile = None
        self._textWindow = None
        self._closeButton = None
        self._backButton = None

    def _onClickButtonForFolderContent(self, name):
        try:
            locationType = self._commandExecutor.checkIfTypeFileOrDirectory(name)
            if locationType == CLE.EntityType.folder:
                self._commandExecutor.changeDirectory(name)
            else:
                self._currOpenFile = self._commandExecutor.getPathFromCurrentFolder(name)
            self._renderUI()
        except PermissionError:
            self._commandExecutor.goBackOneLevel()
            self._textWindow.delete('1.0', END)
            self._textWindow.insert(INSERT, "You don't have permission to view the content of this folder.")
            self._textWindow.grid(sticky=N + S + E + W)
            self._closeButton.grid()


    def _onClickBackButton(self):
        self._commandExecutor.goBackOneLevel()
        self._renderUI()

    def _onClickCloseTextFileButton(self):
        self._currOpenFile = None
        self._renderUI()

    def _renderUI(self):
        if self._currOpenFile:
            self._textWindow.delete('1.0', END)
            try:
                fileContent = self._commandExecutor.getFileContent(self._currOpenFile)
                self._textWindow.insert(INSERT, fileContent)
            except UnicodeDecodeError:
                self._textWindow.insert(INSERT, "Cannot open this file extension.")
            self._textWindow.grid(sticky=N + S + E + W)
            self._closeButton.grid()
        else:
            self._textWindow.grid_remove()
            self._closeButton.grid_remove()

        if not self._commandExecutor.isRootLevel():
            self._backButton.grid()
        else:
            self._backButton.grid_remove()

        self._renderButtonsForFolderContent()

    def _renderButtonsForFolderContent(self):
        for button in self._buttonsForFolderContent:
            button.grid_remove()
        folders = self._commandExecutor.listDirectoryContent(self._commandExecutor.getCurrentDirectory())
        for folderName in folders:
            b = Button(self._mainWindow, text=folderName, fg="gray10", bg="old lace", command=lambda folderName=folderName: self._onClickButtonForFolderContent(folderName))
            self._buttonsForFolderContent.append(b)
            b.grid(sticky=N + S + E + W)

    def _initialiseUI(self):
        root = Tk()
        frame = Frame(width=500, height=500)
        frame.grid()
        swin = ScrolledWindow(frame, width=600, height=600)
        swin.grid()
        self._mainWindow = swin.window

        self._backButton = Button(frame, text="Back to previous folder", fg="black", bg="salmon",
                            command=self._onClickBackButton)
        self._textWindow = Text(self._mainWindow, wrap=WORD, width=80, height=20)
        self._closeButton = Button(self._mainWindow, text="Close", fg="black", bg="salmon",
                                   command=self._onClickCloseTextFileButton)

        self._renderUI()

        return root

    def mainLoopGUI(self):
        root = self._initialiseUI()
        root.mainloop()


def main():
    c = FolderPrinter()
    c.mainLoopGUI()

if __name__ == "__main__":
    main()
