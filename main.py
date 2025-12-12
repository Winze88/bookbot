def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_text("./books/frankenstein.txt")
    count = word_count(text)
    print(f"Found {count} total words")
    #print(get_book_text("./books/frankenstein.txt"))

main()