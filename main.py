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
        dict_list.append(temp_dict)
    return dict_list

def sort_crit(dict_list):
    return dict_list["number"]

def main():
    print("Starting analysis...")
    file_path = "books/frankenstein.txt"
    print(f"Getting data from {file_path}")
    text = get_text(file_path)
    letters = letter_count(text)
    print(f"There are {word_count(text)} words in the document")
    prepped_letters = dict_to_list(letters)
    prepped_letters.sort(reverse=True, key=sort_crit)
    for item in prepped_letters:
        if item["character"].isalpha():
            print(f"The '{item["character"]}' character was found {item["number"]} times")
main()

















