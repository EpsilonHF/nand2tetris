

class CodeWriter:

    def __init__(self, filename):

        self.file = open(filename, 'w')

    def writeArithmetic(self, command):
        """
        Write arithmetic assembly code to file

        Args:
            command[string]
        """
        func = {
            "add": self._add,
            "sub": self._sub,
            "neg": self._neg,
            "eq":  self._eq,
            "gt":  self._gt,
            "lt":  self._lt,
            "and": self._and,
            "or":  self._or,
            "not": self._not,
        }
        
        method = func[command]
        method()


    def WritePushPop(self, command, segment, index):
        """
        Write push or pop assembly code to file

        Args:
            command[string]
            segment[string]
            index[int]
        """
        if command == "push":
            pass
        else:
            pass

    def _add(self):
        self._a_command('0')
        self._c_command('M', 'M-1')
        self._c_command('A', 'M')
        self._c_command('D', 'M')
        self._c_command('A', 'A-1')
        self._c_command('M', 'D+M')


    def _sub(self):
        self._a_command('0')
        self._c_command('M', 'M-1')
        self._c_command('A', 'M')
        self._c_command('D', 'M')
        self._c_command('A', 'A-1')
        self._c_command('M', 'M-D')

    def _neg(self):
        pass

    def _eq(self):
        pass

    def _gt(self):
        pass

    def _lt(self):
        pass

    def _and(self):
        self._a_command('0')
        self._c_command('M', 'M-1')
        self._c_command('A', 'M')
        self._c_command('D', 'M')
        self._c_command('A', 'A-1')
        self._c_command('M', 'D&M')

    def _or(self):
        self._a_command('0')
        self._c_command('M', 'M-1')
        self._c_command('A', 'M')
        self._c_command('D', 'M')
        self._c_command('A', 'A-1')
        self._c_command('M', 'D+M')

    def _not(self):
        self._a_command('0')
        self._c_command('A', 'A-1')
        self._c_command('M', '!M')


    def _a_command(self, address):
        self.file.write('@'+address+'\n')

    def _c_command(self, dest, comp, jump = None):
        if dest:
            self.file.write(dest+'=')
        self.file.write(comp+'\n')

    def close(self):
        self.file.close()
