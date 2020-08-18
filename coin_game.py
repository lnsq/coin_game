## Author: Ellen Qian
## NetID: esq2
## Recursion sample code for CPSC 223
## Context: Problem statement taken from
##          Cornell's CS2110 Fall 2014 course, problem 8
## https://www.cs.cornell.edu/courses/cs2110/2014fa/L07-Recursion/recursion_practice.pdf
## Problem statement (for convenience):
##       Coin game: Alice and Bob are playing a game
##       using a bunch of coins. The players pick several coins out of the
##       bunch in turn. Each time a player is allowed to pick 1, 2 or 4 coins,
##       and the player that gets the last coin is the winner. Assume that
##       both players are very smart and he/she will try his/her best to
##       work out a strategy to win the game. For example, if there are 2
##       coins and Alice is the first player to pick, she will definitely pick 2
##       coins and win. If there are 3 coins and Alice is still the first player
##       to pick, no matter she picks 1 or 2 coins, Bob will get the last coin
##       and win the game. Given the number of coins and the order of
##       players (which means the first and the second players to pick the
##       coins), you are required to write a program to calculate the winner
##       of the game, and calculate how many different strategies there are
##       for he/she to win the game. You should use recursion to solve
##       the problem, and the parameters are read from the command line.
##       You can assume that there are no more than 30 coins.
## Sample output:
##        ./pickcoin 1 alice bob
##        alice 1
##        ./pickcoin 2 bob alice
##        bob 1
##        ./pickcoin 3 alice bob
##        bob 2
##        ./pickcoin 10 alice bob
##        alice 22
##        ./pickcoin 25 alice bob
##        alice 3344
##        ./pickcoin 30 alice bob
##        bob 18272
## Steps:
##      1. Input the number of coins you would like the game to have
##      2. Input two names in the order in which they will play
## Output: The name of the winner followed by the number of different
##         strategies the winner could have used to win
## Notes: Deceptively tough to figure out what the problem statement considered a
##        "winning strategy" but very satisfying to finally figure out! Took a lot
##        of drawing trees.

import argparse

strats = 0

def play(n, first, second):
    global strats
    if n > 0:
        ## Assume that the winner is the first person that plays,
        ## alternating with each recursive call.
        winner = first

        ## Covering the base cases
        if n == 1 or n == 2:
            strats += 1
            return winner
        ## If the first player has 4 coins in the pile, they can pick all 4 and win,
        ## or they can pick 1 and still win. 
        elif n == 4:
            strats += 1
            play(n - 1, second, first)
            return winner
        ## If there are 3 coins in the pile, the first person (aka the person whose
        ## turn it is -- I use these terms interchangeably) will never win. 
        elif n == 3:
            winner = second
            play(n - 1, second, first)
            play(n - 2, second, first)
            return winner
        else:
            ## The strategy: the first player will try to play as 'optimally' as possible
            ## i.e. They will try to enforce a condition where the next player
            ## has to play on a multiple of 3.

            ## If the first player is playing on a multiple of 3, then it doesn't matter
            ## what they play -- they will always lose because they cannot force the above condition.
            if n % 3 == 0:
                winner = second
                play(n - 1, second, first)
                play(n - 2, second, first)
                play(n - 4, second, first)
                return winner
            ## If the amount of coins mod 3 is 1, they will pick 1 or 4 to enforce the above condition
            ## on the second player.
            elif n % 3 == 1:
                play(n - 4, second, first)
                play(n - 1, second, first)
                return winner
            ## If the amount of coins mod 3 is 2, they will pick 2 to enforce the above condition
            ## on the second player.
            elif n % 3 == 2:
                play(n - 2, second, first)
                return winner
                
                
def main():
    ## Parse through command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("coins", help="Number of coins?", type=int)
    parser.add_argument("first", help="Who goes first?", type=str)
    parser.add_argument("second", help="Who goes second?", type=str)
    args = parser.parse_args()

    ## Play the game
    winner1 = play(args.coins, args.first, args.second)

    ## Print the winner and the number of strategies
    print(winner1, strats)

if __name__ == "__main__":
    main()
