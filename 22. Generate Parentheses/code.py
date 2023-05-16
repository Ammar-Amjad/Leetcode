class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        Parans = []
        def dfs(Str, left_count, right_count):
            if len(Str) == 2 * n:
                Parans.append(Str)
                return
            if left_count < n:
                dfs(Str + "(", left_count + 1, right_count) 
            if right_count < left_count:
                dfs(Str + ")", left_count, right_count + 1)                                

        dfs("", 0, 0)
        return Parans