class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {k:0 for k in set(nums)}
        for n in nums:
            m[n] +=1
        t = sorted(m.items(), key=lambda i: i[1], reverse=True)[:k]
        return [x[0] for x in t]
        