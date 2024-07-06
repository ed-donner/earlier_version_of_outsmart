from typing import List, Self
from game.players import Player
from game.referees import Referee
import random


class Arena:
    """
    The manager of multiple Players competing in Outsmart
    """

    players: List[Player]
    turn: int

    def __init__(self, players: List[Player]):
        """
        Create a new instance of the receiver
        Set the 'other players' field for each player. Shuffle it to reduce any bias on the order in which players
        are listed.
        :param players: the players to use
        """
        self.players = players
        for player in self.players:
            others = [p.name for p in players if p.name != player.name]
            random.shuffle(others)
            player.other_names = others
        self.turn = 1

    def __repr__(self) -> str:
        """
        :return: a string to represent the receiver
        """
        result = f"Arena at turn {self.turn} with {len(self.players)} players:\n"
        for player in self.players:
            result += f"{player}\n"
        return result

    def do_turn(self):
        """
        Carry out a Turn; delegate to a Referee to manage this process
        """
        ref = Referee(self.players, self.turn)
        ref.do_turn()
        self.turn += 1

    @classmethod
    def default(cls) -> Self:
        """
        Return a new insteance of Arena with default players
        :return: an Arena instance
        """
        names = ["Alex", "Blake", "Claude"]
        model_names = ["gpt-3.5-turbo", "claude-3-haiku-20240307", "gemini-pro"]
        temperatures = [0.7, 0.7, 0.7]
        players = []
        for data in zip(names, model_names, temperatures):
            players.append(Player(data[0], data[1], data[2]))
        return cls(players)
