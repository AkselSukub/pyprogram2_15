#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def remove_comments(source_file, destination_file):
    try:
        with open(source_file, 'r') as file:
            lines = file.readlines()
        
        with open(destination_file, 'w') as file:
            for line in lines:
                idx = line.find('#')
                if idx != -1:
                    file.write(line[:idx] + '\n')
                else:
                    file.write(line)

        with open(destination_file, 'r') as file:
            modified_content = file.read()
            print("Modified content of the file: ", modified_content)
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print("An error occurred:", e)

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")
    remove_comments(source_file, destination_file)

if __name__ == "__main__":
    main()