from stats import get_book_text, word_count, char_count, sort_dict

def main():
    text = get_book_text("./books/frankenstein.txt")
    count = word_count(text)
    char_count_result = char_count(text)
    sorted_dict = sort_dict(char_count_result)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for n in sorted_dict:
        print(f"{n['char']}: {n['num']}")
    print("============= END ===============")

main()