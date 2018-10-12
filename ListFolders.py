import os
import shutil
from itertools import islice


class Actions:
    def __init__(self):

        homeFolder = os.getenv("HOME")
        self.currentDirectory = homeFolder


    def printCurrentDirectory(self):
        print(self.currentDirectory)

    def createDirectory(self, destination):
        newPath = os.path.join(self.currentDirectory, destination)
        return newPath

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

    def cd(self, instruction):
        newPath = (self.createDirectory((''.join(instruction[1:]))))
        print("")

        if os.path.isdir(newPath):
            self.currentDirectory = newPath
            print("You are in " + self.currentDirectory + " now")
        else:
            print("No such directory to step into, so you are in " + self.currentDirectory)
        print("")

    def together(self, file1, file2):
        path1 = self.currentDirectory + "\\" + file1
        path2 = self.currentDirectory + "\\" + file2
        try:
            with open("c.txt", "w") as catFile, open(path1, 'r') as f1, open(path2, 'r') as f2:
                for line in f1:
                    catFile.write(line)
                for line in f2:
                    catFile.write(line)

            with open("c.txt", "r") as catFile:
                for line in catFile:
                    print(line)
        except IOError or OSError:
            print("Please choose other files as I cannot find them!")

    def cat(self, file):
        if os.path.isfile(self.createDirectory(file)):
            newPathFile = self.createDirectory(file)
            with open(newPathFile, 'r') as f:
                for line in f:
                    print(line)
        else:
            print("This file does not exist.")

    def mkdir(self, name):
        newPath = self.createDirectory(name)
        if not os.path.exists(newPath):
            os.makedirs(newPath)
            print("Your new folder is ready! It is called " + name + " and is here: " + newPath)
        else:
            print("This folder already exists.")

    def rm(self, name):
        filePath = self.createDirectory(name)
        if os.path.isdir(filePath):
            shutil.rmtree(filePath)
            print("Folder " + name + " removed.")

        elif os.path.exists(filePath):
            os.remove(filePath)
            print("File " + name + " removed.")

        else:
            print("I cannot find this file or folder.")

    def head(self, file, linesNum):
        path = self.createDirectory(file)
        if os.path.exists(path):
            with open(path, "r") as f:
                for line in islice(f, int(linesNum)):
                    print(line)
        else:
            print("I cannot find this file.")



class CommandPrompt(Actions):
    def run(self):
        while True:
            self.printCurrentDirectory()
            command = input("What should I do? Type:" '\n'
                            "'ls' to see my content, " '\n'
                            "'ls -r' to see my content reversed, "  '\n'
                            "'cat <file>' to see the content of a text file, " '\n'
                            "'together <file1> <file2>' to put two text files together," '\n'
                            "'mkdir <name>' to create a folder, " '\n'
                            "'rm <name>' to delete a file or folder, " '\n'
                            "'head <file> <x>' to see the first x lines of a file, " '\n'
                            "'cd <somewhere>' to go somewhere, or " '\n'
                            "'exit' to...exit!: ")

            request = command.split()

            if request[0] == "ls":
                self.ls(request)

            if request[0] == "cd":
                self.cd(request)

            if request[0] == "together" and len(request) == 3:
                self.together(request[1], request[2])

            if request[0] == "cat" and len(request) == 2:
                self.cat(request[1])

            if request[0] == "mkdir" and len(request) == 2:
                self.mkdir(request[1])

            if request[0] == "rm" and len(request) == 2:
                self.rm(request[1])

            if request[0] == "head" and len(request) == 3:
                self.head(request[1], request[2])

            if command == "exit":
                break


def main():
    command = CommandPrompt()
    command.run()

if __name__ == "__main__":
    main()