def postfix_to_prefix(postfix):
    stack = []
    operators = set(['+', '-', '*', '/', '^'])

    for char in postfix:
        if char not in operators:
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(char + operand1 + operand2)

    return stack.pop()




postfix = '1-2-33'
prefix = postfix_to_prefix(postfix)
print(prefix) 
