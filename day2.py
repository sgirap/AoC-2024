def is_safe(levels):
    """Check if a sequence is safe as is (increasing or decreasing)."""
    increasing = True
    decreasing = True
    for i in range(len(levels) - 1):
        diff = abs(levels[i] - levels[i + 1])
        if diff < 1 or diff > 3:
            return False  # Adjacent levels differ by less than 1 or more than 3
        if levels[i] >= levels[i + 1]:  # Not strictly increasing
            increasing = False
        if levels[i] <= levels[i + 1]:  # Not strictly decreasing
            decreasing = False
    return increasing or decreasing


def is_safe_with_dampener(levels):
    """Check if removing one level makes the sequence safe."""
    for i in range(len(levels)):
        # Create a new sequence excluding the current index
        new_levels = levels[:i] + levels[i + 1:]
        if is_safe(new_levels):
            return True
    return False


# Main logic
with open("day2input.txt", "r") as file:
    total = 0
    for line in file:
        levels = [int(x) for x in line.strip().split()]
        if is_safe(levels) or is_safe_with_dampener(levels):
            total += 1

    print(total)    