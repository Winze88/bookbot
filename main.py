import sys
from stats import get_book_text, word_count, char_count, sort_dict

try:
    path = sys.argv[1]
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    text = get_book_text(path)
    count = word_count(text)
    char_count_result = char_count(text)
    sorted_dict = sort_dict(char_count_result)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for n in sorted_dict:
        print(f"{n['char']}: {n['num']}")
    print("============= END ===============")

main()