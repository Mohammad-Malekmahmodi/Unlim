def malakh_jump(n, m):
    current_height = 0
    jump_height = m
    jumps = 0

    while current_height < n:
        current_height += jump_height
        jump_height += 0.2  # هر بار افزایش ارتفاع پرش
        jumps += 1

    if current_height >= n:
        return jumps
    else:
        return -1  # ملخ نمی‌تواند از چاه خارج شود


if __name__ == "__main__":
    n, m = map(int, input().split())

    result = malakh_jump(n, m)

    if result != -1:
        print(f"Azadi ba {result} paresh")
    else:
        print("Malakh failed")
