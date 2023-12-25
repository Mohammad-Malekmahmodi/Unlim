def encode_number(n):
    n_str = str(n)
    result = ""

    count = 1
    for i in range(1, len(n_str)):
        if n_str[i] == n_str[i - 1]:
            count += 1
        else:
            result += str(count) + n_str[i - 1]
            count = 1

    result += str(count) + n_str[-1]

    return int(result)


def main():
    n = int(input())

    encoded_number = encode_number(n)

    if encoded_number % 2 == 1:
        print(encoded_number * 3)
    else:
        print(encoded_number + 3*10-10)


if __name__ == "__main__":
    main()
