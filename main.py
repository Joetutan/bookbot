from stats import get_num_words, get_num_character, chars_dict_to_sorted_list
import sys


def main():
    # path_to_file = '/home/tutan/workspace/github.com/Joetutan/bookbot/books/frankenstein.txt'

    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_file>")
        sys.exit(1)

    path_to_file = sys.argv[1]

    book_text = get_book_text(path_to_file)
    num_words = get_num_words(book_text)
    char_dict = get_num_character(book_text)
    
    #get_num_character(book_text)
    sorted = chars_dict_to_sorted_list(char_dict)
   
    print("================== BOOKBOT =====================")  
    print(f"Analyzing book found at books/frankenstein.txt")
    print(f"-----------------Word Count--------------------")
    print(f"Found {num_words} total words")
    print(f"-----------------Character Count---------------")
    for item in sorted:
            print(f"{item['char']}: {item['num']}")
    print("================== END =========================")


def get_book_text(path_to_file):
    with open(path_to_file) as file:
        return file.read()


main()