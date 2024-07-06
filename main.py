"""
Entry point for the Outsmart Arena LLM Battle
"""

import sys
from dotenv import load_dotenv
import logging

from game.arenas import Arena

root = logging.getLogger()
root.setLevel(logging.INFO)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter(
    "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S %z",
)
handler.setFormatter(formatter)
root.addHandler(handler)


def main():
    load_dotenv()
    arena = Arena.default()
    print(arena.players[2].make_turn(1))


if __name__ == "__main__":
    main()
