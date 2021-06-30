def age_assignment(*args, **kwargs):
    result = dict()
    for name in args:
        for letter in kwargs:
            if name.startswith(letter):
                result[name] = kwargs[letter]
    return result

print(age_assignment("Peter", "George", G=26, P=19))