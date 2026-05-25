from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        seqlen = 0
        if len(nums) > 0: maxlen = 1
        else: maxlen = 0
        for i in numset:
            if i - 1 not in numset and i + 1 in numset:
                # seq start
                j = i + 1
                while (j in numset): j +=1
                seqlen = j - i 
                if seqlen > maxlen: maxlen = seqlen
                seqlen = 0
        return maxlen


        

        