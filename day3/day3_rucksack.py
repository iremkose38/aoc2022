with open('input.txt', 'r') as temp_file:
    lst_rucksacks = temp_file.read().splitlines()
    # example of input
    # ['FzQrhQpJtJMFzlpplrTWjTnTTrjVsVvvTnTs', 'mScqSqqgcfPCqGPZcfGNSvTNsVVNSjNvWSNsNz', ...]

def main():
    answer = puzzle(lst_rucksacks)
    print('puzzle answer: ', answer)

def puzzle(lst):
    # difference between lower and uppercase !
    sum_priorities = 0
    for rucksack in lst_rucksacks:
        # find index of split: if not even length, take rounded value
        split = round(len(rucksack) // 2)
        compartment1 = rucksack[:split]
        compartment2 = rucksack[split+1:]
        # equal item(s):
        items = find_item(compartment1, compartment2)
        if items is not None:
            # priority value
            for item in items:
                value = calculate_priority(item)
                sum_priorities += value
    return sum_priorities

def find_item(comp1, comp2):
    # find item that's in both compartments
    equal_items = []
    for item in comp1:
        for item2 in comp2:
            if item == item2:
                # equal item is found
                equal_items.append(item)
            else:
                # no equal items?
                return None
    return equal_items

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
rucksacks_example = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg'
                                                                                     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
assert(puzzle(rucksacks_example) == 157)
