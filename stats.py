def get_num_words(book_text):
    words = book_text.split()
    return len(words)

def get_num_character(book_text):
    lower_case = book_text.lower()
    char_count = {}
    for char in lower_case:
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(char_count):
    sorted_list = []
    for ch in char_count:
        sorted_list.append({"char": ch, "num": char_count[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


