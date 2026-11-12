def filter_chars(target, reference):
    ref_set = set(reference)
    return "".join(c for c in target if c not in ref_set)

if __name__ == "__main__":
    print("Example 1:", filter_chars("programming", "grm"))
    print("Example 2:", filter_chars("hello world", "lo"))
    print("Example 3:", filter_chars("abcdef", "xyz"))
