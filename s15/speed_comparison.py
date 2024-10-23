def load_words_into_list():
    """
    Read all the english words from words.txt into a list and return the list
    """

    words = []
    
    with open("data/words.txt") as file:
        for line in file:
            word = line.strip()
            words.append(word)
    return words

def main():
    words_list = load_words_into_list()
    words_dict = load_words_into_dict()
    print(words_list[-1], len(words_list))

main()