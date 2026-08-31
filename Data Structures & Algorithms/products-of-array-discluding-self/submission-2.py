class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix, postfix = [1] * len(nums), [1] * len(nums)

        for i in range(len(nums) - 1):
            prefix[i + 1] = nums[i] * prefix[i]

        total = 1
        for j in range(len(nums) - 1, -1, -1):
            postfix[j] = total * prefix[j]
            total *= nums[j]
        
        return postfix

