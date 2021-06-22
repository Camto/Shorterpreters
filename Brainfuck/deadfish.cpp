#include <iostream>
#include <string>

int main() {
	std::string program;
	std::cin >> program;
	
	int accumulator = 0;
	
	for(char instruction : program) {
		switch(instruction) {
			case 'i':
				accumulator += 1;
				break;
			case 'd':
				accumulator -= 1;
				break;
			case 's':
				accumulator *= accumulator;
				break;
			case 'o':
				std::cout << accumulator << std::endl;
				break;
		}
		
		if(accumulator == 256 || accumulator == -1) {
			accumulator = 0;
		}
	}
}