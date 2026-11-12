def countSubstrings(s: str):
    palindromes = []
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            if sub == sub[::-1]:
                palindromes.append(sub)
    return len(palindromes), palindromes

if __name__ == "__main__":
    for s in ["ababa", "racecar", "level"]:
        cnt, pals = countSubstrings(s)
        print(f"Input: {s} -> Total Count: {cnt}, Substrings: {pals}")
