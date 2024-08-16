def main():
    print("--- Begin report of books/frankenstein.txt ---")

    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_character(text)
    num_char_sort = converter_list(num_char)

    print(f"{num_words} words found in the document \n")    
    for c in num_char_sort:
        if c[0].isalpha():
            print(f"The {c[0]} character was found {c[1]} times")
        
    print("--- End report ---")
    
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(dic):
    return dic[1]

def converter_list(dic):
    return list(dic.items())

def get_num_character(text):
    words = text.split()
    counter = {}
    for word in words:
        word_lower = word.lower()
        for c in word_lower:
            if c in counter:
                counter[c] += 1
            else:
                counter.update({c : 1})
    return counter

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
