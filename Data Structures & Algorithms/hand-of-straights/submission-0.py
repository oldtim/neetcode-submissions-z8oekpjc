class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = Counter(hand) # *新函數
        hand.sort()
        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True

# 看解答，學到*新函數:Counter()，是計算list內重複數並形成hash map
#        案例: arr = [1,1,2,3,3,3] 
#              count = Counter(arr)
#        結果: count = {1: 2, 2: 1, 3: 3}



        