from typing import List


def first_turn(name: str, other_names: List[str], coins: int) -> str:
    """
    :return: a prompt that can be used for a first round user prompt
    """
    others = ", ".join(other_names)
    response = f"""Your player name is {name} and the other players are {others}.
    
    This is the first turn of the game. There have been no interactions between any players yet, and no coins exchanged.
    
    You have {coins} coins.
    
    Please make your first move, by deciding which player to give a coin to, which player to take a coin from, and private messages for each player.
    
    You must respond strictly in JSON, and it must follow this format:
    
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
