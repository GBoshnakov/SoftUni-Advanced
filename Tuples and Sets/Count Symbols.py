text = input()
text_as_tuple = tuple(text)


chars = set()

for el in text:
    chars.add(el)

sorted_chars = sorted(chars)

for el in sorted_chars:
    print(f"{el}: {text.count(el)} time/s")

