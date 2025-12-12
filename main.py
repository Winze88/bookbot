from stats import get_book_text, word_count

def main():
    text = get_book_text("./books/frankenstein.txt")
    count = word_count(text)
    print(f"Found {count} total words")

main()