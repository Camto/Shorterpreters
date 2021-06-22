program = input()

tape = [0]
cell_index = 0

user_input = []
loop_table = {}

loop_stack = []
for ip, instruction in enumerate(program):
	if instruction == "[":
		loop_stack.append(ip)
	elif instruction == "]":
		loop_beginning_index = loop_stack.pop()
		loop_table[loop_beginning_index] = ip
		loop_table[ip] = loop_beginning_index

ip = 0
while ip < len(program):
	instruction = program[ip]
	
	if instruction == "+":
		tape[cell_index] += 1
		if tape[cell_index] == 256:
			tape[cell_index] = 0
	elif instruction == "-":
		tape[cell_index] -= 1
		if tape[cell_index] == -1:
			tape[cell_index] = 255
	elif instruction == "<":
		cell_index -= 1
	elif instruction == ">":
		cell_index += 1
		if cell_index == len(tape):
			tape.append(0)
	elif instruction == ".":
		print(chr(tape[cell_index]), end="")
	elif instruction == ",":
		if user_input == []:
			user_input = list(input() + "\n")
		tape[cell_index] = ord(user_input.pop(0))
	elif instruction == "[":
		if not tape[cell_index]:
			ip = loop_table[ip]
	elif instruction == "]":
		if tape[cell_index]:
			ip = loop_table[ip]
	
	ip += 1