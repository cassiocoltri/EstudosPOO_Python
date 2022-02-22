"""
Enum -> Normalmente utilizado em conjuntos de programação onde se pode ter várias escolhas, muito útil para economizar
tempo de programação.
"""
from enum import Enum, auto


class Directions(Enum):
    right = auto()  # <-- O auto() esta setando como 1 o primeiro parâmetro, mas dá de colocar qualquer coisa.
    left = auto()
    up = auto()
    down = auto()


def move(direction):
    # if direction != 'right' and direction != 'left':
    #     raise ValueError("Cannot move in this direction")

    if not isinstance(direction, Directions):
        raise ValueError("Cannot move in this direction")

    return f"Moving {direction.name}"  # <-- o ".name" esta pegando o nome da VAR lá en cima na class Directions


if __name__ == "__main__":
    print(move(Directions.right))
    print(move(Directions.left))
    print(move(Directions.up))
    print(move(Directions.down))
    # print(move('qualquer direcao'))
