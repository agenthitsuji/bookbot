from stats import split_book_text, count_characters, sort_dict
import sys

def get_book_text(file):
    with open(file) as f:
        return f.read()


def main():
    franky = "books/frankenstein.txt"
    #print(get_book_text(franky))
    split_book_text(get_book_text(franky))
    count_characters(get_book_text(franky))
    sort_dict(count_characters(get_book_text(franky)))
main()
