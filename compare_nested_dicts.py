# Comparing Nested Dictionaries
def compare_nested_dicts(d1, d2):
    """
    Compares two nested dictionaries recursively for equality.

    Args:
        d1: First dictionary or value.
        d2: Second dictionary or value.

    Returns:
        bool: True if they are equal, False otherwise.
    """
    if type(d1) != type(d2):
        return False

    if isinstance(d1, dict):
        if set(d1.keys()) != set(d2.keys()):
            return False
        for key in d1:
            if not compare_nested_dicts(d1[key], d2[key]):
                return False
        return True

    # For non-dict values
    return d1 == d2
