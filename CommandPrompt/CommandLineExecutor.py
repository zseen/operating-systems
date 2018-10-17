import os
from itertools import islice
import FilesystemHelpers as FH
from pathlib import Path

INITIAL_HELP = ("Options:" '\n'
                "'ls' to see my content, " '\n'
                "'ls -r' to see my content reversed, "  '\n'
                "'cat <file>' to see the content of a text file, " '\n'
                "'printTogether <file1> <file2>' to print two text files together," '\n'
                "'joinTogether <file1> <file2> <file3>' merge file1 and file2 into file3," '\n'
                "'mkdir <name>' to create a folder, " '\n'
                "'rm <name>' to delete a file, " '\n'
                "'head <file> <x>' to see the first x lines of a file, " '\n'
                "'cd <somewhere>' to go somewhere, " '\n'
                "'cd..' to go back to the previous level directory, or " '\n'
                "'exit' to...exit! " '\n')


class CommandLineExecutor:
    def __init__(self):
        self.currentDirectory = FH.getHomeDirectory()

    def run(self):
        print(INITIAL_HELP)

        while True:
            print(self.currentDirectory)
            command = input("What should I do?: ")

            request = command.split()

            if request[0] == "ls":
                self.ls(request)

            if request[0] == "cd":
                self.cd(request[1:])

            if request[0] == "joinTogether" and len(request) == 4:
                self.joinTogether(request[1], request[2], request[3])

            if request[0] == "printTogether" and len(request) == 3:
                self.printTogether(request[1], request[2])

            if request[0] == "cat" and len(request) == 2:
                self.cat(request[1])

            if request[0] == "mkdir" and len(request) == 2:
                self.mkdir(request[1])

            if request[0] == "rm" and len(request) == 2:
                self.rm(request[1])

            if request[0] == "head" and len(request) == 3:
                self.head(request[1], request[2])

            if command == "exit":
                exit(0)

    def ls(self, instruction):
        print("")
        print("The content of " + self.currentDirectory + " is: ")

        if len(instruction) == 2 and instruction[1] == "-r":
            for item in reversed(list(os.listdir(self.currentDirectory))):
                print(item)
        else:
            for item in os.listdir(self.currentDirectory):
                print(item)
        print("")

    def cd(self,location):
        if location[0] == "..":
            currentDir = self.goBackOneLevel()
            print("You are in " + currentDir + " now.")
            self.currentDirectory = currentDir

        else:
            currentDir = self.currentDirectory
            newPath = FH.createDirectoryPath(currentDir,''.join(location))
            exists = FH.checkIfDirectoryExists(newPath)
            print("")

            if exists:
                self.currentDirectory = newPath
                print("You are in " + self.currentDirectory + " now.")
            else:
                print("Directory does not exist")


    def goBackOneLevel(self):
        atRootLevel = FH.isRootLevel(self.currentDirectory)

        if atRootLevel:
            print("You cannot go up, as you are in your home folder.")
        else:
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

