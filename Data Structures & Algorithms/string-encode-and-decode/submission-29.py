class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string)) + "#" + string
        return encoded



    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            len_string = int(s[i:j])
            string = s[j+1:j+1+len_string]
            i = j + 1 + len_string
            decoded.append(string)
            
        return decoded


            



