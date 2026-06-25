class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n = len(isConnected)
        parent = list(range(n))
        self.province = n

        def find(city):
            while city != parent[city]:
                city = parent[city]
            return city
        
        def union(a,b):
            x, y = find(a), find(b)
            print(f" A: {a}. , B: {b}")
            print(f"Parents are {x}.   {y}")
            print(parent)
            if x!=y:
                parent[x] = y
                self.province -=1

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i,j)
                    print("After ", parent)
        
        return self.province