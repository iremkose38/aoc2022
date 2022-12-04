with open('input.txt', 'r') as temp_file:
    assigments = temp_file.read().splitlines()
    # example of input
    # ['75-76,18-75', '2-54,1-50', '82-83,78-82', ...]


def puzzle(lst):
    # check per duo if one contains another, increase pairs
    pairs = 0
    for section in lst:
        # 75-76,18-75
        divided = section.split(',')
        if contains(divided):
            # if they contain one another: a containing pair is found
            pairs += 1
    return pairs


def contains(elves):
    # ['75-76', '18-75']
    # add numbers in range
    all_ranges = []
    for elf in elves:
        ranges = set()
        section_id = elf.split('-')
        # fill in missing numbers between start n end point
        start = int(section_id[0])
        end = int(section_id[1])
        # added bcs of range? ranges.append(start)
        for number in range(start, end+1):
            ranges.add(number)
        all_ranges.append(ranges)

    # check if one FULLY contains another
    if not all_ranges[0].intersection(all_ranges[1]):
        # if set is empty no overlap
        return False
    else:
        return True


if __name__ == '__main__':
    solution = puzzle(assigments)
    print('the answer is: ', solution)
    # test = ['2-4,6-8', '2-3,4-5', '5-7,7-9', '2-8,3-7', '6-6,4-6', '2-6,4-8']
    # assert (puzzle(test) == 2)
