class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + str(len(i)) + "#"
            encoded = encoded + i
        return encoded

    def decode(self, s: str) -> List[str]:
        out_str = []
        idx = 0
        while idx < len(s):
            j = idx 
            while s[j] != '#':
                j += 1
            length = int(s[idx:j])
            idx = j + 1
            j = idx + length
            out_str.append(s[idx:j])
            idx = j
        return out_str