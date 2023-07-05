def check_for_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


print(check_for_palindrome('20222202'))
print(check_for_palindrome('HelloWorld'))
