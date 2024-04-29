def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordCount = word_count(text)
    letterCount = letter_count(text)
    #print(wordCount)
    #print(letterCount)
    
    charsSortedList = chars_dict_to_sorted_list(letterCount)
    print(charsSortedList)

    print(f"--- Begin report of {book_path} ---")
    print(f"{wordCount} words found in the document")
    print()

    for item in charsSortedList:
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

def chars_dict_to_sorted_list(dict):
    sortedList = []
    for ch in dict:
        sortedList.append({"char": ch, "num": dict[ch]})
    sortedList.sort(reverse=True, key=sort_on)
    return sortedList

main()