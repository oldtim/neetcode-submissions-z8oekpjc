class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] = count[i] + 1
        ans = []

        ##第一次寫看錯題目，還以為是>k的都回傳
        # for key,v in count.items():
        #     if v >= k:
        #         ans.append(key)
        
        # Sort the dictionary items by frequency in descending order
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        # Take the first k elements from the sorted list
        for i in range(k):
            ans.append(sorted_items[i][0])
        return ans

            
        