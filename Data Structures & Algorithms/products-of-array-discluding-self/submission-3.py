class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        for i, outer_val in enumerate(nums):

            start_val = nums[i + 1] if i == 0 else nums[i - 1]
            total = start_val
            seen = False
            for j, inner_val in enumerate(nums):
                
                if i == j:
                    continue

                if not seen and inner_val == start_val:
                    seen = True
                    continue

                total *= inner_val
            
            result.append(total)
        return result