import os
import sys



def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
        words = file_contents.split()

        return len(words)


def character_count(file_path):

    unique = {}

    with open(file_path, "r", encoding="utf-8") as f:

        file_contents = f.read()

        for char in file_contents:
            char = char.lower()
            if char not in unique:
                unique[char] = 1
            else:
                unique[char] +=1

    return(unique)
    print(f"results:{unique}")


def sort_chars(char_dict):
    polished = []
    for char, count in char_dict.items():
        polished.append({"char": char, "count":count})

    polished.sort(reverse=True, key=lambda x: x["count"])
    return polished
    print(polished)




