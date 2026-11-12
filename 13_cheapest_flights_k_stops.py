def findCheapestPrice(n, flights, src, dst, k):
    prices = [float('inf')] * n
    prices[src] = 0
    for _ in range(k + 1):
        tempPrices = prices.copy()
        for u, v, w in flights:
            if prices[u] != float('inf') and prices[u] + w < tempPrices[v]:
                tempPrices[v] = prices[u] + w
        prices = tempPrices
    return prices[dst] if prices[dst] != float('inf') else -1

if __name__ == "__main__":
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    print("Example 1:", findCheapestPrice(4, flights, 0, 3, 1))
