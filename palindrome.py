def is_palindrome(s):
  # Reverse the string
  s_reversed = s[::-1]
  
  # Compare the reversed string with the original
  if s_reversed == s:
    return True
  else:
    return False

# Test the function
print(is_palindrome("racecar"))  
print(is_palindrome("hello"))
print(is_palindrome("madam"))  
