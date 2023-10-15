def is_string_integer(char):
    """
    return whether the char is a valid integer in base 10

    Args:
        char(string): The input

    Returns:
        Boolean: Whether ths string is integer
    """

    if len(char) != 1:
        return False
    if char.isdigit():
        return True
    else:
        return False
