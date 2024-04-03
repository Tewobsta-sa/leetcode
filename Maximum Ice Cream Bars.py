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
#we can work the sorting using the counting sort algorithm here is my code:
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        count=[0]*(max(costs)+1)
        for num in costs:
            count[num]+=1
        sorted_array = []
        for i in range(len(count)):
            sorted_array.extend([i]*count[i])
        cost = 0
        counter = 0
        for i in range(len(sorted_array)):
            cost += sorted_array[i]
            if cost <= coins:
               counter += 1
        return counter
