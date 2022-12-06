with open('input.txt', 'r') as temp_file:
    crates = temp_file.read().splitlines()
    # example of input
    # ['            [Q]     [G]     [M]', '            [B] [S] [V]     [P] [R]',..]


def puzzle(lst):
    pass

def form_crates(lst):
    list_crates = [9*[]]
    for string in lst:
        print(string)

if __name__ == '__main__':
    solution = puzzle(crates)
    print(solution)
