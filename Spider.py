def spiderman_journey(n, buildings):
    if buildings[0] == 0:
        return "Spiderman Wasted"

    max_reachable = 0
    current_building = 0
    jumps = 0

    while current_building < n - 1:
        jumps += 1
        farthest_reachable = 0

        for i in range(1, buildings[current_building] + 1):
            if current_building + i < n and buildings[current_building + i] > farthest_reachable:
                farthest_reachable = buildings[current_building + i]

        if farthest_reachable == 0:
            return "Spiderman Wasted"

        current_building += farthest_reachable

    return jumps


# خواندن تعداد ساختمان‌ها
n = int(input().strip())

# خواندن تعداد طبقات هر ساختمان
buildings = list(map(int, input().strip().split()))

result = spiderman_journey(n, buildings)
print(result)
