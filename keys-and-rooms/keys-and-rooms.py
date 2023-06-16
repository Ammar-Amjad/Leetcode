class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(idx):
            
            visited.add(idx)
            for nei in rooms[idx]:
                if nei not in visited:
                    dfs(nei)
        dfs(0)
        return len(visited) == len(rooms) 
        