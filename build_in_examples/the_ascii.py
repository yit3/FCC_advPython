#the ascii()

"""
ascii(obj, /)
    Return an ASCII-only representation of an object.

    As repr(), return a string containing a printable representation of an
    object, but escape the non-ASCII characters in the string returned by
    repr() using \\x, \\u or \\U escapes. This generates a string similar
    to that returned by repr() in Python 2.
"""

#As repr(), return a string containing a printable representation of an object,
# but escape the non-ASCII characters in the string returned by repr() using \x, \u or \U escapes.
# This generates a string similar to that returned by repr() in Python 2

num = [1, 2, 3, "*"]

print(ascii(num))
