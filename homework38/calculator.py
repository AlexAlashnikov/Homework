import operator


def calculator(param1, param2, param3):
    try:
        operation, *args = param1, param2, param3
        args = list(map(float, args))
        function = operator.methodcaller(operation, *args)
        value = function(operator)
    except Exception as e:
        value = ''
    return value
