def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    chars = {}
    char_list = []
    sorted_list = []

    lower_text = text.lower()

    for char in lower_text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    for k in chars:
        char_num = {}
        char_num["name"] = k
        char_num["num"] = chars[k]
        char_list.append(char_num)

    char_list.sort(reverse=True, key=sort_on)

    for count in char_list:
        if count["name"].isalpha():
            sorted_list.append(f"{count["name"]}: {count["num"]}")

    return sorted_list

def sort_on(items):
    return items["num"]