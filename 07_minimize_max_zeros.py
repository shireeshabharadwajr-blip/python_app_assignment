import itertools

def minimize_zeros(L, K):
    zeros = L - K
    strings = sorted(set("".join(p) for p in itertools.permutations('1' * K + '0' * zeros)), reverse=True)
    results = []
    min_zero_block = L + 1
    
    for s in strings:
        max_z = max((len(group) for group in s.split('1')), default=0)
        results.append((s, max_z))
        if max_z < min_zero_block:
            min_zero_block = max_z
            
    optimal = [s for s, mz in results if mz == min_zero_block]
    return results, optimal, min_zero_block

if __name__ == "__main__":
    res, opt, min_z = minimize_zeros(4, 2)
    print("Possible Strings:", res)
    print("Optimal Arrangement(s):", opt)
    print("Minimum Longest Zero Block:", min_z)
