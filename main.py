def main():
    path = "books/frankenstein.txt"
    book_contents = read_book(path)
    word_count = count_words(book_contents)
    letter_dict = count_characters(book_contents)
    letter_occurrences = list_from_dict(letter_dict)
    letter_occurrences.sort(reverse=True, key=sort_on)

    print_report(path, word_count, letter_occurrences)


def sort_on(dict):
    return dict["occurrences"]


def read_book(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_characters(text):
    chars = {}

    for c in text.lower():
        if not c.isalpha():
            continue

        if c not in chars:
            chars[c] = 1
            continue

        chars[c] += 1

    return chars


def list_from_dict(d):
    items = []

    for k, v in d.items():
        items.append({"char": k, "occurrences": v})

    return items


def print_report(path, word_count, letter_occurrences):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    for dic in letter_occurrences:
        print(f"The '{dic["char"]}' character was found {dic["occurrences"]} times")

    print("--- End report ---")


main()
