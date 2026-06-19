class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i=0
        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            string_len = int(s[i:j])
            string = s[j+1:j+1+string_len]
            decoded.append(string)
            i = j + string_len + 1
        return decoded

