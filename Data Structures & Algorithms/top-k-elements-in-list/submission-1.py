from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        top_k = []
        for _ in range(k):
            max_val = max(counts, key=lambda k: counts[k])
            top_k.append(max_val)
            del counts[max_val]

        return top_k