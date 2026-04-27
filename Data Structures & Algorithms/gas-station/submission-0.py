class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        trunk = 0
        flag = 0
        ans = -1
        for i in range(2*len(gas)):
            location = i % len(gas)
            trunk = trunk + gas[location] - cost[location] # >0 表示能夠去下一格
            if trunk < 0:
                trunk = 0
                flag = -1
            else:
                if flag == -1 and i < len(gas):
                    flag = location

            if flag != -1 and flag + len(gas) == i:
                ans = flag 
                break
        return ans


# 第二版還是出問題，問題在測試為:gas=[1,2,3] / cost=[2,3,2]，ans我傳2應該是-1，看起來是第二輪迴圈選到gas=3 ,cost=2後就停止出問題了
#，也就是說原本以為可以用第二個迴圈做確認，沒想到第二個迴圈本身也可以做選擇flag
            
            


        