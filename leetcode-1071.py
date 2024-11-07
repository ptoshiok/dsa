class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str1) > len(str2)):
            s = str1
            t = str2
        else:
            s = str2
            t = str1
        if (t not in s):
            return ""
        else:
            commonDivisor = ""
            for i in range(1, len(t)+1):
                if ((len(s) % i != 0) | (len(t) % i != 0)):
                    continue
                if (((t[0:i]*int(len(s)/i)) == s) & ((t[0:i]*int(len(t)/i)) == t)):
                    commonDivisor = t[0:i]
            
            return commonDivisor

