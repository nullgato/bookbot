import sys
from stats import get_word_count
from stats import get_character_count
from stats import sort_char_dict_by_count

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def validate_args():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return False
    return True

def main():
    if (validate_args() == False):
        sys.exit(1)

    book_path = sys.argv[1]
    
    print("============ BOOKBOT ============")
    book_text = get_book_text(book_path)

    print("----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")
    
    char_count = get_character_count(book_text)

    print("--------- Character Count -------")
    sorted_chars = sort_char_dict_by_count(char_count)
    for char in sorted_chars:
        actual_char = char["char"]
        if actual_char.isalpha():
            print(f"{actual_char}: {char['num']}")

main()