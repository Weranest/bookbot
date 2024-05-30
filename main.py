def word_count(text):
   words = text.split()
   return len(words)


def letter_count(text):
    letters = {}
    lower_text = text.lower()
    for letter in lower_text:
        if letter in letters.keys():
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(word_count(file_contents))
    print(letter_count(file_contents))


main()

















