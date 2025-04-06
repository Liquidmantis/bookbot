import sys
from stats import *

def get_book_text(file_path):
    with open(file_path, "r") as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    text = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")

    word_count = get_num_words(text)
    print(f"Found {word_count} total words")

    chars = get_num_chars(text)
    sorted_chars = sort_counts(chars)
    print("--------- Character Count -------")

    for item in sorted_chars:
        if item['char'].isalpha():
            print(f"{item['char']}: {item['count']}")

main()
