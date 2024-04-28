def bracket_check(test_string):
    test_string = list(test_string)
    if test_string.count("(") != test_string.count(")"):
        return False
    else:
        while True:
            if "(" not in test_string and ")" not in test_string:
                return True
            if "(" in test_string and ")" in test_string:
                if test_string.index("(") > test_string.index(")"):
                    return False
                elif test_string.index("(") < test_string.index(")"):
                    test_string.remove("(")
                    test_string.remove(")")


def is_correct_mobile_phone_number_ru(number):
    number = ''.join(number.split())
    if not number:
        return False
    if not bracket_check(number):
        return False
    if number.count("(") > 1 or number.count(")") > 1:
        return False
    if not (number[0:2] == "+7" or number[0] == '8'):
        return False
    if number[0] == "8":
        number = number[1:]
        number = "+7" + number
    if "(" in number and (number[2] != "(" or number[6] != ")"):
        return False
    number = number.replace("-", "")
    number = number.replace("(", '').replace(")", '')
    check_num = number.replace("+", '')
    if len(check_num) == 11 and check_num.isdigit():
        return True
    return False


print("YES" if is_correct_mobile_phone_number_ru(input()) else "NO")
