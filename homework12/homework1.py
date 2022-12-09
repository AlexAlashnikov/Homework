class InputFormulaError(Exception):
    pass

class InputNumberError(Exception):
    pass

class InputOperatorError(Exception):
    pass


operators = ('+', '-', '*', '/', '**')
while True:
    try:
        user_input = input('Введите числа или quit: ')
        if user_input == 'quit':
            break
        else:
            value1, operator, value2 = user_input.split(' ')
    except Exception as e:
        raise InputFormulaError
    try:
        value1, value2 = int(value1), int(value2)
    except Exception as e:
        raise InputNumberError
    if operator not in operators:
        raise InputOperatorError
    else:
        if operator == '+':
            result = value1 + value2
            print(result)
        elif operator == '-':
            result = value1 - value2
            print(result)
        elif operator == '*':
            result = value1 * value2
            print(result)
        elif operator == '/':
            result = value1 / value2
            print(result)
        elif operator == '**':
            result = value1 ** value2
            print(result)