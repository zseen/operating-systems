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
        try:
            newPath = self.currentDirectory + "\\" + file
            with open(newPath, 'r') as f:
                for line in f:
                    print(line)
        except FileNotFoundError:
            print("This file does not exist.")


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

            if request[0] == "together":
                if len(request) == 3:
                    self.together(request[1], request[2])
                elif len(request) == 2:
                    print("I think you mean 'cat <file>.'")
                else:
                    print("Please give me TWO files.")

            if request[0] == "cat":
                if len(request) == 2:
                    self.cat(request[1])
                elif len(request) == 3:
                    print("I think you are looking for 'together <file1> <file2>'")
                else:
                    print("Please give me ONE file, so that I can show you its content.")

            if command == "exit":
                break


def main():
    command = CommandPrompt()
    command.run()

if __name__ == "__main__":
    main()