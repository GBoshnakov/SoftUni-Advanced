data = tuple(zip(input().split(", "), input().split(", ")))
# #print(data)
# mydict = {el[0]: el[1] for el in data}
# print(tuple(mydict))

# mydict = {country:  for country in input().split(", ") }
#
# print(mydict)

for el in data:
    print(f"{el[0]} -> {el[1]}")