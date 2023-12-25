# def george_food(n):
#     menu = ["fries potato", "burger", "pizza" ,"hotdog"]
#     george_eaten = []
#
#     for i in range(n):
#         george_eaten.append(menu[(i % 3) + 1])
#
#     return george_eaten
#
#
# if __name__ == "__main__":
#     n = int(input())
#
#     result = george_food(n)
#
#     for food in result:
#         print(food)
def george_food(n):
    menu = ["pizza", "burger", "fries potato", "hotdog"]
    george_eaten = []

    for i in range(n):
        george_eaten.append(menu[(i % 4)])
        if (i + 1) % 3 == 0:  # هر بار بعد از سه دور، غذایی که جورج می‌خورد را چاپ کنید
            print(f"George ate: {george_eaten[-1]}")

    return george_eaten


if __name__ == "__main__":
    n = int(input("Enter the number of rounds: "))

    result = george_food(n)

    print("\nFinal result:")
    for food in result:
        print(food)
