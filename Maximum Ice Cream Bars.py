class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        cost = 0
        counter = 0
        for i in range(len(costs)):
            cost += costs[i]
            if cost <= coins:
               counter += 1
        return counter
