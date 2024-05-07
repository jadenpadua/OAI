class Solution:
    def isPalindrome(self, s: str) -> bool:
        # clean string by lowering it and removing alpha numeric chars
        lowered_string = s.lower()
        alpha_num_string = ''.join(char for char in lowered_string if char.isalnum())
        # two pointers on alpha num string
        left = 0
        right = len(alpha_num_string) - 1
        # keep checking equality until pointers meet
        while left <= right:
            if alpha_num_string[left] != alpha_num_string[right]:
                return False
            # move pointers
            left += 1
            right -= 1
        return True
