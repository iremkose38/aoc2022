with open('input.txt', 'r') as temp_file:
    datastream = temp_file.read().splitlines()
    # example of input
    # ['qzbzwwghwhwdhdqhhbhf...]


# How many characters need to be processed before the first start-of-packet marker is detected?

def puzzle(lst):
    # start of a packet = substring of length 4 without repeating char
    marker = []     # substring
    for signal in lst:
        processed = 0  # count letters that have been processed until marker is found
        for letter in signal:
            # add letter either way to marker, then check if marker is valid
            marker.append(letter)
            processed += 1
            if len(marker) == 4:
            # if len correct check for duplicates
                if check(marker):
                    # if marker is valid, no more checking other char
                    return processed
                else:
                    # new marker starting point needed
                    marker = new_marker(marker)


def check(mrk):
    # check if given marker is valid
    doubles = [letter for letter in mrk if mrk.count(letter) > 1]
    if len(doubles) == 0:
        return True
    # if above is not correct, False
    return False

def new_marker(mrk):
    # return new marker that is valid to start again for a search
    # nppdvjthqldpwncqszvftbrmjlhg
    new = mrk
    # delete letters that make mrk not valid = doubles?
    while not check(new):
        new.pop(0)
    return new


if __name__ == '__main__':
    solution = puzzle(datastream)
    print("solution of the puzzle: ", solution)

    #TESTS
    #OK
    example = ['bvwbjplbgvbhsrlpgdmjqwftvncz']
    # assert(puzzle(example) == 5)

    example2 = ['nppdvjthqldpwncqszvftbrmjlhg']
    assert(puzzle(example2) == 6)

    example3 = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']
    assert(puzzle(example3) == 10)

    example4 = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
    assert(puzzle(example4) == 11)