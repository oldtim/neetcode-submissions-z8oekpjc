class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        charSet = set(s)  # 將string內元素(去掉重複)，造一個set

        for c in charSet:
            count = 0
            left = 0
            for right in range(len(s)):
                if s[right] == c:
                    count += 1

                while (right - left + 1) - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1

                ans = max(ans, right - left + 1)
        return ans
        