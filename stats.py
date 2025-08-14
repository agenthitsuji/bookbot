def split_book_text(book):
    print("--------- Word Count -------")
    print(f"Found {len(book.split())} total words")

def count_characters(book):
    lower_list = []
    characters = {}
    for word in book:
        for letter in word.lower():
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
    print(characters)
    return characters
    
def sort_dict(dictionary):
    sorted_chars = []
    for char in dictionary:
        sorted_chars.append({"char" : char, "num" : dictionary[char]})
    sorted_chars.sort(reverse=True, key=sort_on)
    dict_report(sorted_chars)
    return sorted_chars


def dict_report(dictionary):
    print("--------- Character Count -------")
    for entry in dictionary:
        print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


def sort_on(items):
    return items["num"]