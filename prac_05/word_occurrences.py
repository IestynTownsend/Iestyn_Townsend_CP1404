def count_word_occurrences(text):
    # Initialize a dictionary to store word counts
    word_count = {}

    # Split the input text into words and count occurrences
    words = text.lower().split()
    for word in words:
        # Remove punctuation and special characters
        word = word.strip('.,!?()[]{}":;')
        word_count[word] = word_count.get(word, 0) + 1

    # Find the maximum word length for formatting
    max_word_length = max(len(word) for word in word_count)

    # Sort the dictionary by word and print the counts with alignment
    for word, count in sorted(word_count.items()):
        print(f"{word:{max_word_length}} : {count}")


def main():
    user_input = input("Enter a string: ")
    count_word_occurrences(user_input)


main()
