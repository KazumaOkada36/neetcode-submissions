class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(n):
            if n in path:
                return False
            if n in visited:
                return True
            path.add(n)
            for requirement in prereq[n]:
                if not dfs(requirement):
                    return False
            path.remove(n)
            visited.add(n)
            result.append(n)
            return True

            
        prereq = {i: [] for i in range(numCourses)}
        for course, requirement in prerequisites:
            prereq[course].append(requirement)
        
        visited = set()
        path = set()
        result = []
        for course in range(numCourses):
            if not dfs(course):
                return []
        return result