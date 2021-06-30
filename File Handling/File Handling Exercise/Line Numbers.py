with open("text.txt") as file:
    for index, line in enumerate(file.readlines()):
        line = line.strip("\n")
        num_chars = sum([len(el) for el in line.split()])
        num_punctuation = sum([1 for word in line.split() for letter in word if letter in ",.-':;!?"])

        with open("result-02.txt", "a") as file:
            file.write(f"Line {index + 1}: {line} ({num_chars - num_punctuation})({num_punctuation})\n")







