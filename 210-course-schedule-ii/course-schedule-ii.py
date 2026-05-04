class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        indeg=[0]*numCourses
        for u,v in prerequisites:
            adj[v].append(u)
            indeg[u]+=1
        q=[]
        for i in range(numCourses):
            if indeg[i]==0:
                q.append(i)
        res=[]
        while q:
            node=q.pop(0)
            res.append(node)
            for nei in adj[node]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    q.append(nei)
        if len(res) == numCourses:
            return res
        else:
            return []
        
        