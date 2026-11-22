class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[]for _ in range(numCourses)]
        visiting=set()
        visited=set()
        for course,preq in prerequisites:
            adj[course].append(preq)
        def dfs(course):
            if course in visiting :
                return False
            if course in visited:
                return True 
            visiting.add(course)
            for neighbor in adj[course]:
                if not dfs(neighbor):
                    return False
            visiting.remove(course)
            visited.add(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False 
        return True