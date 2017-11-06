#!/usr/bin/env python3

import operator
import readline 
import sys
from termcolor import colored, cprint

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		inp = input('rpn calc> ')
		result = calculate(inp)
		text = ""
		for inp in inp.split(" "):
			if inp == "+" or inp == "-" or inp == "*" or inp == "/":
				text += colored(inp, 'green') + " "
			else:
				text += inp + " "
		print(text)	 
		if result < 0:
			text = colored("Result:" + str(result), 'red', attrs=['bold'])
			print(text)
		else:
			text = colored("Result:" + str(result), 'blue')
			print(text)

if __name__ == '__main__':
	main()
