# What would your total score be if everything goes exactly according to your strategy guide?
with open('input.txt', 'r') as temp_file:
    plays = temp_file.read().splitlines()
    # example of input
    # ['A Z', 'C Z', ...]

def main():
    result = strategy(plays)
    print(result)

def strategy(lst):
    score = 0
    for part in lst:
        play = list(part)
        opponent = value(play[0])
        you = value(play[2])  #space is [1]
        # shape
        score += you
        # draw with same plays
        if opponent == you:
            # game state is draw
            score += 3
        # win for you, see cases above
        elif (opponent == 1 and you == 2) or \
                (opponent == 2 and you == 3) or \
                (opponent == 3 and you == 1):
            # you won
            score += 6

def value(play):
    """
    paper = 2           "X" Paper defeats Rock; if rock -> paper
    scissors = 3        "Y" Scissors defeats Paper; if paper -> scissors
    rock = 1            "Z" Rock defeats Scissors; if scissors -> rock
    """
    if play == 'A' or play == 'Z': #rock
        return 1
    elif play == 'B' or play == 'X': #paper
        return 2
    elif play == 'C' or play == 'Y': #scissors
        return 3
main()
# tests maybe