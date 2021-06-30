vowels = ['a', 'o', 'u', 'e', 'i']

print("".join([el for el in input() if el.lower() not in vowels]))