class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
             count[c] = count.get(c, 0) + 1

        for c in t:
             if c not in count:
                return False
             count[c] -= 1
             if count[c] == 0:
                del count[c]

        return not count
#正確寫法如上，建立hash table，val等於個數，如此O(N)

##以下寫法時間複雜度出問題，首先是在t中每一個元素都要去掃描temp，時間複雜度=O(N^2)
##其次.remove一次也是O(N)，在t迴圈中也是O(N^2)
        # if len(s) != len(t):
        #     return False
        # temps = list(s)
        # for j in t:
        #     if j not in temps:
        #         return False
        #     else:
        #         temps.remove(j)
        # if temps:
        #     return False
        # else:
        #     return True