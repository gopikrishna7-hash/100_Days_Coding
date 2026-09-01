# Leetcode first occurrence of word
# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, or -1 
# if needle is not part of haystack.

def strStr(haystack, needle):
        len_h=len(haystack)
        len_n=len(needle)

        if len_n ==0 or needle=="":
            return 0
        i=0
        for i in range((len_h-len_n)+1):
            if haystack[i:i+len_n]==needle:
                return i

        return -1
res=strStr("SAdsadness","sad")
print(res)