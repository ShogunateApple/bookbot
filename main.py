#returns a file as a single string
def get_book_text(file_path):
    with open(file_path) as f:
        file_string = f.read()
        return file_string

#import word count function from stats
from stats import word_count

#import character count from stats
from stats import character_count

#import the sort dictionary function from stats
from stats import sort_dictionary

#set the path of the book to check
path_to_book = "books/frankenstein.txt"

#main
def main():
    book_string = get_book_text(path_to_book)
    number_of_words = word_count(book_string)
    #print(f"Found {number_of_words} total words")

    total_characters = character_count(book_string)
    #print(total_characters)

    sorted_characters = sort_dictionary(total_characters)
    #print(sorted_characters)

    #print the report nice and neat
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for character in sorted_characters:
        #check if its an alphanumeric character
        if((character["char"]).isalpha() == True):
            #print(sorted_characters)
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main()
