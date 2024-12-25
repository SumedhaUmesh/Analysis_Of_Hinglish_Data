import string

def slang(text):
    file = open("spelling.txt", "r")
    slangs = file.readlines()

    input_lines = text
    input_lines_withoutpunc = []
    slang_word = []
    meaning = []

    # store the slang slangs and meanings in different lists
    for line in slangs:
        temp = line.split()
        slang_word.append(temp[0])
        meaning.append(line[line.find(' ') + 1:-1])

    # replace the slang word with meaning
    for line in range(len(input_lines)):
        for i, word in enumerate(input_lines[line].split()):
            if word in slang_word:
                idx = slang_word.index(word)
                input_lines[line] = input_lines[line].replace(word, meaning[idx])

    for word in input_lines:
        input_lines_withoutpunc.append(word.translate(word.maketrans('', '', string.punctuation)))

    for line in range(len(input_lines_withoutpunc)):
        for i, word in enumerate(input_lines_withoutpunc[line].split()):
            if word in slang_word:
                idx = slang_word.index(word)
                input_lines_withoutpunc[line] = input_lines_withoutpunc[line].replace(word, meaning[idx])

    corrected_sentence = "\n".join(input_lines_withoutpunc)
    return corrected_sentence
