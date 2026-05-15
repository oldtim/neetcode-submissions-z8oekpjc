class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        # temp = 0
        first = 0
        last = len(heights) - 1
        while first < last:
            temp = min(heights[first], heights[last])*(last - first)
            ans = max(ans, temp)
            if heights[first] < heights[last]:
                first += 1
            else:
                last -= 1
        
        return ans


            

        

        


        