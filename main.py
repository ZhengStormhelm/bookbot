import sys
from stats import get_book_text, word_count, char_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = sys.argv[1]
    content = get_book_text(text)
    num_words = word_count(content)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for v in char_count(content):
        print(v)
    print("============= END ===============")
    
main()