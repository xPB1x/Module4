def check_for_palindrome(string):
    if string == string[::-1]:  #идет проверка с помощью среза, является ли перевернутая строка равной заданной
        return True
    else:
        return False


print(check_for_palindrome('20222202'))
print(check_for_palindrome('HelloWorld'))
