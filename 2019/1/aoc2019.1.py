def part1():
    with open('input.txt', 'r') as f:
        print(sum(int(l)//3 - 2 for l in f))


def part2():
    with open('input.txt', 'r') as f:
        modules = [int(line) for line in f]

    total = 0
    for module in modules:
        newFuel = module//3-2
        while newFuel >= 0:
            total += newFuel 
            newFuel = newFuel // 3 - 2

    print(total)
part1()
part2()