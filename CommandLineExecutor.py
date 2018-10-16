import os
from itertools import islice
import FilesystemHelpers as FH
from pathlib import Path




class CommandLineExecutor:
    def run(self):
        while True:
            print(FH.getHomeDirectory())
            command = input("What should I do? Type:" '\n'
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
                            "'exit' to...exit!: ")

            request = command.split()

            # if request[0] == "ls":
            #     self.ls(request)

            if request[0] == "cd":
                self.cd(request[1:])

    # def ls(self, instruction):
    #     print("")
    #     print("The content of " + self.currentDirectory + " is: ")
    #
    #     if len(instruction) == 2 and instruction[1] == "-r":
    #         for item in reversed(list(os.listdir(self.currentDirectory))):
    #             print(item)
    #     else:
    #         for item in os.listdir(self.currentDirectory):
    #             print(item)
    #     print("")

    def cd(self,location):
        currentDir = FH.getHomeDirectory()
        newPath = FH.createDirectoryPath(currentDir,''.join(location))
        exists = FH.checkIfDirectoryExists(newPath)

        print("")

        if exists:
            currentDir = newPath
            print("You are in " + newPath + " now.")
            return currentDir
        else:
            print("Directory does not exist")
    #
    #
    # def goBackOneLevel(self):
    #     if self.currentDirectory == str(Path.home()):
    #         print("You cannot go up, as you are in your home folder.")
    #     else:
    #         pathToModify = list(os.path.split(self.currentDirectory))
    #         pathToModify.pop()
    #         for directory in pathToModify:
    #             self.currentDirectory = str(directory)
    #
    # def joinTogether(self, file1, file2, file3):
    #     path1 = self.createDirectoryPath(file1)
    #     path2 = self.createDirectoryPath(file2)
    #     path3 = self.createDirectoryPath(file3)
    #
    #     if self.checkIfFileExists(path1) and self.checkIfFileExists(path2):
    #         with open(path3, "w") as catFile, open(path1, 'r') as f1, open(path2, 'r') as f2:
    #             for line in f1:
    #                 catFile.write(line)
    #             for line in f2:
    #                 catFile.write(line)
    #
    #         with open(path3, "r") as catFile:
    #             for line in catFile:
    #                 print(line)
    #
    # def printTogether(self, file1, file2):
    #     path1 = self.createDirectoryPath(file1)
    #     path2 = self.createDirectoryPath(file2)
    #
    #     if self.checkIfFileExists(path1) and self.checkIfFileExists(path2):
    #         with open(path1, "r") as f1, open(path2, "r") as f2:
    #             for line in f1:
    #                 print(line, end="")
    #             for line in f2:
    #                 print(line)
    #
    # def cat(self, file):
    #     if os.path.isfile(self.createDirectoryPath(file)):
    #         newPathFile = self.createDirectoryPath(file)
    #         with open(newPathFile, 'r') as f:
    #             for line in f:
    #                 print(line)
    #     else:
    #         print("This file does not exist.")
    #
    # def mkdir(self, name):
    #     newPath = self.createDirectoryPath(name)
    #     if not os.path.exists(newPath):
    #         os.makedirs(newPath)
    #         print("Your new folder is ready! It is called " + name + " and is here: " + newPath)
    #     else:
    #         print("This folder already exists.")
    #
    # def rm(self, name):
    #     filePath = self.createDirectoryPath(name)
    #     if self.checkIfFileExists(filePath):
    #         os.remove(filePath)
    #         print("File " + name + " removed.")
    #
    # def head(self, file, linesNum):
    #     path = self.createDirectoryPath(file)
    #     if os.path.exists(path):
    #         with open(path, "r") as f:
    #             for line in islice(f, int(linesNum)):
    #                 print(line)
    #     else:
    #         print("I cannot find this file.")



            # if request[0] == "joinTogether" and len(request) == 4:
            #     self.joinTogether(request[1], request[2], request[3])
            #
            # if request[0] == "printTogether" and len(request) == 3:
            #     self.printTogether(request[1], request[2])
            #
            # if request[0] == "cat" and len(request) == 2:
            #     self.cat(request[1])
            #
            # if request[0] == "mkdir" and len(request) == 2:
            #     self.mkdir(request[1])
            #
            # if request[0] == "rm" and len(request) == 2:
            #     self.rm(request[1])
            #
            # if request[0] == "head" and len(request) == 3:
            #     self.head(request[1], request[2])
            #
            # if request[0] == "cd..":
            #     self.goBackOneLevel()
            #
            # if command == "exit":
            #     exit(0)


def main():
    command = CommandLineExecutor()
    command.run()

if __name__ == "__main__":
    main()
