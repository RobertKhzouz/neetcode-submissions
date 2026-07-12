class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        triples = []

        for i, num in enumerate(nums):

            if i > 0 and num == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:

                three_sum = nums[l] + nums[r] + num
                if three_sum == 0:
                    triples.append([nums[l], num, nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1

        return triples

            

