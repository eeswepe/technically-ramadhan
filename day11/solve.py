def zero(param=None):
    if param is None:
        return 0
    else:
        return eval("0" + param)


def one(param=None):
    if param is None:
        return 1
    else:
        return eval("1" + param)


def two(param=None):
    if param is None:
        return 2
    else:
        return eval("2" + param)


def three(param=None):
    if param is None:
        return 3
    else:
        return eval("3" + param)


def four(param=None):
    if param is None:
        return 4
    else:
        return eval("4" + param)


def five(param=None):
    if param is None:
        return 5
    else:
        return eval("5" + param)


def six(param=None):
    if param is None:
        return 6
    else:
        return eval("6" + param)


def seven(param=None):
    if param is None:
        return 7
    else:
        return eval("7" + param)


def eight(param=None):
    if param is None:
        return 8
    else:
        return eval("8" + param)


def nine(param=None):
    if param is None:
        return 9
    else:
        return eval("9" + param)


def plus(param):
    str_action = "+" + str(param)
    return str_action


def minus(param):
    str_action = "-" + str(param)
    return str_action


def times(param):
    str_action = "*" + str(param)
    return str_action


def divided_by(param):
    str_action = "/" + str(float(param))
    return str_action
