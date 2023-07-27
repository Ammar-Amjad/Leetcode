def Mapping(c):
    mapping = {'1': 'A', '2': 'B', '3': 'C', '4': 'D', '5': 'E', '6': 'F', '7': 'G', '8': 'H', '9': 'I', '10': 'J', '11': 'K', '12': 'L', '13': 'M', '14': 'N', '15': 'O', '16': 'P', '17': 'Q', '18': 'R', '19': 'S', '20': 'T', '21': 'U', '22': 'V', '23': 'W', '24': 'X', '25': 'Y', '26': 'Z'}
    if c in mapping:
        return True
    else:
        return False


class Solution:
    def numDecodings(self, s: str) -> int:
        
        one_ahead = 1
        two_ahead = 0
        curr = 0
        
        for i in range(len(s) - 1, -1, -1):
            
            if Mapping(s[i]):
                if i + 1 < len(s) + 1:
                    curr += one_ahead
                
            if Mapping(s[i:i+2]):
                if i + 2 < len(s) + 1:
                    curr += two_ahead
            
            two_ahead = one_ahead
            one_ahead = curr
            curr = 0
            
        return one_ahead