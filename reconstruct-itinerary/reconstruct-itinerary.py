class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        n = len(tickets)
        
        tickets.sort()
        
        adj_list = {src: [] for src, dst in tickets} 
        
        for src, dst in tickets:
            adj_list[src].append(dst)
            
        res = ['JFK']
        
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            
            if src not in adj_list:
                return False
            
            temp = list(adj_list[src])
            for i, v in enumerate(temp):
                adj_list[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                adj_list[src].insert(i, v)
                res.pop()
                
            return False
        
        dfs('JFK')
        return res