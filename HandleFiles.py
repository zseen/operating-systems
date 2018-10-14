import os
from BackgroundCommands import Commands
from itertools import islice

class FilesHandling(Commands):
    def joinTogether(self, file1, file2, file3):
        path1 = self.createDirectoryPath(file1)
        path2 = self.createDirectoryPath(file2)
        path3 = self.createDirectoryPath(file3)

        if self.checkIfFileExists(path1) and self.checkIfFileExists(path2):
            with open(path3, "w") as catFile, open(path1, 'r') as f1, open(path2, 'r') as f2:
                for line in f1:
                    catFile.write(line)
                for line in f2:
                    catFile.write(line)

            with open(path3, "r") as catFile:
                for line in catFile:
                    print(line)

    def printTogether(self, file1, file2):
        path1 = self.createDirectoryPath(file1)
        path2 = self.createDirectoryPath(file2)

        if self.checkIfFileExists(path1) and self.checkIfFileExists(path2):
            with open(path1, "r") as f1, open(path2, "r") as f2:
                for line in f1:
                    print(line, end="")
                for line in f2:
                    print(line)

    def cat(self, file):
        if os.path.isfile(self.createDirectoryPath(file)):
            newPathFile = self.createDirectoryPath(file)
            with open(newPathFile, 'r') as f:
                for line in f:
                    print(line)
        else:
            print("This file does not exist.")

    def mkdir(self, name):
        newPath = self.createDirectoryPath(name)
        if not os.path.exists(newPath):
            os.makedirs(newPath)
            print("Your new folder is ready! It is called " + name + " and is here: " + newPath)
        else:
            print("This folder already exists.")

    def rm(self, name):
        filePath = self.createDirectoryPath(name)
        if self.checkIfFileExists(filePath):
            os.remove(filePath)
            print("File " + name + " removed.")

    def head(self, file, linesNum):
        path = self.createDirectoryPath(file)
        if os.path.exists(path):
            with open(path, "r") as f:
                for line in islice(f, int(linesNum)):
                    print(line)
        else:
            print("I cannot find this file.")