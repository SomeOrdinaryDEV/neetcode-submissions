class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for i in strs:
            string = string + str(len(i)) + "#" + i
        return string

    def decode(self, s: str) -> List[str]:
        l = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            string = s[j+1:j+1+length]
            l.append(string)
            i = j + 1 + length
        return l




#["Hello","World"]
# 5#Hello5#World