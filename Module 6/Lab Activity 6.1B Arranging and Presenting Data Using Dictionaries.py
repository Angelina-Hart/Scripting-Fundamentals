def word_counter(word):
    dictionary = {}
    for char in word:
        if char == " ":
            continue
        else:
            letter_count = word.count(char)
            dictionary[char] = letter_count
    return dictionary


print(word_counter("Mississippi"))
