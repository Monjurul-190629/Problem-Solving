
def valid_palindrome(s):
    str1 = ""
    for ch in s:
        if(ch.isalnum()):
          str1 += ch.lower()
    str2 = str1[::-1]
    if(str1 == str2):
        print("true")
    else:
        print("false")


valid_palindrome("A man, a plan, a canal: Panama")