from stats import word_count, char_stat
import sys

args = sys.argv
if len(args)==1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path1 = args[1]

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()

    return file_contents

def main():
    content = get_book_text(path1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(content)} total words")
    print("--------- Character Count -------")
    char_cnt = char_stat(content)
    for x,y in char_cnt.items():
        print(f"{x}: {y}")


main()