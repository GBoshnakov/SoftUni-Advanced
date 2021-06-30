def palindrome(string, index):
    end_index = len(string) - index - 1
    if len(string[index:end_index]) < 2:
        return f"{string} is a palindrome"
    if string[index] == string[end_index]:
        return palindrome(string, index + 1)
    else:
        return f"{string} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))