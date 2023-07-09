class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        arr = []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        if len(digits) == 0:
            return ""
        def dfs(ic, string):
            for s in dic[digits[ic]]:
                if ic + 1 == len(digits):
                    arr.append(string + s)
                else:
                    dfs(ic + 1, string + s)

        dfs(0, "")

        return arr