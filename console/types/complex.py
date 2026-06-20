def complex_(value):
    try:
        return complex(value)
    except (ValueError, TypeError):
        raise TypeError("Value should be complex")
