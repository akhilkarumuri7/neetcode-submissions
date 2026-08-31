class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # nlogn time
        triplets = []

        for i in range(0, len(nums) - 2):
            curr = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if curr + nums[l] + nums[r] < 0:
                    l += 1
                elif curr + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    triplet = [curr, nums[l], nums[r]]
                    if triplet not in triplets:
                        triplets.append(triplet)
                    l += 1
        return triplets