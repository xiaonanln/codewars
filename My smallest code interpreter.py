import Test

######################################## ANSWER AREA ########################################

def brain_luck(code, input):
	Q = [0] * 1000000
	output = ''
	dp = 0
	pc = 0
	# > increment the data pointer (to point to the next cell to the right).
	# < decrement the data pointer (to point to the next cell to the left).
	# + increment (increase by one, truncate overflow: 255 + 1 = 0) the byte at the data pointer.
	# - decrement (decrease by one, treat as unsigned byte: 0 - 1 = 255 ) the byte at the data pointer.
	# . output the byte at the data pointer.
	# , accept one byte of input, storing its value in the byte at the data pointer.
	# [ if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.
	# ] if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching [ command.

	while pc < len(code):
		c = code[pc]
		pc += 1
		if c == '>':
			dp += 1
		elif c == '<':
			dp -= 1
		elif c == '+':
			Q[dp] = (Q[dp] + 1) % 256
		elif c == '-':
			Q[dp] = (Q[dp] - 1) % 256
		elif c == '.':
			output += chr(Q[dp])
		elif c == ',':
			ic, input = input[0], input[1:]
			Q[dp] = ord(ic)
		elif c == '[':
			if Q[dp] == 0:
				depth = 1
				while depth > 0:
					c = code[pc]
					if c == '[':
						depth += 1
					elif c == ']':
						depth -= 1
					else:
						pass

					pc += 1

		elif c == ']':
			if Q[dp] != 0:
				pc -= 2
				depth = 1
				while depth > 0:
					c = code[pc]
					if c == '[':
						depth -= 1
					elif c == ']':
						depth += 1
					else:
						pass

					pc -= 1
				pc += 2
		else:
			raise ValueError(c)

	return output

######################################## ANSWER AREA ########################################

# Echo until byte(255) encountered
Test.assert_equals(
  brain_luck(',+[-.,+]', 'Codewars' + chr(255)),
  'Codewars'
);

# Echo until byte(0) encountered
Test.assert_equals(
  brain_luck(',[.[-],]', 'Codewars' + chr(0)),
  'Codewars'
);

# Two numbers multiplier
Test.assert_equals(
  brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)),
  chr(72)
)