with open('input.txt', 'r') as temp_file:
    lst_rucksacks = temp_file.read().splitlines()
    # example of input
    # ['FzQrhQpJtJMFzlpplrTWjTnTTrjVsVvvTnTs', 'mScqSqqgcfPCqGPZcfGNSvTNsVVNSjNvWSNsNz', ...]

def main():
    answer = puzzle(lst_rucksacks)
    print('puzzle answer: ', answer)

def puzzle(lst):
    sum_priorities = 0
    for rucksack in lst:
        # find index of split: always even because compartments have even amount of items.
        split = len(rucksack) // 2
        compartment1 = rucksack[:split-1]
        compartment2 = rucksack[split:]

        equal_item = find_item(compartment1, compartment2)
        if equal_item is not None:
            value = calculate_priority(equal_item)
            sum_priorities += value
    return sum_priorities

def find_item(comp1, comp2):
    list1 = list(comp1)
    list2 = list(comp2)
    # The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.
    for item in list1:
        for item2 in list2:
            if item == item2:
                return item
    # example: 'RQFLStFvdcBbzdJbJM' has no equal in compartments
    return None

def calculate_priority(item):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    # find priority by index in following alphabet list:
    alphabet = [0]
    for j in range(97, 123): # lower case
        alphabet.append(chr(j))
    for i in range(65, 91): # upper case
        alphabet.append(chr(i))
    # take value out of list index
    value = alphabet.index(item)
    return value

main()
# test
rucksacks_example = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg', 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
assert(puzzle(rucksacks_example) == 157)
