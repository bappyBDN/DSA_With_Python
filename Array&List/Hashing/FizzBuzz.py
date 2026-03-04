"""Given an integer n, for every positive integer i <= n, the task is to print,

"FizzBuzz" if i is divisible by 3 and 5,
"Fizz" if i is divisible by 3,
"Buzz" if i is divisible by 5
"i" as a string, if none of the conditions are true.
Examples:

Input: n = 3
Output: ["1", "2", "Fizz"]

Input: n = 10
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]

Input: n = 20
Output: ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"]"""
#[Brute Force Approach] - O(n) Time and O(n) Space
def fizz_buzz(n):
    result=[]
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            result.append("FizzBuzz")
        elif i%3==0:
            result.append("Fizz")
        elif i%5==0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
#[Better Approach] By String Concatenation - O(n) Time and O(n) Space
def fizz_buzz_string(n):
    result=[]
    for i in range(1,n+1):
        s=""
        if i%3==0:
            s+="Fizz"
        if i%5==0:
            s+="Buzz"
        if s=="":
            s=str(i)
        result.append(s)
    return result
#hash_map={"Fizz":3,"Buzz":5}
def fizz_buzz_hash(n):
    result=[]
    hash={"Fizz":3,"Buzz":5}
    for i in range(1,n+1):
        s=""
        for key in hash:
            if i%hash[key]==0:
                s+=key
        if s=="":
            s=str(i)
        result.append(s)
    return result
if __name__ == "__main__":

    n=3
    print("FizzBuzz for n =", n, ":", fizz_buzz(n))
    print("FizzBuzz (String Concatenation) for n =", n, ":", fizz_buzz_string(n))
    print
    n=10
    print("FizzBuzz for n =", n, ":", fizz_buzz(n))
    n=20
    print("FizzBuzz for n =", n, ":", fizz_buzz(n))
    print("FizzBuzz (String Concatenation) for n =", n, ":", fizz_buzz_string(n))
    print("FizzBuzz (Hashing) for n =", n, ":", fizz_buzz_hash(n))