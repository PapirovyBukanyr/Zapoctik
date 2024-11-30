CC = gcc
CFLAGS = -Wall -Wextra -I.
TARGET = ..\\launcher.exe
SRCS = launcher.c pyc_killer.c
OBJS = $(SRCS:.c=.o)
RES = launcher.res

all: $(TARGET)

$(TARGET): $(OBJS) $(RES)
	$(CC) $(CFLAGS) -o $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

$(RES): launcher.rc
	windres $< -O coff -o $@

clean:
	del /q $(OBJS) $(RES)

.PHONY: all clean
