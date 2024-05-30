def get_text(file_path):
    with open(file_path) as f:
        return f.read()

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
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    print (f"Wordcount for the selected book: {word_count(text)} words")
    print(f"Letter distribution for selected book: {letter_count(text)}")

main()

















