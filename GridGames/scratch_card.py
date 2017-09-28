import random
from typing import List
from GridGames.grid_game_class import GridGame
from GridGames.constants import *
from GridGames.coordinate_parser import CoordinateParser


class ScratchCard(GridGame):

    def __init__(self, host):
        super().__init__(host)
        self.num_winnable_combos = self._roll_num_winnable_combos()
        self.num_columns = 3
        self.grid_size = self.num_columns * self.num_columns
        self.attempts_remaining = self.num_columns * 2
        self.matches_to_win = self.attempts_remaining // 2
        self.card_grid = []
        self.underlying_symbols = []
        self.winning_symbols = []
        self.in_progress = True
        self.input_parser = CoordinateParser(self)
        self.default_values = [empty_tile,
                               empty_tile,
                               empty_tile,
                               one,
                               one,
                               three,
                               three,
                               five,
                               five,
                               ten,
                               ten,
                               hundred]

    def initialize_card(self) -> None:
        self._add_winnable_combo()
        self._add_random_values()
        random.shuffle(self.underlying_symbols)
        self._initialize_grids()

    def get_starting_message(self) -> str:
        host_name = self.host_name
        num_symbols = self.matches_to_win
        num_attempts = self.attempts_remaining
        return '\n'.join([f'New scratch card for {host_name}.',
                          self._render_card(),
                          f'Match {num_symbols} symbols to win!',
                          f'You have {num_attempts} attempts remaining.'])

    def parse_input(self, user_input) -> List[list]:
        return self.input_parser.get_parse(user_input)

    def draw_card_state(self) -> str:
        return '\n'.join(["{}'s scratch card".format(self.host_name),
                          self._render_card()])

    def get_report(self) -> str:
        if self.winning_symbols:
            return self._get_winning_report()
        return 'Sorry, not a winning game.'

    def scratch_tiles(self, user_input) -> None:
        list_coordinates = self.parse_input(user_input)
        for coordinates in list_coordinates:
            x = coordinates[0]
            y = coordinates[1]
            tile = self.card_grid[x][y]
            if self.is_scratchable(tile):
                self._scratch(x, y)
        self._check_game_end()

    def _initialize_grids(self) -> None:
        self.underlying_symbols = self._generate_grid(self.underlying_symbols)
        neutral_tiles = [neutral_tile] * self.grid_size
        self.card_grid = self._generate_grid(neutral_tiles)

    def _roll_num_winnable_combos(self) -> int:
        combos = [1, 1, 2]
        return self._roll(combos)

    def _add_winnable_combo(self) -> None:
        for i in range(self.num_winnable_combos):
            self.underlying_symbols += self._roll_winnable_value()

    def _roll_winnable_value(self) -> List[dict]:
        winnable_symbols = self.remove_value_from(container=self.default_values, filter_value=empty_tile)
        symbol = self._roll(winnable_symbols)
        return [symbol] * self.matches_to_win

    def _add_random_values(self) -> None:
        symbols_remaining = self.grid_size - len(self.underlying_symbols)
        for i in range(symbols_remaining):
            symbol = self._roll(self.default_values)
            self.underlying_symbols.append(symbol)

    def _generate_grid(self, values: List) -> List[list]:
        def create_line(i):
            return [values[i * self.num_columns + j] for j in range(self.num_columns)]
        return [create_line(i) for i in range(self.num_columns)]

    def _render_card(self) -> str:
        column_header = space.join([corner] + column_labels[:self.num_columns])
        tiles = []
        for i, row in enumerate(self.card_grid):
            row_emotes = ''.join(self.get_emotes(row))
            tiles.append(row_labels[i] + row_emotes)
        tile_string = '\n'.join(tiles)
        return '\n'.join([column_header, tile_string])

    def _scratch(self, x, y) -> None:
        chosen_symbol = self.underlying_symbols[x][y]
        self.card_grid[x][y] = chosen_symbol
        self._check_winnable_symbol(chosen_symbol)
        self.attempts_remaining -= 1

    def _check_winnable_symbol(self, symbol) -> None:
        if symbol is not empty_tile:
            self.results.append(symbol)

    def _check_game_end(self) -> None:
        if self.attempts_remaining <= 0:
            self._check_results()
            self.in_progress = False

    def _check_results(self) -> None:
        results = self.results

        def add_if_match(i):
            if i >= self.matches_to_win:
                self.winning_symbols.append(results[0])

        def count_match():
            i = 0
            for result in results:
                if result == results[0]:
                    i += 1
                    add_if_match(i)

        while len(results) > 0:
            count_match()
            results = self.remove_value_from(results, results[0])

    def _get_winning_report(self) -> str:
        payout_stats = '\n'.join([self._symbol_stats(match) for match in self.winning_symbols])
        payout = self.calculate_payout()
        payout_message = ':dollar: Payout is {} gold. :dollar:'.format(payout)
        return '\n'.join(["Winning match!", payout_stats, payout_message])

    @staticmethod
    def _symbol_stats(symbol) -> str:
        return ': '.join([str(symbol[key]) for key in symbol])

    @staticmethod
    def is_scratchable(tile) -> bool:
        return tile is neutral_tile
