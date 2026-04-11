class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        tmp_stack = []
        i = 0
        while i < len(temperatures):
            if not tmp_stack:
                tmp_stack.append(i)
                i += 1
                continue

            if temperatures[i] <= temperatures[tmp_stack[-1]]:
                tmp_stack.append(i)
                i += 1
            else:
                j = tmp_stack.pop()
                result[j] = i - j
        
        return result



                


        