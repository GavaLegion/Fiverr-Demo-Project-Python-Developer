

def count_words(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    filename = "input.txt"
    word_count = count_words(filename)

    if word_count is None:
        print(f"File {filename} not found. Please create it and add some text.")
    else:
        print(f"Number of words in the file: {word_count}")
