class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for char in strs:
            temp_key = ''.join(sorted(char))
            # sorted出來是list，需用.join結合回char，''是指結合之間無其他字元
            if temp_key not in count:
                count[temp_key] = [char]
            else:
                count[temp_key].append(char)
        ans = []
        for v in count.values():
            ans.append(v)
        return ans
     