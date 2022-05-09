def to_pascal(string: str) -> str:
    """General method that takes in a string and converts it to a PascalCase String with uppercase after each dash

    Args:
        string: a string that will contain each field for each model's field name that will be converted back and forth

    Returns:
        : String that is converted to PascalCase
    """
    return "".join(word.capitalize() for word in string.split("_"))


def to_camel(string: str) -> str:
    """General method that takes in a string and converts it to a CamelCase String with uppercase after each dash

    Args:
        string: a string that will contain each field for each model's field name that will be converted back and forth

    Returns:
        : String that is converted to CamelCase
    """
    pascal = "".join(word.capitalize() for word in string.split("_"))
    return pascal[0].lower() + pascal[1:]
