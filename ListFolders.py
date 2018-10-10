import os


class Actions:
    def __init__(self):
        self.currentDirectory = "C:\\Users"
        print(self.currentDirectory)

    def ls(self, instruction):
        print("")
        print("The content of " + self.currentDirectory + " is: ")

        if len(instruction) == 1 or instruction[1] == "/W":
            print(', '.join(os.listdir(self.currentDirectory)))

        elif instruction[1] == "/D":
            for item in os.listdir(self.currentDirectory):
                print(item)
        print("")

    def cd(self, instruction):
        directoryBeforeChange = self.currentDirectory
        self.currentDirectory += "\\"
        self.currentDirectory += ' '.join(instruction[1:])
        path = self.currentDirectory
        if os.path.isdir(path):
            print("You are in " + self.currentDirectory + " now")
        else:
            self.currentDirectory = directoryBeforeChange
            print("No such directory to step into, I will return to " + self.currentDirectory)

    def cat(self, file1, file2):
        with open("c.txt", "w") as catFile:
            with open(self.currentDirectory + "\\" + file1, 'r') as f1:
                with open(self.currentDirectory + "\\" + file2, 'r') as f2:
                    for line in f1:
                        catFile.write(line)
                    for line in f2:
                        catFile.write(line)
            for line in catFile:
                print(line)

    def openFile(self, file):
        self.currentDirectory += "\\"
        self.currentDirectory += file
        with open(self.currentDirectory, 'r') as f:
            for line in f:
                print(line)



class CommandPrompt(Actions):

    def runCommand(self):
        while True:
            command = input("What should I do? Type 'ls /W' to see my content horizontally, 'ls /D' to see my content vertically, 'cd <somewhere>' to go somewhere  or 'exit' to...exit!: ")

            request = command.split()

            if request[0] == "ls":
                self.ls(request)

            if request[0] == "cd":
                self.cd(request)

            if request[0] == "cat":
                self.cat(request[1], request[2])

            if request[0] == "openFile":
                self.openFile(request[1])

            if command == "exit":
                break


def main():
    command = CommandPrompt()
    command.runCommand()

if __name__ == "__main__":
    main()