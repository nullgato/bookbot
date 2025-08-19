def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_character_count(book_text):
    char_count = {}
    for char in book_text:
        to_lower = char.lower()
        if to_lower not in char_count:
            char_count[to_lower] = 0
        char_count[to_lower] += 1
    return char_count

def sort_char_dict_by_count(char_counts):
    def sort_on(items):
        return items["num"]
    
    chars_dict_list = []
    
    for char in char_counts:
        chars_dict_list.append({ "char": char, "num": char_counts[char] })

    
    chars_dict_list.sort(reverse=True, key=sort_on)
    return chars_dict_list