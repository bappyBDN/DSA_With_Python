"""Given a string S, the task is to remove all its adjacent duplicate characters recursively.

Examples: 

Input: S = "geeksforgeek"
Output: "gksforgk"
Explanation: g(ee)ksforg(ee)k -> gksforgk

Input: S = "abccbccba"
Output: ""
Explanation: ab(cc)b(cc)ba->abbba->a(bbb)a->aa->(aa)->"" (empty string)"""
 
def rremove(s):
    # Initialize result string
    sb = ""
    # Get the size of the input string
    n = len(s)

    # Iterate over the length of current string
    i = 0
    while i < n:
        # Flag to check if the current character
        # is repeated
        repeated = False

        # Check if the current characte
        # r is the same as the next one
        while i + 1 < n and s[i] == s[i + 1]:
            # Mark as repeated
            repeated = True
            # Skip the next character since
            # it's a duplicate
            i += 1

        # If the character was not repeated, 
        # add it to the result string
        if not repeated:
            sb += s[i]
        i += 1

    # If no changes were made, return the result
    # string
    if n == len(sb):
        return sb
    # Otherwise, recursively call the function \
    # to check for more duplicates
    return rremove(sb)

s = "geeksforgeek"
result = rremove(s)
print(result)