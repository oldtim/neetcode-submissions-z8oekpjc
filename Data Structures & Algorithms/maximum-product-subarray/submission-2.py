class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = []
        cur = []
        res = float('-inf')

#用0作分割點，切成好幾段list，分別存入A
        for num in nums:
            res = max(res, num)         #走完迴圈後，ans內已存了nums中最大的num，因此如果所有元素都<=0(無正數的nums)，此時ans已存入0
            if num == 0:
                if cur:
                    A.append(cur)
                cur = []
            else:
                cur.append(num)
        if cur:
            A.append(cur)

        for sub in A:                                #在存入A的每個sub-string中
            negs = sum(1 for i in sub if i < 0)       #算有多少負數在sub-string內
            prod = 1
            need = negs if negs % 2 == 0 else negs - 1 #*關鍵1.:如果負號# = 偶數，need = #，否則，need = #-1
            negs = 0
            j = 0      # 從index=0開始算sub-string

            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i] < 0:
                    negs += 1
                    while negs > need:    # *關鍵2:根據*關鍵1，基本發生在負號#為奇數case，若sub-string包含全部負數時，從前端index-j開始吐出元素並往前推進，直到吐出一個負數元素 
                        prod //= sub[j]   #從前端index-j開始吐出元素
                        if sub[j] < 0:    #如果吐出的是負數，則sub-list內部負數#-1(因此下一圈跳出while)
                            negs -= 1
                        j += 1            #sub-list的前端因此往前推進
                if j <= i:                #只要沒有發生前端j-index超過後端i-index的情況(比如negs=1、need=0時，nums[0]=負數的情況，此時在i還沒從0更新到1前，j已經在回圈內更新到1)
                    res = max(res, prod)

        return res
    
    # 這方法也太多補丁，還是看dp的解答八