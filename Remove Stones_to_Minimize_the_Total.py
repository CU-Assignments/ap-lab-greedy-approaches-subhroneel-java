class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        total_sum = 0
        max_heap = []
        for num in piles:
            max_heap.append(-num)
            total_sum += num
        
        heapq.heapify(max_heap)

        res = 0
        while k > 0 and max_heap:
            heap_value = -heapq.heappop(max_heap)
            operated_value = (heap_value) // 2
            
            if operated_value > 0:
                heapq.heappush(max_heap, -(heap_value - operated_value))
           
            res += operated_value                      
            k -= 1

        return total_sum - res