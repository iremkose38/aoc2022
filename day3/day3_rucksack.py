with open('input.txt', 'r') as temp_file:
    lst_rucksacks = temp_file.read().splitlines()
    # example of input
    # ['FzQrhQpJtJMFzlpplrTWjTnTTrjVsVvvTnTs', 'mScqSqqgcfPCqGPZcfGNSvTNsVVNSjNvWSNsNz', ...]


def main():
    # part one
    answer = puzzle(lst_rucksacks)
    print("answer of puzzle:", answer)
    # part two
    answer = puzzle2(lst_rucksacks)
    print("answer of second puzzle:", answer)


def puzzle2(lst):
    # handle rucksacks per 3, create sublist
    sublists = split(lst)
    sum_equals = 0
    for team in sublists:
        equal = comparison3(team)
        # get priority if equal element
        value = calculate(equal)
        sum_equals += value
    return sum_equals


def comparison3(lst):
    # convert lists to sets
    person1 = set(lst[0])
    person2 = set(lst[1])
    person3 = set(lst[2])
    # find intersection of three sets
    value = person1.intersection(person2)
    value2 = value.intersection(person3)
    # convert back to list
    for item in value2:
        return item


def split(lst):
    # amount of sublists?
    sublists = []
    amount = len(lst)//3
    i = 0  # first sublists are [0:3], [3:6]
    j = 3
    while amount > 0:
        new_list = lst[i: j]
        i += 3
        j += 3
        sublists.append(new_list)
        amount -= 1
    return sublists


def puzzle(lst):
    sum_priorities = 0
    # handle per rucksack in list
    for rucksack in lst:
        # find split index
        split = len(rucksack) // 2
        # find first and second compartment by slicing
        compartment1 = rucksack[0:split]
        compartment2 = rucksack[split:]
        # compare the two to find equal element
        element = comparison2(compartment1, compartment2)
        # element could be None, so different cases
        if element is not None:
            # calculate priority of equal element
            priority = calculate(element)
            sum_priorities += priority
        # else, do nothing bcs no priority to add
    return sum_priorities


def comparison2(compartment1, compartment2):
    for element in compartment1:
        for other in compartment2:
            if element == other:
                # found equal one
                return element
    # if out of loop without returning equal element, there is no equal
    return None


def calculate(letter):
    # Lowercase item types a through z have priorities 1 through 26 -> filler 0
    # Uppercase item types A through Z have priorities 27 through 52.
    # find priority by index in following alphabet list:
    alphabet = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return alphabet.index(letter)

main()
# TESTs
rucksacks_example = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg',
                     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
assert(puzzle(rucksacks_example) == 157)

group = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg',
          'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', ' CrZsJsPPZsGzwwsLwLmpwMDw']
assert(puzzle2(group) == 70)
