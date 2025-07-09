import random
from constants import color
from constants import strip_ansi
from constants import format_cell

class GameMap():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.world_map = [['' for _ in range(width)] for _ in range(height)]


    def print_map(self, x, y, world_map, see_all=True):
        for i in world_map:
            print('\n' + '+---' * self.width + '+')
            for j in i:
                cell = format_cell(j if j else '', see_all)
                visible = strip_ansi(cell)
                pad = 3 + len(cell) - len(visible)
                print('|{:^{width}}'.format(cell, width=pad), end='')
            print('|', end='')
        print('\n' + '+---' * self.width + '+')


    def set_tile(self, x, y, tile_type):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.world_map[y][x] = tile_type
        elif x < 0 or y < 0:
            print("Invalid Position: Coordinates cannot be negative.")
        else:
            print("Invalid Position: Coordinates out of bounds.")

    def get_tile(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.world_map[y][x]
        else:
            print("Invalid position: Coordinates out of bounds.")
            return None
            
    def generate_map(self):

        total_tiles = self.width * self.height
        num_special = max(2, round(total_tiles * 0.75))
        positions = [(y, x) for y in range(self.height) for x in range(self.width)]

        start_pos = (0, 0)
        positions.remove(start_pos)

        exit_pos = (self.height - 1, self.width - 1)
        positions.remove(exit_pos)

        chosen = random.sample(positions, num_special)

        m_pos = random.choice(chosen)
        q_pos = random.choice([pos for pos in chosen if pos != m_pos])

        self.world_map[m_pos[0]][m_pos[1]] = 'M'
        self.world_map[q_pos[0]][q_pos[1]] = '?'

        for pos in chosen:
            if pos == m_pos or pos == q_pos:
                continue
            self.world_map[pos[0]][pos[1]] = random.choice(['M', '?'])

        self.world_map[exit_pos[0]][exit_pos[1]] = 'E'
        self.world_map[start_pos[0]][start_pos[1]] = 'H'


            
