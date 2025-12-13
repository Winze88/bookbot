def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    counted_chars = {}
    text = text.lower()
    for char in text:
        if char not in counted_chars:
            counted_chars[char] = 1
        else:
            counted_chars[char] += 1
    return counted_chars

def sort_on(items):
    return items["num"]

def sort_dict(dictionary):
    new_dict = []
    for key in dictionary:
        if key.isalpha():
            new_dict.append({"char": key, "num": dictionary[key]})
    new_dict = sorted(new_dict, key=sort_on, reverse=True)
    return new_dict