# Last updated: 3/24/2025, 10:46:26 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        def palindrome(s:str):
            if len(s) in [0,1]:
                return True
            length = len(s) - 1
            for i in range(len(s)//2):
                if s[i] != s[length - i]:
                    return False
            return True


        
        s = s.strip()
        clean_s = ''.join([x.lower() for x in list(s) if x.isalnum()])
        return palindrome(clean_s)
