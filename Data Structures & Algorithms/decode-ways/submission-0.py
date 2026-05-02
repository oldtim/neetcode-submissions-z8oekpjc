class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1 if int(s[0]) != 0 else 0
        
        dp1 = 1 if int(s[0]) != 0 else 0
        dp2 = 1 if int(s[0:2]) <= 26 and int(s[0]) != 0 else 0 # 錯誤1. 一開始寫成s[0:1]
        temp = 1 if dp1 and int(s[1]) != 0 else 0
        dp2 = dp2 + temp

        i = 2
        while i < len(s):
            #加入那位元形成1-digit case
            if int(s[i]) != 0:
                tmp1 = dp2
            else:
                tmp1 = 0
            
            #加入那位元和後面一位形成2-digit case
            if int(s[i-1:i+1]) <= 26 and int(s[i-1]) != 0:
                tmp2 = dp1
            else:
                tmp2 = 0
            
            dp1 = dp2
            dp2 = tmp2 + tmp1
            i += 1
        
        return dp2