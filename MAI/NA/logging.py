
class log():
    def __init__(self, filename, verb = True):
        self.fout = open(filename , 'w')
        self.verb = verb

    def write(self, s):
        s = str(s)
        if self.verb:
            print(s)
        self.fout.write(s + '\n')

    def fwrite(self, s):
        s = str(s)
        print(s)
        self.fout.write(s + '\n')
