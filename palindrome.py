#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#Note: For the purpose of this problem, we define empty string as valid palindrome.

#Example 1:

#Input: "A man, a plan, a canal: Panama"
#Output: true
#Example 2:

#Input: "race a car"
#Output: false


import string

def isPalindrome(s):
        for i in s:
		if i in string.punctuation:
			s = s.replace(i,'')
        sub = s.replace(' ','').lower()
        return sub[::-1]==sub[:]


