import os


class Actions:
    def __init__(self):
        self.currentDirectory = "C:\\Users"

    def printCurrentDirectory(self):
        print(self.currentDirectory)

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
        newPath = self.currentDirectory + "\\" + ' '.join(instruction[1:])
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
        if os.path.isfile(self.currentDirectory + "\\" + file):
            newPathFile = self.currentDirectory + "\\" + file
            with open(newPathFile, 'r') as f:
                for line in f:
                    print(line)
        else:
            print("This file does not exist.")

    def mkdir(self, name):
        newpath = self.currentDirectory + "\\" + name
        if not os.path.exists(newpath):
            os.makedirs(newpath)
            print("Your new folder is ready! It is called " + name + " and is here: " + newpath)
        else:
            print("This folder already exists.")


class CommandPrompt(Actions):
    def run(self):
        while True:
            self.printCurrentDirectory()
            command = input("What should I do? Type:" '\n'
                            "'ls' to see my content, " '\n'
                            "'ls -r' to see my content reversed, "  '\n'
                            "'cat <file>' to open a text file, " '\n'
                            "'together <file1> <file2>' to put two text files together," '\n'
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

            if request[0] == "mkdir":
                self.mkdir(request[1])

            if command == "exit":
                break


def main():
    command = CommandPrompt()
    command.run()

if __name__ == "__main__":
    main()