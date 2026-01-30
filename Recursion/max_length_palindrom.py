"""Given a string S, the task is to find the length of the longest sub-string which is a palindrome
Examples: 

Input: S = "aaaabbaa" 
Output: 6 
Explanation: Sub-string "aabbaa" is the longest palindromic sub-string.

Input: S = "banana" 
Output: 5 
Explanation: Sub-string "anana" is the longest palindromic sub-string. """
def is_palindroms(s,start,end,count):
    if start >end:
        return count
    if start == end:
        return count + 1
    if s[start]==s[end]:
        return is_palindroms(s,start+1,end-1,count+2)
    else:
        return max(is_palindroms(s,start+1,end,count),is_palindroms(s,start,end-1,count))
def max_length_palindrom(s):
    n = len(s)
    return is_palindroms(s,0,n-1,0)
s = "aaaabbaa"
result = max_length_palindrom(s)
print(result)

