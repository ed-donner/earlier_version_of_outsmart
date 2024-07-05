# Outsmart

## A battle arena of diplomacy and deviousness between LLMs

An Arena in which LLMs compete in a turn-based negotiation game.

### Rules of the game

1. Each player starts with 20 coins
2. With each turn:

- Players send a private message to each of the other players
- Players choose to give one of their coins to a player, and take a coin from a different player
- At the end of the turn, the players receive their private messages and any coins taken/given (with the player name)
- If 2 players give each other coins, and both take from the same player, that is considered a successful alliance and they are rewarded with an extra coin each

3. The objective is to negotiate with the other players and build a strategy to make money. The winner is the player with the most money after 10 moves.

### Installation instructions

Using Anaconda is strongly recommended, to give you a fully consistent environment including the right Python version.

1. If you don't already have Anaconda, you can install it here:

https://docs.anaconda.com/anaconda/install/

2. Create and activate your environment:

`conda create -n outsmart python=3.12.3`

`conda activate outsmart`

3. git clone the repo and install dependencies from the root directory:

`pip install -r requirements.txt`
