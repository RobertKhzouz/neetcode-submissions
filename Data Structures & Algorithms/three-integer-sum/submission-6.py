class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        sorted_nums = sorted(nums)
        triples = []

        for i, num in enumerate(sorted_nums):

            if i > 0 and num == sorted_nums[i - 1]:
                continue

            l, r = i + 1, len(sorted_nums) - 1

            while l < r:

                three_sum = sorted_nums[l] + sorted_nums[r] + num
                if three_sum == 0:
                    triples.append([sorted_nums[l], num, sorted_nums[r]])
                    l += 1
                    while sorted_nums[l] == sorted_nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1

        return triples

            

