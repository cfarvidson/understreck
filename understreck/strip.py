def strip(text):
    """Remove indents from multi-line strings

    Example:

        to_strip = '''This is a
        multi-line
        string'''

        strip(to_strip) == "This is a\nmulti-line\nstring"

    :param text: The string to strip indents from
    :return: A string with the indents removed
    """
    return "\n".join([line.strip() for line in text.split("\n")])
