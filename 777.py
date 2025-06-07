def handle_1962_case_1964(x):
    if x[0] == "REBOL":
        return 0
    elif x[0] == "KIT":
        return 1
    elif x[0] == "SCALA":
        return 2


def handle_1962_case_1983(x):
    if x[1] == "GN":
        return 3
    elif x[1] == "YACC":
        return 4
    elif x[1] == "GRACE":
        return 5


def handle_1962_case_1967(x):
    if x[1] == "GN":
        return 6
    elif x[1] == "YACC":
        return 7
    elif x[1] == "GRACE":
        return 8


def handle_1962(x):
    if x[2] == 1964:
        return handle_1962_case_1964(x)
    elif x[2] == 1983:
        return handle_1962_case_1983(x)
    elif x[2] == 1967:
        return handle_1962_case_1967(x)


def handle_1965(x):
    if x[0] == "KIT":
        return 12
    elif x[0] == "SCALA":
        return 13
    elif x[0] == "REBOL":
        if x[1] == "GN":
            return 9
        elif x[1] == "YACC":
            return 10
        elif x[1] == "GRACE":
            return 11


def main(x):
    if x[3] == 1962:
        return handle_1962(x)
    if x[3] == 1975:
        return 14
    if x[3] == 1965:
        return handle_1965(x)