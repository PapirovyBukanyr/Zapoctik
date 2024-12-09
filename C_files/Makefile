# Nastaveni promennych
CC = gcc
CFLAGS = -Wall -Wextra -I.
TARGET = ..\\launcher.exe
SRCS = launcher.c pyc_killer.c
OBJS = $(SRCS:.c=.o)
RES = launcher.res


# Spusteni vseho
all: $(TARGET) clean


# Vytvoreni .exe souboru
$(TARGET): $(OBJS) $(RES)
	$(CC) $(CFLAGS) -o $@ $^


# Preklad .c souboru do .o souboru
%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<


# Preklad .rc souboru do .res souboru, aby se mohly pouzit ikony
$(RES): launcher.rc
	windres $< -O coff -o $@


# Smazani vsech .o a .res souboru
clean:
	del /q $(OBJS) $(RES)

