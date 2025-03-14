from stats import get_book_text, character_count, sort_chars
import os
import sys




def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("========BOOKBOT========")
        file_path = sys.argv[1]
        char_dict = character_count(file_path)
        sorted_chars = sort_chars(char_dict)
        print("Analyzing book")
        print("~~~~~~~~Word Count~~~~~~~~")
        print(f"Found {get_book_text(file_path)} total words")
        print("********Character Count********")
        for char_dict in sorted_chars:
            char = char_dict["char"]
            if char.isalpha():
                print(f"{char}: {char_dict['count']}")


main()