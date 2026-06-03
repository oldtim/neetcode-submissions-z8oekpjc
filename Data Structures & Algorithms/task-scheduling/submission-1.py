class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks) # count[i] = ('ith_char':次數)
        maxHeap = [-cnt for cnt in count.values()] # count.value()是把每個char的次數輸出成list
        heapq.heapify(maxHeap)

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while maxHeap or q:   # 有未處理的char時，進入下一個time frame處理
            time += 1

            if not maxHeap:                      # 如果剩下char都處於idle狀態，time直接跳到第一個q解除idle的時刻
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxHeap) + 1 # cnt(個別char次數)為了maxHeap轉成負數，所以+1
                if cnt:                          # cnt未歸零之前，pop之後重新貼回q(等待cool down序列)
                    q.append([cnt, time + n])
            if q and q[0][1] == time:            # q內的
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    
    # 看解答，maxHeap解法的思路:用時間流控制。可以避開Greedy和Math不懂之處
        