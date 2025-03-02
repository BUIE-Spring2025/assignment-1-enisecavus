def int_to_roman(num):

        if num == 0:
        return ""
    elif 5 > num >= 1:
        if num == 4:
            num -= 4
            return "IV" + str(int_to_roman(num))
        else:
            num -= 1
            return "I" + str(int_to_roman(num))
    elif 10 > num >= 5:
        if num == 9:
            num -= 9
            return "IX" + str(int_to_roman(num))
        else:
            num -= 5
            return "V" + str(int_to_roman(num))
    elif 50 > num >= 10:
        if num >= 40:
            num -= 40
            return "XL" + str(int_to_roman(num))
        else:
            num -= 10
            return "X" + str(int_to_roman(num))
    elif 100 > num >= 50:
        if num>= 90:
            num -= 90
            return "XC" + str(int_to_roman(num))
        else:
            num -= 50
            return "L" + str(int_to_roman(num))
    elif 500 > num >= 100:
        if num == 400:
            num -= 400
            return "CD" + str(int_to_roman(num))
        else:
            num -= 100
            return "C" + str(int_to_roman(num))
    elif 1000 > num >= 500:
        if num >= 900:
            num -= 900
            return "CM" + str(int_to_roman(num))
        else:
            num -= 500
            return "D" + str(int_to_roman(num))
    elif num >= 1000:
            num -= 1000
            return "M" + str(int_to_roman(num))
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
