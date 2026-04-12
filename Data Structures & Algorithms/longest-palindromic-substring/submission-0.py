class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        max_str = s[0]
        id_stack = []
        id_stack_type2 = []
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                id_stack.append(i)
            if i+1 < len(s) and s[i-1] == s[i+1]:
                id_stack_type2.append(i)
        
        while id_stack:
            tmp_id = id_stack.pop()
            id_top = tmp_id 
            id_bottom = tmp_id -1
            while id_top < len(s) and id_bottom >= 0:
                if s[id_top] != s[id_bottom]:
                    break
                if id_top - id_bottom + 1 > max_len:
                    max_len = id_top - id_bottom + 1
                    max_str = s[id_bottom : (id_top+1)]    
                id_top += 1
                id_bottom -= 1  
        
        while id_stack_type2:
            tmp_id = id_stack_type2.pop()
            id_top = tmp_id + 1
            id_bottom = tmp_id -1
            while id_top < len(s) and id_bottom >= 0:
                if s[id_top] != s[id_bottom]:
                    break
                if id_top - id_bottom + 1 > max_len:
                    max_len = id_top - id_bottom + 1
                    max_str = s[id_bottom : (id_top+1)]    
                id_top += 1
                id_bottom -= 1                
                
                
        
        return max_str

#第一次寫，錯誤認知迴文的核心一定是兩個重複char相鄰，其實還有另一種是以單一char的核心
#放棄此版，重新寫



        