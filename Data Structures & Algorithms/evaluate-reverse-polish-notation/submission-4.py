from functools import reduce
import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        evalRst = 0
        temp = []
        for t in tokens:
            print(t)
            # using try/except to catch negative values
            try:
                t = int(t) 
                temp.append(t)
                if evalRst == 0: evalRst = t
            except ValueError:
                print(temp)
                y = temp.pop()
                x = temp.pop()
                
                if t == '+':
                    evalRst = x + y
                if t == '-':
                    evalRst = x - y
                if t == '*':
                    evalRst = x * y
                if t == '/':
                    evalRst = int(x / y)
                temp.append(evalRst)
            
        return evalRst

        