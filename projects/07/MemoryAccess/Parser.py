

class Parser:
    
    def __init__(self, filename):
        """
        parse the vm command to assembly code
        """
        self.name = filename
        self.file = open(self.name, 'r')
        self.allcommands = iter(self.file.readlines())
        self.tokens = None


    def advance(self):
        """
        load next command in vm file, if to EOF, close the file
        """
        while True:

            try: 
                command = next(self.allcommands).strip()
                if len(command) == 0: continue
                if command[0] == '/': continue
                if '/' in command:
                    command = command.split("//")[0].strip()
                self.tokens = command.split()

                return True

            except StopIteration:
                self.file.close()

                return False


    def commandType(self):
        """
        Judge the type of current command
        """
    
        command_types = {
            "label":    "C_LABEL",
            "function": "C_FUNCTION",
            "return":   "C_RETURN",
            "goto":     "C_GOTO",
            "if-goto":  "C_IF",
            "push":     "C_PUSH",
            "pop":      "C_POP",
            "call":     "C_CALL",
            "add":      "C_ARITHMETIC",
            "sub":      "C_ARITHMETIC",
            "neg":      "C_ARITHMETIC",
            "eq":       "C_ARITHMETIC",
            "gt":       "C_ARITHMETIC",
            "lt":       "C_ARITHMETIC",
            "and":      "C_ARITHMETIC",
            "or":       "C_ARITHMETIC",
            "not":      "C_ARITHMETIC",
        }
        
        return command_types[self.tokens[0]]


    def arg1(self):
        if self.commandType() == "C_ARITHMETIC":
            return self.tokens[0]
        else:
            return self.tokens[1]


    def arg2(self):
        return int(self.tokens[2])
