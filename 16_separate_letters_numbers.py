def separate_chars(s):
    letters = "".join([c for c in s if c.isalpha()])
    digits = "".join([c for c in s if c.isdigit()])
    return [letters, digits]

if __name__ == "__main__":
    print("Example 1:", separate_chars("a1b2c3d4"))
    print("Example 2:", separate_chars("x9y8z7"))
    print("Example 3:", separate_chars("12345"))
    print("Example 4:", separate_chars("abcdef"))
