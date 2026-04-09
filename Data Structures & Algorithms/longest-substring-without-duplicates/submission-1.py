class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        i, j = 0, 1
        duplicate = set(s[0])
        tmp_ans = 1
        ans = 1
        while i < len(s) and j < len(s):
            if s[j] not in duplicate:
                duplicate.add(s[j]) 
                tmp_ans += 1
                ans = max(ans, tmp_ans)
                j += 1
            else:
                if j - i > 1:
                    duplicate.remove(s[i])
                    tmp_ans -= 1
                    i += 1
                else:
                    i = i + 1
                    j = j + 1
        return ans


        