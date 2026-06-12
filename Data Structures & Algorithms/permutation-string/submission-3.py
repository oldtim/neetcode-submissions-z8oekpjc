class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dict_s1 = Counter(s1)
        count = len(s1)
        #dict_surplus = {}
        for i in range(len(s1)):
            if s2[i] in dict_s1:
                if dict_s1[s2[i]] > 0:
                    count -= 1 
                dict_s1[s2[i]] -= 1       
        if count == 0:
            return True

        j = len(s1)
        while j < len(s2):
            if s2[j] in dict_s1:
                if dict_s1[s2[j]] > 0:
                    count -= 1
                dict_s1[s2[j]] -= 1

                if s2[j-len(s1)] in dict_s1:
                    dict_s1[s2[j-len(s1)]] += 1
                    if dict_s1[s2[j-len(s1)]] > 0:
                        count += 1
            if count == 0:
                return True
            j += 1

        return False



        