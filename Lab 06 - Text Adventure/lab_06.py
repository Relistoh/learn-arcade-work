class Cell:
    def __init__(self, description="", s=None, e=None, n=None, w=None):
        self.description = description
        self.n = n
        self.s = s
        self.w = w
        self.e = e

    def print(self):
        print(self.description)

def main():
    cells = []
    cells.append(Cell("The entrance of the saloon.", n=1, w=3, e=2))
    cells.append(Cell("Center of the saloon.", 0, 4, 7, 5))
    cells.append(Cell("A table full of people.", n=4, w=0))
    cells.append(Cell("A piano.", e=0, n=5))
    cells.append(Cell("An empty table.", 2, n=8, w=1))
    cells.append(Cell("The west wall of the saloon", 3, 1, 6))
    cells.append(Cell("Stairs leading upstairs.", 5, 7, 14))
    cells.append(Cell("The barman.", 1, 8, w=6))
    cells.append(Cell("An empty bar chair.", 4, w=7))
    cells.append(Cell("Hallway.", 16, 10))
    cells.append(Cell("Hallway.", 11, 13, w=9))
    cells.append(Cell("A full room.", n=10))
    cells.append(Cell("An empty room.", n=13))
    cells.append(Cell("Hallway.", 12, w=10))
    cells.append(Cell("The second floor.", 16, 10))
    cells.append(Cell("The first floor.", 3, 1, 6))
    cells.append(Cell("Stairs leading downstairs.", 15, n=9))

    current_cell = 0
    done = False

    print("You are in the saloon, try to find an empty room to stay for the night.")
    print()

    while not done:
        cells[current_cell].print()
        print()

        if current_cell == 12:
            print("You win!")
            print()
            break

        next_cell = 0
        player_direction = input("Which direction would you like to go to? (N/S/E/W) ").upper()
        print()
        if player_direction == "N":
            next_cell = cells[current_cell].n
        elif player_direction == "S":
            next_cell = cells[current_cell].s
        elif player_direction == "E":
            next_cell = cells[current_cell].e
        elif player_direction == "W":
            next_cell = cells[current_cell].w
        else:
            print("Invalid direction.")

        if next_cell is None:
            print("You can't go there!")
        else:
            current_cell = next_cell


if __name__ == "__main__":
    main()