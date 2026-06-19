class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        pattern = ""

        def dfs(i, pattern):
            if i >= 2*n:
                if self.isValid(pattern) == True:
                    ret.append(pattern)
                return

            temp = pattern
            pattern += "("
            dfs(i+1, pattern)
            pattern = temp
            pattern += ")"
            dfs(i+1, pattern)

        dfs(0, "")
        return ret

    def isValid(self, pattern):
        st = []
        for letter in pattern:
            if letter == "(":
                st.append(letter)
            if letter == ")":
                if st == []:
                    return False
                st.pop()
        if st == []:
            return True
        return False

        

        