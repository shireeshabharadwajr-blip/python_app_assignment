def transform_string(s, sub):
    transformed_sub = "".join(chr(ord(c) - 1) if c != 'a' else 'z' for c in sub)
    return s.replace(sub, transformed_sub, 1)

if __name__ == "__main__":
    print("Example 1:", transform_string("hackerrank", "hack"))
    print("Example 2:", transform_string("programming", "gram"))
    print("Example 3:", transform_string("apple", "a"))
