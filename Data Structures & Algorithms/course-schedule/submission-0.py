class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #一開始自己寫。沒想出來
        # syllabus = [0]*numCourses
        # for i in range(len(prerequisites)):
        #     #題目給條件: 0 <= a[i], b[i] < numCourses，所以以下判斷不用
        #     # if prerequisites[i][1] < numCourses and prerequisites[i][0] >= numCourses:
        #     #     return False
        #     # if prerequisites[i][1] < numCourses:
            
        #     syllabus[prerequisites[i][1]] = 1
        #     syllabus[prerequisites[i][0]] = -1
            
        # 我沒想明白的部分。先建立對照表:{課程:先修課程s}
        # 當時思考糾結在這種對照關係有可能一對多也可能多對一，但其實多對一(多個課程有同樣的先修課程)不重要
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        # visiting是訪問中，也就是*訪問結束後，要從中移除
        visiting = set()

        def dfs(crs):
            if crs in visiting:    # Cycle detected
                return False
            if preMap[crs] == []:  # 代表沒有先修要求
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)  # *訪問結束後，沒觸發return False=確定這一條鏈沒問題，要從visiting中移除
            preMap[crs] = []      # 同時將這門課程標註為[]，其他鏈的先修課程是這門課的話，可直接return True，不需要跑後續，節省時間複雜度
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True

#想不出來，直接看解答