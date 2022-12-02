# What would your total score be if everything goes exactly according to your strategy guide?
with open('input.txt', 'r') as temp_file:
    plays = temp_file.read().splitlines()
    # example of input
    # ['A Z', 'C Z', ...]

def main():
    result = strategy(plays)
    print(result, 'part 1')
    result2 = new_strategy(plays)
    print(result2, 'part 2')

def strategy(lst):
    score = 0
    for part in lst:
        play = list(part)
        opponent = value(play[0])
        you = value(play[2])  #space is [1]
        # shape score
        score += you
        # play state score
        if opponent == you:
            # game state is draw
            score += 3
        # win for you, see cases above
        elif (opponent == 1 and you == 2) or \
                (opponent == 2 and you == 3) or \
                (opponent == 3 and you == 1):
            # you won
            score += 6
    return score

def value(play):
    """
    rock = 1             X, A - Rock defeats Scissors; if scissors -> rock
    paper = 2            B, Y - Paper defeats Rock; if rock -> paper
    scissors = 3         C, Z - Scissors defeats Paper; if paper -> scissors

    """
    if play == 'A' or play == 'X': #rock
        return 1
    elif play == 'B' or play == 'Y': #paper
        return 2
    elif play == 'C' or play == 'Z': #scissors
        return 3

def new_strategy(lst):
    score = 0
    for part in lst:
        play = list(part)
        opponent = value(play[0])
        you = play[2]
        # now game state is defined differently
        if you == 'X': #lose
            # only score of play
            if opponent == 1:
                score += 3
            elif opponent == 2:
                score += 1
            elif opponent == 3:
                score += 2
        elif you == 'Y': # draw
            you = opponent
            score += you + 3
        elif you == 'Z': #value of winning play
            if opponent == 1:
                score += 2 + 6
            elif opponent == 2:
                score += 3 + 6
            elif opponent == 3:
                score += 1 + 6
    return score

main()

# test example
example = ['A Y', 'B X', 'C Z']
assert(strategy(example) == 15)

example2 = ['A Y', 'B X', 'C Z']
assert(new_strategy(example2) == 12)