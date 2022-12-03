with open('input.txt', 'r') as temp_file:
    lst_rucksacks = temp_file.read().splitlines()
    # example of input
    # ['FzQrhQpJtJMFzlpplrTWjTnTTrjVsVvvTnTs', 'mScqSqqgcfPCqGPZcfGNSvTNsVVNSjNvWSNsNz', ...]

def main():
    answer = puzzle(lst_rucksacks)
    print("answer of puzzle:", answer)

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
        element = comparison(compartment1, compartment2)
        # element could be None, so different cases
        if element is not None:
            # calculate priority of equal element
            priority = calculate(element)
            sum_priorities += priority
        # else, do nothing bcs no priority to add
    return sum_priorities

def comparison(compartment1, compartment2):
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
# TEST
rucksacks_example = ['vJrwpWtwJgWrhcsFMMfFFhFp', 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL', 'PmmdzqPrVvPwwTWBwg',
                     'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn', 'ttgJtRGJQctTZtZT', 'CrZsJsPPZsGzwwsLwLmpwMDw']
assert(puzzle(rucksacks_example) == 157)
