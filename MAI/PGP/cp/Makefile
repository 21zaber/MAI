OBJECTS = gpu.o cp.o

CC= nvcc
FLAGS=  -x cu -arch=sm_20 -I. -dc -lpthread -lGL -lGLU -lglut -lGLEW
FILES= cp.cu gpu.cu
TARGET= cp
LOG= log

%.o: %.cu
	${CC} ${FLAGS} $< -o $@

all: $(OBJECTS)
	${CC} -arch=sm_20 $(OBJECTS) -o ${TARGET}

clean:
	rm -f *.o ${TARGET} ${LOG}

run:
	./${TARGET} > ${LOG}
