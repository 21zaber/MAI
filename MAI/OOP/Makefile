
OUT_FILE=lab

COMPILER=g++
OPTIONS=-std=gnu++11

CPP_FILES=$(wildcard src/*.cpp)

all:
	${COMPILER} ${OPTIONS} lab1.cpp ${CPP_FILES}

lab%.cpp: ;

lab%: lab%.cpp ${CPP_FILES} 
	${COMPILER} ${OPTIONS} -o ${OUT_FILE} $@.cpp ${CPP_FILES}

