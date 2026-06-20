def integer(num):
    if isinstance(num, int):
        return num

    if isinstance(num, str) and num.lstrip("+-").isdigit():
        return int(num)

    raise TypeError("Number should be integer")
