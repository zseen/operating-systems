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

if request[0] == "cd..":
    self.goBackOneLevel()

if command == "exit":
    exit(0)



