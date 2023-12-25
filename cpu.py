def commands(command):
    """
    این تابع دستورات CPU را پیاده‌سازی می‌کند.

    Args:
      command: دستور CPU

    Returns:
      تابعی که دستور را اجرا می‌کند.
    """

    if command == "SET":
        return lambda var, num: num
    elif command == "ADD":
        return lambda var, num: var + num
    elif command == "SUB":
        return lambda var, num: var - num
    elif command == "MUL":
        return lambda var, num: var * num
    elif command == "GTL":
        return lambda var, num: num
    elif command == "GBL":
        return lambda var, num: var - num
    elif command == "GUL":
        return lambda var, num: var + num
    elif command == "CTA":
        return lambda var, num: num + num
    elif command == "CTS":
        return lambda var, num: num - num
    elif command == "SKP":
        return lambda var, num: num == 0
    elif command == "PRT":
        return lambda var, num: print(chr(var))
    else:
        raise ValueError(f"نامعتبر: {command}")


def simulate(lines):
    """
    این تابع برنامه را شبیه‌سازی می‌کند.

    Args:
      lines: ورودی برنامه

    Returns:
      مقدار رجیستر var در انتهای برنامه
    """

    var = 0
    num = 0
    for line in lines:
        command = line[:3]
        if command != "PRT":
            num = commands(command)(var, int(line[3:]))
        else:
            commands(command)(var, num)
            return  # چون PRT مقدار var را چاپ می‌کند و مقدار نهایی را می‌دانیم

    return var


if __name__ == "__main__":
    n = int(input(""))
    lines = []
    for i in range(n):
        line = input(i + 1)
        lines.append(line)


    result = simulate(lines)
    print(result)
