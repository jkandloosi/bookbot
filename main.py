def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordCount = word_count(text)
    letterCount = letter_count(text)
    #print(wordCount)
    #print(letterCount)
    
    chars_sorted_list = chars_dict_to_sorted_list(letterCount)
    print(chars_sorted_list)

    print(f"--- Begin report of {book_path} ---")
    print(f"{wordCount} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def word_count(book):
    words = book.split()
    return len(words)

def letter_count(book):
    letters = {}
    book = book.lower()
    words = book.split()

    for word in words:
        for letter in word:
            #print(letter)
            if (letter in letters):
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()