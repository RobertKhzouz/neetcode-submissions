class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix = []
        suffix = []
        results = []

        for i, num in enumerate(nums):

            if i == 0:
                prefix.append(None)
            else:
                prev = prefix[i - 1] if prefix[i - 1] is not None else 1
                prefix.append(prev * prev_num)

            prev_num = num

        for j in range(len(nums) - 1, -1, -1):

            if j == len(nums) - 1:
                suffix.append(None)
            else:
                prev = suffix[len(nums) - j - 2] if suffix[len(nums) - j - 2] is not None else 1
                suffix.append(prev * prev_num)
            
            prev_num = nums[j]

        print(prefix)
        print(suffix)

        for i in range(len(nums)):
            j = len(nums) - 1 - i
            if prefix[i] is not None and suffix[j] is not None:
                results.append(prefix[i] * suffix[j])
            elif prefix[i] is not None:
                results.append(prefix[i])
            elif suffix[j] is not None:
                results.append(suffix[j])
            else:
                results.append(0)
    
        return results