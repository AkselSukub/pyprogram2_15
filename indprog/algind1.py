#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def extract_vowel_starting_words(text):
    vowels = 'aeiouAEIOU'
    words = text.split()
    vowel_words = [word for word in words if word and word[0] in vowels]
    return vowel_words

def main():
    file_path = 'C:/otkat/progr5/english_text.txt'
    english_text = read_text_from_file(file_path)
    vowel_starting_words = extract_vowel_starting_words(english_text)

    for word in vowel_starting_words:
        print(word)

if __name__ == "__main__":
    main()