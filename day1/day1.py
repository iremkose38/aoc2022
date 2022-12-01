with open('elves_list.txt', 'r') as temp_file:
    calorie_list = temp_file.read().splitlines()

example = [1000, 2000, 3000, '', 4000, '', 5000, 6000, '', 7000, 8000, 9000, '', 10000]

def main():
    answer2 = find_max(example)
    print(answer2, "example2")

    answer = find_max(calorie_list)
    print(answer, 'puzzle')


# problem with reading the file somehow reads newlines so:
# def no_newlines(lst):


def find_max(lst):
    # returns max sum of all sums
    sum_list = []
    # initialise current total to zero first
    total = 0
    # loop over calorie_list; a calorie is one item in an 'individual' list
    for calorie in lst:
        # if space = next list
        if calorie == '':
            # add total calories of current elf to list
            sum_list.append(total)
            # reset total for next elf
            total = 0
        else:
            total += int(calorie)
    return max(sum_list)

main()