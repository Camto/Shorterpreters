program = input()

accumulator = 0

for instruction in program:
	if instruction == "i":
		accumulator += 1
	elif instruction == "d":
		accumulator -= 1
	elif instruction == "s":
		accumulator **= 2
	elif instruction == "o":
		print(accumulator)
	
	if accumulator == 256 or accumulator == -1:
		accumulator = 0