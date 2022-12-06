with open('input.txt', 'r') as temp_file:
    datastream = temp_file.read().splitlines()
    # example of input
    # ['qzbzwwghwhwdhdqhhbhf...]


# How many characters need to be processed before the first start-of-packet marker is detected?

def puzzle(lst):
    # start of a packet is indicated by a sequence of four characters that are all different
    marker = []
    before_marker = ""
    for signal in lst:
        for letter in signal:
            if letter not in marker:
                marker.append(letter)
                # when marker of len 4 is found, return amount of characters before marker
                if len(marker) == 4:
                    # processed before + currently processed
                    processed = len(before_marker) + len(marker)
                    return processed
            else:
                # marker rule broken so search for new substring#
                marker.append(letter)
                # move rulebreakers to before marker so marker is clean to use again
                # TO DO check if equal letters are in marker;



if __name__ == '__main__':
    # solution = puzzle(datastream)
    # print("solution of the puzzle: ", solution)
    #TESTS
    example = ['bvwbjplbgvbhsrlpgdmjqwftvncz']
    assert(puzzle(example) == 5)

    example2 = ['nppdvjthqldpwncqszvftbrmjlhg']
    assert(puzzle(example2) == 6)

    example3 = ['nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg']
    assert(puzzle(example3) == 10)

    example4 = ['zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw']
    assert(puzzle(example4) == 11)