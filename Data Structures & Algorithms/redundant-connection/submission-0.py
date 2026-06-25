class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        parent  = list(range(n))

        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        
        def union(a,b):
            m, n = find(a), find(b)
            if m != n:
                parent[m] = n
            

        for i, j in edges:
            if find(i) == find(j):
                return [i,j]
            union(i,j)
        return 