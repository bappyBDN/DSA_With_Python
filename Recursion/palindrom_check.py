
def is_palindrome(s,l,r):
    if l>=r:
        return True
    if s[l]!=s[r]:
        return False
    return is_palindrome(s,l+1,r-1)

# Example usage:
string ="Bappy"
print(is_palindrome(string,0,len(string)-1))  
string2 ="madam"
if is_palindrome(string2,0,len(string2)-1):
    print(f"{string2} is a palindrome")
else:
    print(f"{string2} is not a palindrome")
    