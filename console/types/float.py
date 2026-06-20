def float_(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        raise TypeError("Value should be float")
