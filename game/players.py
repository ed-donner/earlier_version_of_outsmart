from typing import List, Dict, Any
from interfaces.llms import LLM
from prompting.system import instructions
from prompting.user import first_turn


class Player:
    """
    An LLM participating in the Arena
    """

    name: str
    llm: LLM
    other_names: List[str]
    history: Dict[str, Any]
    coins: int

    def __init__(self, name: str, model_name: str, temperature: float):
        """
        Create a new instance of Player
        :param name: The Player's name, as the others will address them
        :param model_name: Which LLM model to use
        :param temperature: The temperature setting for the model, so that different temp models can compete
        """
        self.name = name
        self.llm = LLM.for_model_name(model_name, temperature)
        self.history = {}
        self.coins = 20
        self.other_names = []  # this will be initialized during Arena construction

    def __repr__(self) -> str:
        """
        :return: a String to represent the receiver
        """
        return f"[Player {self.name} with ${self.coins} using {self.llm}]"

    def system_prompt(self) -> str:
        """
        :return: a System Prompt to reflect this player
        """
        return instructions(self.name, self.other_names)

    def user_prompt(self, turn: int) -> str:
        """
        :return: a User prompt to reflect this player in this turn
        """
        if turn == 1:
            return first_turn(self.name, self.other_names, self.coins)
        else:
            return ""

    def make_turn(self, turn: int) -> str:
        """
        Carry out a turn by interfacing with my LLM
        :param turn: which turn number we are on
        :return: a string response
        """
        system_prompt = self.system_prompt()
        user_prompt = self.user_prompt(turn)
        return self.llm.send(system_prompt, user_prompt, 200)
