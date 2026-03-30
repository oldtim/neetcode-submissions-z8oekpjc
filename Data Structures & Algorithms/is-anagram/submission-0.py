class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temps = list(s)
        for j in t:
            if j not in temps:
                return False
            else:
                temps.remove(j)
        if temps:
            return False
        else:
            return True