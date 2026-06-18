class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        lookups = {}

        for i, num in enumerate(nums):
            lookups[num] = i

        for i, num in enumerate(nums):
            lookup = target - num
            if lookup in lookups:
                j = lookups[lookup]
                if i == j:
                    continue
                return [i, j] if i < j else [j, i]
