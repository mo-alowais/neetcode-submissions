class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        myStack = []
        rst = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            while myStack and v > myStack[-1][1]: 
                prev_idx, prev_val = myStack.pop()
                rst[prev_idx] = i - prev_idx 
            myStack.append((i, v))
        return rst





        