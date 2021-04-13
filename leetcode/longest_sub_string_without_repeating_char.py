class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        max_len = 0
        cur_len = 0
        sub_start = 0
        
        for i,char in enumerate(s):
            
            if char in dict and dict[char] >= sub_start:
                sub_start = dict[char]+1
                cur_len = i - dict[char]
            else:
                cur_len += 1
                if max_len < cur_len:
                    max_len = cur_len
                    
            dict[char]=i
        
        return max_len