def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    low_string = make_lower(text)
    characters = character_count(low_string)
    chars_sorted_list = chars_dict_to_sorted_list(characters)
    
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in document")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("---End of Report---")
    

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

def report_gen(characters):
    for idx in characters:
        
        letter= characters.split()
        print(letter)

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char":ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    

    
    



    
        
main()
