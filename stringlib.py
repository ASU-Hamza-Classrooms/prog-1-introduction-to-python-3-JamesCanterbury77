#!/bin/python3

#Add the following functions:
#
#reverseStr - takes as input a string and returns the reverse of it
#
def reverseStr(str):
    return str[::-1]
#containsWord - takes as input two strings, containingStr and containedStr,
#and returns "Yes" if containedStr is anywhere within containingStr 
#and returns "No" otherwise
#
def containsWord(containingStr, containedStr):
    if containingStr.find(containedStr) != -1:
        return "Yes"
    else: 
        return "No"
#isPalindrome - takes as input a string and returns "Yes" if it is
#palindrome and "No" otherwise  
#
def isPalindrome(str):
    if str == str[::-1]:
        return "Yes"
    else: 
        return "No"
#upperCaseStr - takes as input a string and returns the identical string
#with the characters 'a' ... 'z' changed to uppercase
#
def upperCaseStr(str):
    return str.upper()

