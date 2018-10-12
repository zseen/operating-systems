import os

class CommandPrompt:
    def __init__(self):
        self.currentDirectory = "C:\\Users"
        print(self.currentDirectory)

    def runCommand(self):
        while True:
            command = input("What should I do? Type 'ls' to see my content, 'cd <somewhere>' to go somewhere  or 'exit' to...exit!: ")

            if command == "ls":
                print(os.listdir(self.currentDirectory))

            goToLocation = command.split()
            if goToLocation[0] == "cd":
                self.currentDirectory += "\\"
                self.currentDirectory += ' '.join(goToLocation[1:])
                print("You are in " + self.currentDirectory+ " now")




            if command == "exit":
                break




def main():
    command = CommandPrompt()
    command.runCommand()

if __name__ == "__main__":
    main()