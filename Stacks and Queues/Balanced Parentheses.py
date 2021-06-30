text = input()

opening_parethesses = []

is_balanced = True

for el in text:
    if el in "{[(":
        opening_parethesses.append(el)
    elif el in "}])" and opening_parethesses:
        parenthesis = opening_parethesses.pop()

        if f"{parenthesis}{el}" in ["{}", "[]", "()"]:
            continue
        # if  opening_parethesses[-1] == "{" and text[i] == "}":
        #     opening_parethesses.pop()
        # elif opening_parethesses[-1] == "[" and text[i] == "]":
        #     opening_parethesses.pop()
        # elif opening_parethesses[-1] == "(" and text[i] == ")":
        #     opening_parethesses.pop()
        else:
            is_balanced = False
            break
    else:
        is_balanced = False
        break
if is_balanced and not opening_parethesses:
    print("YES")
else:
    print("NO")