import Test

############################# ANSWER AREA ########################################

import string
from collections import Counter

ATOM, NUM, LPAR, RPAR = 0, 1, 2, 3

def parse_molecule (formula):
	tokens = list(get_tokens(formula))
	pos = 0
	stack = [Counter()]

	while pos < len(tokens):
		tok = tokens[pos]
		if tok[0] == ATOM:
			atom = tok[1]
			count = 1
			if pos+1 < len(tokens) and tokens[pos+1][0] == NUM:
				pos += 1
				count = tokens[pos][1]

			stack[-1][atom] += count
		elif tok[0] == LPAR:
			stack.append(Counter())
		elif tok[0] == RPAR:
			count = 1
			if pos+1 < len(tokens) and tokens[pos+1][0] == NUM:
				pos += 1
				count = tokens[pos][1]

			lastcounter = stack.pop(-1)
			merge_counter(stack[-1], lastcounter, count)

		pos += 1

	return stack[0]

def merge_counter(c1, c2, mul):
	for k, v in c2.iteritems():
		c1[k] += v * mul

def get_tokens(formula):
	pos = 0
	while pos < len(formula):
		c = formula[pos]
		if c in string.uppercase:
			pos += 1
			while pos < len(formula) and formula[pos] in string.lowercase:
				c += formula[pos]
				pos += 1
			yield (ATOM, c)
		elif c in string.digits:
			pos += 1
			while pos < len(formula) and formula[pos] in string.digits:
				c += formula[pos]
				pos += 1
			yield (NUM, int(c))
		elif c in '([{':
			pos += 1
			yield (LPAR, c)
		elif c in ')]}':
			pos += 1
			yield (RPAR, c)
		else:
			yield NotImplemented

############################# ANSWER AREA ########################################


def equals_atomically (obj1, obj2):
    if len(obj1) != len(obj2):
        return False
    for k in obj1:
        if obj1[k] != obj2[k]:
            return False
    return True

Test.expect(equals_atomically(parse_molecule("H2O"), {'H': 2, 'O' : 1}), "Should parse water")
Test.expect(equals_atomically(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2}), "Should parse magnesium hydroxide: Mg(OH)2")
Test.expect(equals_atomically(parse_molecule("K4[ON(SO3)2]2"), {'K': 4,  'O': 14,  'N': 2,  'S': 4}), "Should parse Fremy's salt: K4[ON(SO3)2]2")