class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parent  = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(a,b):
            parent[find(a)] = find(b)

        for i, j in edges:
            if find(i) == find(j):
                return [i,j]
            union(i,j)
        return 