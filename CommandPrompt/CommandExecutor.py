import os
from itertools import islice
import FilesystemHelpers as FH

class CommandExecutor:
    def __init__(self):
        self.currentDirectory = FH.getHomeDirectory()

    def getCurrentDirectory(self):
        return self.currentDirectory

    def listDirectoryContent(self, instruction):
        foldersList = []

        if len(instruction) == 2 and instruction[1] == "-r":
            for item in reversed(list(os.listdir(self.currentDirectory))):
                foldersList.append(item)
        else:
            for item in os.listdir(self.currentDirectory):
                foldersList.append(item)

        return foldersList

    def changeDirectory(self, location):
        currentDir = self.currentDirectory
        newPath = FH.createDirectoryPath(currentDir,''.join(location))
        exists = FH.checkIfDirectoryExists(newPath)

        if exists:
            self.currentDirectory = newPath
            return True
        return False

    def goBackOneLevel(self):
        atRootLevel = FH.isRootLevel(self.currentDirectory)

        if not atRootLevel:
            pathToModify = list(os.path.split(self.currentDirectory))
            pathToModify.pop()
            for directory in pathToModify:
                self.currentDirectory = str(directory)
            return True
        return False

    def joinTwoFilesTogetherInThird(self, file1, file2, file3):
        path1 = FH.createDirectoryPath(self.currentDirectory, file1)
        path2 = FH.createDirectoryPath(self.currentDirectory, file2)
        path3 = FH.createDirectoryPath(self.currentDirectory, file3)
        content = []

        if FH.checkIfFileExists(path1) and FH.checkIfFileExists(path2):
            with open(path3, "w") as catFile, open(path1, 'r') as f1, open(path2, 'r') as f2:
                for line in f1:
                    catFile.write(line)
                for line in f2:
                    catFile.write(line)

            with open(path3, "r") as catFile:
                for line in catFile:
                    content.append(line)
            return content
        else:
            return None

    def printTwoFilesTogether(self, file1, file2):
        path1 = FH.createDirectoryPath(self.currentDirectory, file1)
        path2 = FH.createDirectoryPath(self.currentDirectory, file2)
        content = []

        if FH.checkIfFileExists(path1) and FH.checkIfFileExists(path2):
            with open(path1, "r") as f1, open(path2, "r") as f2:
                for line in f1:
                    content.append(line)
                for line in f2:
                    content.append(line)
            return content
        else:
            return None


    def getFileContent(self, file):
        pathToFile = FH.createDirectoryPath(self.currentDirectory, file)
        exists = FH.checkIfFileExists(pathToFile)
        content = []

        if exists:
            with open(pathToFile, 'r') as f:
                for line in f:
                    content.append(line)
            return content
        else:
            return None

    def makeDirectory(self, name):
        newPath = FH.createDirectoryPath(self.currentDirectory, name)

        if not FH.checkIfDirectoryExists(newPath):
            os.makedirs(newPath)
            return True
        return False

    def removeFile(self, name):
        filePath = FH.createDirectoryPath(self.currentDirectory, name)
        exists = FH.checkIfFileExists(filePath)
        if exists:
            os.remove(filePath)
            return True
        else:
            return False

    def getTextLinesFromBeginning(self, file, linesNum):
        path = FH.createDirectoryPath(self.currentDirectory, file)
        exists = FH.checkIfFileExists(path)
        content = []
        if exists:
            with open(path, "r") as f:
                for line in islice(f, int(linesNum)):
                    content.append(line)
            return content
        else:
            return None

