class Solution:
    def sortString(self,str):
         return ''.join(sorted(str))
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict = {}
        res=[]
        
        for str in strs:
            ss = self.sortString(str)
            if ss in dict:
                dict[ss].append(str)
            else:
                dict[ss]=[str]
        
        for li in dict:
            res.append(dict[li])
        return res