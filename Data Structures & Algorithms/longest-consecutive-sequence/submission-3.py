from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsDict = defaultdict(int)
        maxlen = 0

        # this solution is exactly what my own initial solution was
        # the indexing here solves the problems I had
        for num in nums:
            if numsDict[num] == 0:
                numsDict[num] = numsDict[num - 1] + numsDict[num + 1] + 1
                numsDict[num - numsDict[num - 1]] = numsDict[num]
                numsDict[num + numsDict[num + 1]] = numsDict[num]
                maxlen = max(maxlen, numsDict[num])
        return maxlen

        


        

        