#counts the number of words in the given string
def word_count(book):
    word_list = book.split()
    count = len(word_list)
    return count

#------------------------------------------------------------------------------------------------------------
#counts the amount each characters appears
def character_count(book):
    #create an empty dictionary
    characters = {}

    #print (f"The number of characters in Frankenstein is {len(book)}")
    book = book.lower()

    #iterate through the entire book
    for i in range(0, len(book)):
        
        #check if character is in the dictionary
        if ((book[i] in characters) == True):
            characters[book[i]] += 1    
        else:
            characters[book[i]] = 1  
    return characters

#-----------------------------------------------------------------------------------------------------------
#Takes the dictionary of characters and counts, returns a sorted list of dictionaries
def sort_dictionary(character_dictionary):
    #helper function to return the "num" for sorting
    def sort_on(dictionary):
        return dictionary["num"]

    #create the empty list
    dictionary_list = []

    #create the list of dictionaries
    for character in character_dictionary:
        dictionary_list.append({"char": character, "num": character_dictionary[character]})
    
    #sort the dictionary using the num
    dictionary_list.sort(reverse=True, key=sort_on)

    return dictionary_list

    
#-----------------------------------------------------------------------------------------------------------








        

