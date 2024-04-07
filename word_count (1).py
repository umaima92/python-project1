
def count_words(text):
    words = text.split()
    return len(words)

def count_sentences(text):
    sentences = text.split('.')
    return len(sentences)

def main():
    text = input("Enter a text: ")

    num_words = count_words(text)
    num_sentences = count_sentences(text)

    print("Number of words:", num_words)
    print("Number of sentences:", num_sentences)

if __name__ == "__main__":
    main()
