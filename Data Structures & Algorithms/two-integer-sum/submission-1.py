class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i , num in enumerate(nums):
            res = target - num
            if res in hash:
                return [hash[res],i]
            hash[num] = i