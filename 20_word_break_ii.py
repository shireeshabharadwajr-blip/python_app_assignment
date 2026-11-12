def wordBreak(s, wordDict):
    wordSet = set(w.lower() for w in wordDict)
    memo = {}
    def dfs(sub):
        if sub in memo: return memo[sub]
        if not sub: return [[]]
        res = []
        for word in wordSet:
            if sub.lower().startswith(word):
                for next_words in dfs(sub[len(word):]):
                    res.append([sub[:len(word)]] + next_words)
        memo[sub] = res
        return res
    segs = [" ".join(words) for words in dfs(s)]
    return len(segs) > 0, segs

if __name__ == "__main__":
    print("Example 1:", wordBreak("AmritaMysuru", ["Amrita", "Rita", "Mysuru"]))
    print("Example 2:", wordBreak("applepenapple", ["apple", "pen"]))
    print("Example 3:", wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
    print("Example 4:", wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
