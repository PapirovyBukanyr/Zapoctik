# Nastaveni promennych
CC = gcc
CFLAGS = -Wall -Wextra -I.

# Promenne pro launcher.exe
TARGET = ..\\launcher.exe
SRCS = launcher.c pyc_killer.c
OBJS = $(SRCS:.c=.o)
RES = launcher.res

# Promenne pro generate_documentation.exe
TARGET2 = ..\\generate_documentation.exe
SRCS2 = generate_documentation.c
OBJS2 = $(SRCS2:.c=.o)


# Spusteni vseho
all: $(TARGET) $(TARGET2) clean


# Vytvoreni launcher.exe souboru
$(TARGET): $(OBJS) $(RES)
	$(CC) $(CFLAGS) -o $@ $^


# Vytvoreni generate_documentation.exe souboru
$(TARGET2): $(OBJS2)
	$(CC) $(CFLAGS) -o $@ $^


# Preklad .c souboru do .o souboru
%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<


# Preklad .rc souboru do .res souboru, aby se mohly pouzit ikony
$(RES): launcher.rc
	windres $< -O coff -o $@


# Smazani vsech .o a .res souboru
clean:
	del /q $(OBJS) $(RES) $(OBJS2)

