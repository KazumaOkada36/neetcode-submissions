class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(num):
            if num in path:
                return False
            if num in completed:
                return True
            path.add(num)
            for requirement in prereq[num]:
                if not dfs(requirement):
                    return False
            path.remove(num)
            completed.add(num)
            return True
        prereq = {i: [] for i in range(numCourses)}
        for course, requirement in prerequisites:
            prereq[course].append(requirement)

        path = set()
        completed = set()
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
