class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []
        results = []

        for i, num in enumerate(nums):

            if i == 0:
                prefix.append(1)
            else:
                prev = prefix[i - 1]
                prefix.append(prev * prev_num)

            prev_num = num

        for j in range(len(nums) - 1, -1, -1):

            if j == len(nums) - 1:
                suffix.append(1)
            else:
                prev = suffix[len(nums) - j - 2]
                suffix.append(prev * prev_num)
            
            prev_num = nums[j]

        for i in range(len(nums)):
            j = len(nums) - 1 - i
            results.append(prefix[i] * suffix[j])
    
        return results