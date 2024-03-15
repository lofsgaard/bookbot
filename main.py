def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{sum(count_words(file_contents).values())} words found in the document\n")
    characters = count_chars(file_contents)
    char_sorted = sorted(characters.items(), key=lambda x: x[1], reverse=True)
    for char, count in char_sorted:
        print(f"The '{char}' character was found {count} times")
    print("--- End report  ---")

def count_words(text):
    word_counts = {}
    for word in text.split():
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def count_chars(text):
    char_counts = {}
    for char in text.lower():
        for c in char.split():
            if c.isalpha():
                if c in char_counts:
                    char_counts[char] += 1
                else:
                    char_counts[char] = 1
    return char_counts


main()
