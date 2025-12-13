from stats import get_book_text, word_count, char_count

def main():
    text = get_book_text("./books/frankenstein.txt")
    count = word_count(text)
    char_count_result = char_count(text)
    print(f"Found {count} total words")
    print(char_count_result)

main()