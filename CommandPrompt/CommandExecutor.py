import os
from itertools import islice
import FilesystemHelpers as FH
from enum import Enum

EntityType = Enum('EntityType', 'file folder')

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
        newPath = FH.createPathInDirectory(currentDir, ''.join(location))
        exists = FH.checkIfDirectoryExists(newPath)

        if not exists:
            return False

        self.currentDirectory = newPath
        return True

    def goBackOneLevel(self):
        atRootLevel = FH.isRootLevel(self.currentDirectory)

        if atRootLevel:
            return False

        pathToModify = list(os.path.split(self.currentDirectory))
        pathToModify.pop()
        for directory in pathToModify:
            self.currentDirectory = str(directory)
        return True

    def joinTwoFilesTogetherInThird(self, file1, file2, file3):
        path1 = FH.createPathInDirectory(self.currentDirectory, file1)
        path2 = FH.createPathInDirectory(self.currentDirectory, file2)
        path3 = FH.createPathInDirectory(self.currentDirectory, file3)
        content = []

        if not (FH.checkIfFileExists(path1) and FH.checkIfFileExists(path2)):
            return None

        with open(path3, "w") as catFile, open(path1, 'r') as f1, open(path2, 'r') as f2:
            for line in f1:
                catFile.write(line)
            for line in f2:
                catFile.write(line)

        with open(path3, "r") as catFile:
            for line in catFile:
                content.append(line)
        return content


    def printTwoFilesTogether(self, file1, file2):
        path1 = FH.createPathInDirectory(self.currentDirectory, file1)
        path2 = FH.createPathInDirectory(self.currentDirectory, file2)
        content = []

        if not (FH.checkIfFileExists(path1) and FH.checkIfFileExists(path2)):
            return None

        with open(path1, "r") as f1, open(path2, "r") as f2:
            for line in f1:
                content.append(line)
            for line in f2:
                content.append(line)
        return content


    def getFileContent(self, file):
        pathToFile = FH.createPathInDirectory(self.currentDirectory, file)
        exists = FH.checkIfFileExists(pathToFile)
        content = []

        if not exists:
            return None

        with open(pathToFile, 'r') as f:
            for line in f:
                content.append(line)
        return content

    def makeDirectory(self, name):
        newPath = FH.createPathInDirectory(self.currentDirectory, name)

        if FH.checkIfDirectoryExists(newPath):
            return False

        os.makedirs(newPath)
        return True

    def removeFile(self, name):
        filePath = FH.createPathInDirectory(self.currentDirectory, name)
        exists = FH.checkIfFileExists(filePath)
        if not exists:
            return False

        os.remove(filePath)
        return True

    def getTextLinesFromBeginning(self, file, linesNum):
        path = FH.createPathInDirectory(self.currentDirectory, file)
        exists = FH.checkIfFileExists(path)
        content = []

        if not exists:
            return None

        with open(path, "r") as f:
            for line in islice(f, int(linesNum)):
                content.append(line)
        return content

    def getPathFromCurrentFolder(self, destination):
        path = FH.createPathInDirectory(self.currentDirectory, destination)
        return path


    def checkIfTypeFileOrDirectory(self, name):
        namePath = self.getPathFromCurrentFolder(name)

        if os.path.isdir(namePath):
            return EntityType.folder
        else:
            return EntityType.file



