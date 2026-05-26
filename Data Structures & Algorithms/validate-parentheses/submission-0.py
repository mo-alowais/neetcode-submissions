class Solution:
    def isValid(self, s: str) -> bool:

        myStack = list()
        openchars = ['{', '[', '(',]
        closedchars = ['}', ']', ')']
        myMap = dict(zip(openchars, closedchars)) # initially these were frozensets but they don't preserve order which causes issues

        for c in s:
            if c in openchars: myStack.append(c); continue
            elif c in closedchars:
                if len(myStack) > 0 and c == myMap[myStack[-1]]: 
                    myStack.pop() 
                    continue
                else: return False # cannot have a closing without opening
        return len(myStack) == 0