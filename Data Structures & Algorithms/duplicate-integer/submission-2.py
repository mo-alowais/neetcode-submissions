class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = {}
        for i in nums:
            if i not in myDict:
                myDict[i] = 1
            else:
                return True
        return False
         