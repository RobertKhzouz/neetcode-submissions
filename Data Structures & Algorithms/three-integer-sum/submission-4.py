class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)
        triples = []

        # [-4, -1, -1, 0, 1, 2]

        prev = None
        for i, num in enumerate(sorted_nums):

            if num == prev:
                continue

            l = i + 1
            r = len(sorted_nums) - 1
            prev_l = None
            prev_r = None

            while l < r:
                
                if sorted_nums[l] == prev_l:
                    l += 1
                    continue
                if sorted_nums[r] == prev_r:
                    r -= 1
                    continue

                if sorted_nums[l] + sorted_nums[r] == -num:
                    triples.append([sorted_nums[l], num, sorted_nums[r]])
                    prev_l = sorted_nums[l]
                    prev_r = sorted_nums[r]
                    r -= 1
                    l += 1
                elif sorted_nums[l] + sorted_nums[r] < -num:
                    prev_l = sorted_nums[l]
                    l += 1
                else:
                    prev_r = sorted_nums[r]
                    r -= 1

            prev = num

        return triples

            

