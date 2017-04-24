
lab.cu: lab
	true

lab:
	nvcc -Werror cross-execution-space-call -lm  lab.cu -o lab

test.cu:
	nvcc -Werror cross-execution-space-call -lm  test.cu -o test

gpg:
	rm -f lab.cu.asc
	gpg -ba lab.cu

all: lab.cu
	true

run: lab.cu test.cu
#   ./lab < min.txt
#   ./test < kin.txt
#   ./converter.py mout.jpg.bin
#   ./converter.py kout.jpg.bin

	
