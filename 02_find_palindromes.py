def find_palindromes(m, n):
    return [i for i in range(m, n + 1) if str(i) == str(i)[::-1]]

if __name__ == "__main__":
    print("Example 1:", find_palindromes(10, 50))
    print("Example 2:", find_palindromes(100, 150))
    print("Example 3:", find_palindromes(1, 9))
