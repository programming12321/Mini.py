def string(value):
    if isinstance(value, str):
        return value
    raise TypeError("Value should be string")
