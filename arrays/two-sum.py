class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumToFindMap = {}
        for i in range(len(nums)):
            sumToFind = target - nums[i]
            # case where current nums[i] satisfies number to find, so return here
            if nums[i] in sumToFindMap:
                return [sumToFindMap[nums[i]], i]
            sumToFindMap[sumToFind] = i
