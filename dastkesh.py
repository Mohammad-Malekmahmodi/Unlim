def worst_case(r, b, y, g):
    """
    This function calculates the worst case scenario.

    Args:
        r: number of red gloves
        b: number of blue gloves
        y: number of yellow gloves
        g: number of green gloves

    Returns:
        number of gloves that need to be picked to have at least one pair of each color
    """

    max_count = max(r, b, y, g)

    if max_count % 2 == 0:
        return max_count

    return max_count + 2


def main():
    """
    This function is the main function of the program.
    """

    # Get the number of gloves of each color from the user.
    r = int(input(""))
    b = int(input(""))
    y = int(input(""))
    g = int(input(""))

    # Calculate the worst case scenario.
    worst_case = worst_case(r, b, y, g)

    # Print the output.
    print(f"سارا در بد شانس ترین حالت خود باید {worst_case} دستکش از سطل بردارد تا از همه رنگ ها حداقل یک جفت داشته باشد.")


if __name__ == "__main__":
    main()
