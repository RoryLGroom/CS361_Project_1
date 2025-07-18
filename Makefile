# compiler options
CXXFLAGS = -g -Wall -Wextra
CXXFLAGS += -std=c++17 -pedantic -pedantic-errors
CXXFLAGS += -Wfloat-equal -Wredundant-decls -Wshadow -Wconversion

# list .h files here
HEADERS =

# list .cpp files here
PROGRAM_FILES = main.cpp functions.cpp 
SHARED_FILES = 

.PHONY: all
all: program.exe

.PHONY: program.exe # Always force rebuild of program
program.exe: $(PROGRAM_FILES) $(SHARED_FILES) $(HEADERS)
	$(CXX) $(CXXFLAGS) $(PROGRAM_FILES) $(SHARED_FILES) -o $@

.PHONY: clean
clean:
	rm -f program.exe
