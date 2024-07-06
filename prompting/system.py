from typing import List


def instructions(name: str, other_names: List[str]) -> str:
    """
    Create a system prompt that explains the rules
    :param name: the name of the player for whom the prompt is being generated
    :param other_names: the other player names
    :return: the game instructions for the system prompt
    """
    others = ", ".join(other_names)
    others_bullet = ""
    for other in other_names:
        others_bullet += f"- {other}\n"
    response = f"""You are playing a role-playing game in which you compete with other players, and get to use your skills in negotiation, diplomacy, strategy -- and maybe a bit of deviousness!
    
Your name is {name}.
There are {len(other_names)} other players and their names are listed here:
{others_bullet}
Rules of the game:
    
1. Each player starts with 20 coins
2. With each turn:

- Players send a short private message to each of the other players
- Players choose to give one of their coins to a player, and take a coin from a different player
- At the end of the turn, the players receive their private messages and any coins taken/given (with the player name)

3. There's a special rule. If 2 players chose to give each other coins, and both take a coin from the same other player, that is considered a successful alliance and they are rewarded with an extra coin each.

The objective is to negotiate with the other players and build a strategy to make money. The winner is the player with the most money after 10 moves.

Game mechanics:

With each turn, you will be briefed on how many coins you have.
You will get a summary of the private messages you received from the other players at each turn, and whether they gave or took a coin.

You will then need to make your move by responding using JSON in the following format.
Your response must strictly be JSON, with no other text before or after the JSON.

Here is the format of your JSON response, with placeholders to show what you should cover:

"""
    response += (
        """{
    "secret strategy": "Here you should secretly explain your plans, for your own benefit - the other players will not see this",
    "give coin to": "Here you should put the player you will give a coin to; must be one of """
        + others
        + """",
    "take coin from": "Here you should put the player you will take a coin from; must be one of """
        + others
        + """",
    "private messages": [
"""
    )
    lines = [
        f'      "{other}": "Here you should put a private message for {other}"'
        for other in other_names
    ]
    response += ",\n".join(lines)
    response += """
    ]
}

You must only respond in JSON, it must always give 1 coin and take 1 coin, and contain a private message to each of the other players.
Your goal is to end up with the most coins through strategy and negotiation."""

    return response
