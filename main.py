def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    low_string = make_lower(text)
    characters = character_count(low_string)
    print(characters)
def get_book_text(path):    
    with open(path) as f:
        return f.read()

def get_num_words(text):     
    words = text.split()
    return len(words)

def make_lower(text):
    lowered_string = text.lower()
    return lowered_string

def character_count(low_string):
    character_dict = {}
    
    for letter in low_string:
        if letter in character_dict:
           character_dict[letter] +=1
        else:
            character_dict[letter] = 1

        
    return character_dict
    
        
main()
