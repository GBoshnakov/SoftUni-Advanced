text = [" ".join(el.split()) for el in input().split("|")][::-1]
print(*[el for el in text if el])
#print(text)

#print(*[el for sub_el in text for el in sub_el if el.isdigit()])