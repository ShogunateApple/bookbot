#returns a file as a single string
def get_book_text(file_path):
    with open(file_path) as f:
        file_string = f.read()
        return file_string

#counts the number of words in the given string
def word_count(book):
    word_list = book.split()
    count = len(word_list)
    return count

#main
def main():
    book_string = get_book_text("books/frankenstein.txt")
    number_of_words = word_count(book_string)
    print(f"Found {number_of_words} total words")


main()
