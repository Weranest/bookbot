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

def dict_to_list(dict):
    dict_list = []
    for key in dict:
        temp_dict = {"character":"", "number":0}
        temp_dict["character"] = key
        temp_dict["number"] = dict[key]
        print(temp_dict)
        dict_list.append(temp_dict)
    print(dict_list)
    return dict_list

def sort_crit(dict_list):
    return dict_list["number"]

def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    letters = letter_count(text)
    prepped_letters = dict_to_list(letters)
    print (f"Wordcount for the selected book: {word_count(text)} words")
    print(f"Letter distribution for selected book: {prepped_letters.sort(reverse=True, key=sort_crit)}")

main()

















