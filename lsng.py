def can_build_target(data, target_word, target_number):
    letters = set()
    numbers = set()

    for char in data:
        if char.isalpha():
            letters.add(char)
        elif char.isdigit():
            numbers.add(char)

    can_build_word = all(letter in letters for letter in target_word)
    can_build_number = all(number in numbers for number in target_number)

    return can_build_word, can_build_number


def main():
    data = input().strip()
    target_word, target_number = input().strip().split()

    result_word, result_number = can_build_target(data, target_word, target_number)

    print(result_word)
    print(result_number)


if __name__ == "__main__":
    main()
