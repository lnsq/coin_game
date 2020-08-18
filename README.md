# Coin Game

## [Cornell CS2110 Recursion Practice Question 8](https://www.cs.cornell.edu/courses/cs2110/2014fa/L07-Recursion/recursion_practice.pdf)

### Problem:
Alice and Bob are playing a game
using a bunch of coins. The players pick several coins out of the
bunch in turn. Each time a player is allowed to pick 1, 2 or 4 coins,
and the player that gets the last coin is the winner. Assume that
both players are very smart and he/she will try his/her best to
work out a strategy to win the game. For example, if there are 2
coins and Alice is the first player to pick, she will definitely pick 2
coins and win. If there are 3 coins and Alice is still the first player
to pick, no matter she picks 1 or 2 coins, Bob will get the last coin
and win the game. Given the number of coins and the order of
players (which means the first and the second players to pick the
coins), you are required to write a program to calculate the winner
of the game, and calculate how many different strategies there are
for he/she to win the game. You should use recursion to solve
the problem, and the parameters are read from the command line.
You can assume that there are no more than 30 coins.

### Sample Output:
./pickcoin 1 alice bob  
alice 1  
./pickcoin 2 bob alice  
bob 1  
./pickcoin 3 alice bob  
bob 2  
./pickcoin 10 alice bob  
alice 22  
./pickcoin 25 alice bob  
alice 3344  
./pickcoin 30 alice bob  
bob 18272
