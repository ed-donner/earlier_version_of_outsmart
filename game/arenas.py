from typing import List, Self
from game.players import Player


class Arena:
    """
    The manager of multiple Players competing in Outsmart
    """

    players: List[Player]
    turn: int

    def __init__(self, players: List[Player]):
        """
        Create a new instance of the receiver
        :param players: the players to use
        """
        self.players = players
        for player in self.players:
            player.other_names = [p.name for p in players if p.name != player.name]
        self.turn = 1

    def __repr__(self) -> str:
        """
        :return: a string to represent the receiver
        """
        result = f"Arena at turn {self.turn} with {len(self.players)} players:\n"
        for player in self.players:
            result += f"{player}\n"
        return result

    @classmethod
    def default(cls) -> Self:
        """
        Return a new insteance of Arena with default players
        :return: an Arena instance
        """
        names = ["Alex", "Blake", "Claude"]
        model_names = ["gpt-3.5-turbo", "claude-3-haiku-20240307", "gemini-pro"]
        temperatures = [1.0, 1.0, 1.0]
        players = []
        for data in zip(names, model_names, temperatures):
            players.append(Player(data[0], data[1], data[2]))
        return cls(players)
