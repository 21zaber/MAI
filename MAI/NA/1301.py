from copy import deepcopy as copy




class SLE():
    def __init__(self, m = None, b = None):
        self.m = m
        self.b = b
        
    def mprint(self):
        for i in range(self.rank):
            print ' '.join(list(map(lambda s: str(s).rjust(4), self.m[i]))), '|', str(self.b[i]).rjust(4)


    def fread(self, filename):
        fin = open(filename, "r")

        self.rank = int(fin.readline())

        self.m = []
        self.b = []

        for i in range(self.rank):
            l = list(map(int, fin.readline().split()))
            self.m.append(l[:-1])
            self.b.append(l[-1])

        fin.close()

    def seidel(self, eps):
        x = [0 for i in range(self.rank)]
        iteration = -1
	fout = open("outseidel", "w")
        while True:
            iteration += 1
            if iteration > 10 ** 8:
                break

            
            prev = copy(x)
            for i in range(self.rank):
                var = sum([self.m[i][j] * x[j] for j in range(i)])
                var += sum([self.m[i][j] * prev[j] for j in range(i + 1, self.rank)])
                x[i] = (self.b[i] - var) / self.m[i][i]
	    
	    fout.write("Iteration " + str(iteration).rjust(4) + ":" + str(x) + "\n")
            
            if sum([(x[i] - prev[i]) ** 2 for i in range(self.rank)]) < eps:
                break
	fout.close()
	return x

    def simpleiter(self, eps):
        x = [0 for i in range(self.rank)]
        prev = copy(x)
	iteration = -1

	fout = open("outsimple", "w")

	while True:
	    iteration += 1
            if iteration > 10 ** 6:
		break

	    for i in range(self.rank):
                x[i] = self.b[i]
		for j in range(self.rank):
		    if i != j:
			x[i] -= self.m[i][j] * prev[j]
		x[i] /= self.m[i][i]
	    
	    fout.write("Iteration " + str(iteration).rjust(4) + ":" + str(x) + "\n")

            if sum([(x[i] - prev[i]) ** 2 for i in range(self.rank)]) < eps:
                break

	    prev = copy(x)
	fout.close()
	return x
	    




m = SLE()

filename = raw_input("Enter file name: ")

m.fread(filename)
print "Matrix"
m.mprint()
eps = float(raw_input("Enter epsilon: "))

print "Seidel method:"
print "Answer: ", m.seidel(eps)
print "Simple iteration method:"
print "Answer: ", m.simpleiter(eps)
