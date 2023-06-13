class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for s in strs:
            ss = ''.join(sorted(s)) 
            if ss not in dic:
                dic[ss] = [s]
            else:
                dic[ss].append(s)
        
        res = []
        for k in dic:
            res.append(dic[k])
            
        return res