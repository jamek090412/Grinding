from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        [1, n] inclusive : n+1 integers
        - without modifying the array
        - constant extra space
        """
        for i in range(len(nums)):
            """
            1. the 'number at index' has to be i+1
                otherwise, swap 
            2. if the number to be swapped is already in place, return 
            """
            while nums[i] != i+1:
                if nums[i] == nums[nums[i]-1]:
                    return nums[i]
                ind = nums[i]-1
                nums[i], nums[ind] = nums[ind], nums[i]
        return None