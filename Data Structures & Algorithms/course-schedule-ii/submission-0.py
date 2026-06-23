class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        order = []
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visit, cycle = set(), set()
        def dfs(i):
            if i in cycle:
                return False
            if i in visit:
                return True
            cycle.add(i)

            for pre in preMap[i]:
                if not dfs(pre):
                    return False
            cycle.remove(i)
            visit.add(i)
            order.append(i)
            return True
        


        for i in range(numCourses):
            if not dfs(i):
                return []
        return order