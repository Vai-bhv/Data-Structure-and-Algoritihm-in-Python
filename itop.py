def isOperator(c):
	return (not c.isdigit())

def getPriority(c):
	if c == '-' or c == '+':
		return 1
	elif c == '*' or c == '/':
		return 2
	return 0

def infixToPostfix(infix):
	infix = '(' + infix + ')'
	l = len(infix)
	char_stack = []
	output = ""

	for i in range(l):
		if infix[i].isdigit():
			output += infix[i] if ((i!=0) and infix[i-1].isdigit())  else " " + infix[i]
            # if (i!=0) and infix[i-1].isdigit():
            #     output += infix[i]    
            # else:
            #     output += infix[i]
            # if (i != 0 and infix[i-1].isdigit()):
            #     output += infix[i]
            # else:
            #     output += " " + infix[i]
			    
		elif infix[i] == '(':
			char_stack.append(infix[i])
		elif infix[i] == ')':
			while char_stack[-1] != '(':
				output += char_stack.pop()
			char_stack.pop()
		else:
			if isOperator(char_stack[-1]):
				while getPriority(infix[i]) < getPriority(char_stack[-1]):
					output += char_stack.pop()
				char_stack.append(infix[i])

	while len(char_stack) != 0:
		output += char_stack.pop()
	return output

def infixToPrefix(infix):
	l = len(infix)

	infix = infix[::-1]

	for i in range(l):
		if infix[i] == '(':
			infix[i] = ')'
		elif infix[i] == ')':
			infix[i] = '('

	prefix = infixToPostfix(infix)
	prefix = prefix[::-1]

	return prefix

s = input()
print(infixToPrefix(s))
