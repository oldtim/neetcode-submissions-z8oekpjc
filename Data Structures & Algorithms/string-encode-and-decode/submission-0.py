
class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for char in strs:
            n = len(char)
            ans = ans + str(len(char)) + "#" + char
            #ex:['my','way'] -> [2#my3#way]
        return ans



    def decode(self, s: str) -> List[str]:
        index_len = []
        tmp_ans = ""
        ans = []
        sign = 0
        for char in s:
            if sign == 0:
                if char != "#":
                    index_len.append(char)
                else:
                    sign = int("".join(index_len))
                    index_len = []
                    if sign == 0:
                        ans.append("")
            else:
                tmp_ans += char
                sign -= 1
                if sign == 0:
                    ans.append(tmp_ans)
                    tmp_ans = ""

        return ans

        
