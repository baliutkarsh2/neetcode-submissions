class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "0"
        
        encoded_str = ""
        for string in strs:
            encoded_str = encoded_str + string + "-"
        encoded_str = encoded_str[:len(encoded_str)-1]
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return [""]
        if s == "0":
            return []
        
        return s.split("-")
