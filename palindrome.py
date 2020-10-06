'''
python program to get a factorial of number
''' 
#function which checks if reverse and original strings are equal
def isPalindrome(s):
    return s == s[::-1]

# main function
if __name__ == "__main__":
    s = 'racecar'
    ans = isPalindrome(s)
    if ans :
        print('Yes')
    else:
        print('No')