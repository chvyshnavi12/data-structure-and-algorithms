def evaluation(expr):
    def calc(x, y, ope):
        if ope == '+':
            return x + y
        if ope == '-':
            return x - y
        if ope == '*':
            return x * y
        if ope == '/':
            return x / y

    operators = ['+', '-', '*', '/']
    stack = []

    for char in expr:
        if char in operators:
            y = stack.pop()
            x = stack.pop()
            stack.append(calc(x, y, char))
        else:
            stack.append(int(char))

    return stack[0]  # final result

print(evaluation("23+"))  # Output: 5
