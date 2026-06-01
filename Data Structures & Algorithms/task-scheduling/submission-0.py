class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1  # ord()是用來取得字元的UniCode編碼值

        maxf = max(count)
        maxCount = 0
        for i in count:
            maxCount += 1 if i == maxf else 0

        time = (maxf - 1) * (n + 1) + maxCount # + maxCount，是因為有同樣maxf的task，最後一點不會被包含在(maxf - 1) * (n + 1)裡面，會黏在最末位後
        return max(len(tasks), time)



# 初始想法: 設共有CHAR x種，有兩種可能: 1. x<=n，要花時間 = 最多重複的x# * n。 2. x>n，....想不出
# 看解答: 我的初始想法跟解答中，Math解法類似，至少在時間由最多重複的x#主導時，要看time的部分是一致
# ，但為何解答說若tasks#(即我說的x)>time時，則由len(tasks)主導，這我不懂

        