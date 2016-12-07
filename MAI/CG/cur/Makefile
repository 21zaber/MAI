NAME = water
CC = g++
RM = rm -f
SRC	= main.c noise.c
CFLAGS = -std=c++11 -Wall -W -Werror
IFLAGS = -I /usr/include -I /usr/include/GL -I /usr/X11R6/include -I /usr/X11R6/include/GL
LFLAGS = -L/usr/lib	-L/usr/X11R6/lib -lX11 -lGL -lGLU -lglut -ljpeg
OBJ	= $(SRC:.c=.o)

all: $(NAME)
$(NAME): $(OBJ)
	$(CC) $(OBJ) $(LFLAGS) -o $(NAME)
.c.o:
	$(CC) $(CFLAGS) $(IFLAGS) $< -c -o $@
clean:
	$(RM) $(OBJ)
	$(RM) $(NAME)
