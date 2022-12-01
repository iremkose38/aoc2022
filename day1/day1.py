with open('elves_list.txt', 'r') as temp_file:
    calorie_list = temp_file.read().splitlines()

example = [1000, 2000, 3000, '', 4000, '', 5000, 6000, '', 7000, 8000, 9000, '', 10000]

def main():
    print("example: ")
    answer2 = find_max(example)
    print(answer2)

    print("\n")

    print("puzzle: ")
    answer = find_max(calorie_list)
    print(answer)

def top_three(lst):
    first = max(lst)
    sum3 = first
    print('first', first)
    lst.remove(first)

    second = max(lst)
    sum3 += second
    lst.remove(second)
    print('second', second)

    third = max(lst)
    sum3 += third
    print('third', third)

    return sum3

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
        elif calorie == lst[-1]:
            # last values wont be added bcs no space after
            # add last value to sum and add to list
            total += int(calorie)
            sum_list.append(total)
        else:
            total += int(calorie)
    sum_top3 = top_three(sum_list)
    return sum_top3

main()