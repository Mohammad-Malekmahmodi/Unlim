def find_common_words(words):
    word_dict = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in word_dict:
            word_dict[sorted_word].append(word)
        else:
            word_dict[sorted_word] = [word]

    common_word_lists = [word_list for word_list in word_dict.values() if len(word_list) > 1]

    return common_word_lists


def main():

    input_words = input("").split()

    result = find_common_words(input_words)

    for word_list in result:
        print(' '.join(word_list))


if __name__ == "__main__":
    main()
