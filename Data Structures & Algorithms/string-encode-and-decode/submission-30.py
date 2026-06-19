class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded



    def decode(self, s: str) -> List[str]:
        decoded = []

        cur = 0
        while cur < len(s):
            i = cur
            while s[i] != "#":
                i+=1
            string_len = int(s[cur:i])
            string = s[i+1:i+1+string_len]
            decoded.append(string)
            cur = i+1+string_len
        return decoded


            



