class Solution:
    #python3.6以後可以用f-string

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            # 找到 '#' 分隔長度
            j = s.find('#', i)  #從ith開始，找下一個'#'
            length = int(s[i:j])
            # 讀字串內容
            word = s[j+1:j+1+length]
            ans.append(word)
            # 移動指標
            i = j + 1 + length
        return ans
