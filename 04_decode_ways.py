def decode_ways(s):
    if not s or s[0] == '0': return 0, []
    res = []
    def backtrack(idx, path):
        if idx == len(s):
            res.append("".join(path))
            return
        if s[idx] != '0':
            backtrack(idx + 1, path + [chr(64 + int(s[idx]))])
        if idx + 1 < len(s) and 10 <= int(s[idx:idx+2]) <= 26:
            backtrack(idx + 2, path + [chr(64 + int(s[idx:idx+2]))])
    backtrack(0, [])
    return len(res), res

if __name__ == "__main__":
    for test in ["12", "226", "11106", "06"]:
        ways, patterns = decode_ways(test)
        print(f"Input: {test} -> Total Ways: {ways}, Decoded Strings: {patterns if patterns else 'None'}")
