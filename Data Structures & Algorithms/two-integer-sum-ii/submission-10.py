class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        if len(numbers) == 2:
            return [1, 2]
        
        l = 0
        r = len(numbers) - 1
        while True:
            
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]

            if numbers[l] + numbers[r] < target:
                l += 1

            if numbers[l] + numbers[r] > target:
                r -= 1