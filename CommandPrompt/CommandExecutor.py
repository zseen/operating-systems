import os
from itertools import islice
import FilesystemHelpers as FH

class CommandExecutor:
    def __init__(self):
        self.currentDirectory = FH.getHomeDirectory()

    def getCurrentDirectory(self):
        return self.currentDirectory

    def ls(self, instruction):
        foldersList = []

        if len(instruction) == 2 and instruction[1] == "-r":
            for item in reversed(list(os.listdir(self.currentDirectory))):
                foldersList.append(item)
        else:
            for item in os.listdir(self.currentDirectory):
                foldersList.append(item)

        return foldersList

    def cd(self,location):
        if location[0] == "..":
            currentDir = self.goBackOneLevel()
            self.currentDirectory = currentDir
        else:
            currentDir = self.currentDirectory
            newPath = FH.createDirectoryPath(currentDir,''.join(location))
            exists = FH.checkIfDirectoryExists(newPath)

            if exists:
                self.currentDirectory = newPath
            else:
                return False
        return self.currentDirectory


    def goBackOneLevel(self):
        atRootLevel = FH.isRootLevel(self.currentDirectory)

        if not atRootLevel:
            pathToModify = list(os.path.split(self.currentDirectory))
            pathToModify.pop()
            for directory in pathToModify:
                self.currentDirectory = str(directory)

        return self.currentDirectory

    def joinTogether(self, file1, file2, file3):
        path1 = FH.createDirectoryPath(self.currentDirectory, file1)
        path2 = FH.createDirectoryPath(self.currentDirectory, file2)
        path3 = FH.createDirectoryPath(self.currentDirectory, file3)

        if FH.checkIfFileExists(path1) and FH.checkIfFileExists(path2):
            with open(path3, "w") as catFile, open(path1, 'r') as f1, open(path2, 'r') as f2:
                for line in f1:
                    catFile.write(line)
                for line in f2:
                    catFile.write(line)

            with open(path3, "r") as catFile:
                for line in catFile:
                    print(line)

    def printTogether(self, file1, file2):
        path1 = FH.createDirectoryPath(self.currentDirectory, file1)
        path2 = FH.createDirectoryPath(self.currentDirectory, file2)

        if FH.checkIfFileExists(path1) and FH.checkIfFileExists(path2):
            with open(path1, "r") as f1, open(path2, "r") as f2:
                for line in f1:
                    print(line, end="")
                for line in f2:
                    print(line)

    def cat(self, file):
        pathToFile = FH.createDirectoryPath(self.currentDirectory, file)
        exists = FH.checkIfFileExists(pathToFile)

        if exists:
            with open(pathToFile, 'r') as f:
                for line in f:
                    print(line)
        else:
            print("This file does not exist.")

    def mkdir(self, name):
        newPath = FH.createDirectoryPath(self.currentDirectory, name)
        if not FH.checkIfDirectoryExists(newPath):
            os.makedirs(newPath)
            print("Your new folder is ready! It is called " + name + " and is here: " + newPath)
        else:
            print("This folder already exists.")

    def rm(self, name):
        filePath = FH.createDirectoryPath(self.currentDirectory, name)
        exists = FH.checkIfFileExists(filePath)
        if exists:
            os.remove(filePath)
            print("File " + name + " removed.")
        else:
            print("I cannot find this file.")

    def head(self, file, linesNum):
        path = FH.createDirectoryPath(self.currentDirectory, file)
        exists = FH.checkIfFileExists(path)
        if exists:
            with open(path, "r") as f:
                for line in islice(f, int(linesNum)):
                    print(line)
        else:
            print("I cannot find this file.")

