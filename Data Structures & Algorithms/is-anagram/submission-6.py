class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s) :
            return False
        else:
            x = sorted(s);
            y = sorted(t);
            if x == y:
                return True
            else:
                return False
            



