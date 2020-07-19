from hashlib import md5

PUZZLE_INPUT = "bwnlcvfs"
GRID_SIZE = 4
OPEN_CHARACTERS = {"b", "c", "d", "e", "f"}

RIGHT = "R"
LEFT = "L"
DOWN = "D"
UP = "U"


class State:
    def __init__(self, row, column, path):
        self.row = row
        self.column = column
        self.path = path

    def next_states(self):
        result = []
        md5_hash = self.__generate_hash()
        for index, direction in enumerate([UP, DOWN, LEFT, RIGHT]):
            if self.__can_move(direction) and State.__is_door_open(md5_hash, index):
                result.append(self.__move(direction))
        return result

    def is_destination(self):
        return self.row == GRID_SIZE and self.column == GRID_SIZE

    def get_path(self):
        return self.path

    def get_path_length(self):
        return len(self.path)

    def __move(self, direction):
        if direction == UP:
            return State(self.row - 1, self.column, self.path + [UP])
        elif direction == DOWN:
            return State(self.row + 1, self.column, self.path + [DOWN])
        elif direction == LEFT:
            return State(self.row, self.column - 1, self.path + [LEFT])
        return State(self.row, self.column + 1, self.path + [RIGHT])

    def __can_move(self, direction):
        return (direction == UP and self.row > 1) or \
               (direction == DOWN and self.row < GRID_SIZE) or \
               (direction == LEFT and self.column > 1) or \
               (direction == RIGHT and self.column < GRID_SIZE)

    def __generate_hash(self):
        value_to_hash = PUZZLE_INPUT + "".join(self.path)
        return md5(value_to_hash.encode()).digest().hex()

    @staticmethod
    def __is_door_open(md5_hash, index):
        return md5_hash[index] in OPEN_CHARACTERS

    @staticmethod
    def initial_state():
        return State(1, 1, [])


def find_shortest_path():
    queue = [State.initial_state()]
    while True:
        state = queue.pop(0)
        if state.is_destination():
            return state.get_path()
        queue.extend(state.next_states())


def find_length_of_longest_path():
    queue = [State.initial_state()]
    longest = 0
    while len(queue) > 0:
        state = queue.pop(0)
        if state.is_destination():
            longest = max(longest, state.get_path_length())
        else:
            queue.extend(state.next_states())
    return longest


shortest_path = "".join(find_shortest_path())
print(f"The shortest path (part 1) is {shortest_path}")

length_of_longest_path = find_length_of_longest_path()
print(f"The length of the longest path (part 2) is {length_of_longest_path}")
