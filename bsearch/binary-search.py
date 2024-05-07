class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # init 2 pointers
        left = 0
        right = len(nums) - 1
        # traverse until pointers pass each other
        while left <= right:
            # calc optimal midpoint to prevent overflow
            mid = left + (right - left) // 2
            if target == nums[mid]:
                return mid
            # we want larger numbers here so chop off left half
            elif target > nums[mid]:
                left = mid + 1
            # we want smaller numbers here so chop off right half
            else:
                right = mid - 1
        # case where pointers pass each other and we still don't have a target
        return -1
