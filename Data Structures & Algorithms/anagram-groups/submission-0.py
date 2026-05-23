class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        uniques = [sorted(i) for i in strs]
        uniques = set([''.join(i) for i in uniques])
        myMap = {k:[] for k in uniques}
        for string in strs:
            key = ''.join(sorted(string))
            myMap[key].append(string)
        return(list(myMap.values()))
        
            


        