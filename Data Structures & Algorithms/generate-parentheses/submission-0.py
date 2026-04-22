class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        tmp_char = []
        def dfs(left_sign, right_sign):
            if left_sign == n:
                ans_char = tmp_char.copy()
                for _ in range(n - right_sign):
                    ans_char.append(")")
                ans.append("".join(ans_char))   # 不需要用tmp_char.copy()，因為.join已創造跟tmp_char(mutable)不同的另一個字串(immutable)
                return
            tmp_char.append("(")
            dfs(left_sign + 1, right_sign)
            tmp_char.pop()
            if left_sign > right_sign:
                tmp_char.append(")")
                dfs(left_sign, right_sign + 1)
                tmp_char.pop()
        dfs(0,0)
        return ans





