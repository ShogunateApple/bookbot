#returns a file as a single string
def get_book_text(file_path):
    with open(file_path) as f:
        file_string = f.read()
        return file_string

#main
def main():
    book_string = get_book_text("books/frankenstein.txt")
    print(book_string)


main()
