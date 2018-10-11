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
        with open("c.txt", "r+") as catFile:
            with open(self.currentDirectory + "\\" + file1, 'r') as f1:
                with open(self.currentDirectory + "\\" + file2, 'r') as f2:
                    for line in f1:
                        catFile.write(line)
                        print(line)
                    for line in f2:
                        catFile.write(line)
                        print(line)
            for line in catFile:
                print(line)

    def cat(self, file):
        previousDirectory = self.currentDirectory
        try:
            self.currentDirectory += "\\"
            self.currentDirectory += file
            with open(self.currentDirectory, 'r') as f:
                for line in f:
                    print(line)
            self.currentDirectory = previousDirectory

        except FileNotFoundError:
            print("This file does not exist.")
            self.currentDirectory = previousDirectory



class CommandPrompt(Actions):

    def runCommand(self):
        while True:
            self.printCurrentDirectory()
            command = input("What should I do? Type:" '\n'
                            "'ls' to see my content, " '\n'
                            "'ls -r' to see my content reversed, "  '\n'
                            "'openfile <file>' to open a text file, " '\n'
                            "'cat <file1> <file2>' to put two text files together," '\n'
                            "'cd <somewhere>' to go somewhere, or " '\n'
                            "'exit' to...exit!: ")

            request = command.split()

            if request[0] == "ls":
                self.ls(request)

            if request[0] == "cd":
                self.cd(request)

            if request[0] == "together":
                self.together(request[1], request[2])

            if request[0] == "cat":
                self.cat(request[1])

            if command == "exit":
                break


def main():
    command = CommandPrompt()
    command.runCommand()

if __name__ == "__main__":
    main()