# to ONP

VALUES = {'+': 1, '-': 1, '*': 2, '/': 2, ':': 2, '^': 3, '(': 0}


def value(sign):
    return VALUES[sign]


# FROM RPN
def from_rpn():
    inputFile = open('../1_2/from_rpn.txt', 'r')
    characters = inputFile.readline().strip().split(' ')
    stack = []
    for c in characters:
        if c.isnumeric():
            stack.append(c)
        else:
            result = f"( {stack[-2]} {c} {stack[-1]} )"
            stack.pop()
            stack.pop()
            stack.append(result)
    inputFile.close()
    outputFile = open('../1_2/from_rpn_output.txt', 'w+')
    outputFile.write(stack[0])
    outputFile.close()


# TO RPN
def to_rpn():
    inputFile = open('../1_2/to_rpn.txt', 'r')
    outputFile = open('../1_2/to_rpn_output.txt', 'w+')
    characters = inputFile.readline().split()
    inputFile.close()
    stack = []
    for c in characters:
        if c.isnumeric():
            outputFile.write(c + " ")
        else:
            if c == '(':
                stack.append(c)
            elif c == ')':
                while stack[-1] != '(':
                    outputFile.write(stack.pop() + " ")
                stack.pop()
            else:
                while True:
                    if len(stack) == 0 or int(value(stack[-1]) < value(c)):
                        stack.append(c)
                        break
                    else:
                        outputFile.write(stack.pop() + " ")
    while len(stack) != 0:
        outputFile.write(stack.pop() + " ")
    outputFile.write('\n')
    outputFile.close()


from_rpn()
to_rpn()
