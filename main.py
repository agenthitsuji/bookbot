from stats import split_book_text, count_characters, sort_dict
import sys

def get_book_text(file):
    with open(file) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_filepath = sys.argv[1]
    #franky = "books/frankenstein.txt"
    #print(get_book_text(franky))
    split_book_text(get_book_text(book_filepath))
    count_characters(get_book_text(book_filepath))
    sort_dict(count_characters(get_book_text(book_filepath)))
main()
