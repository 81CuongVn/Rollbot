import random
from typing import List


class SlotMachine:
    def __init__(self, author):
        self.player = author
        self.num_rows = 3
        self.winning_symbols = []
        self.cherry = {'emote': ':cherries:', 'value': 1}
        self.angel = {'emote': ':angel:', 'value': 3}
        self.pear = {'emote': ':pear:', 'value': 5}
        self.pineapple = {'emote': ':pineapple:', 'value': 7}
        self.butt = {'emote': ':peach:', 'value': 10}
        self.meat = {'emote': ':meat_on_bone:', 'value': 15}
        self.hammer = {'emote': ':hammer:', 'value': 25}
        self.seven = {'emote': ':seven:', 'value': 100}

    def get_outcomes(self):
        return [self.cherry, self.cherry, self.cherry,
                self.angel, self.angel, self.angel,
                self.pear, self.pear,
                self.pineapple, self.pineapple,
                self.butt, self.butt,
                self.meat, self.meat,
                self.hammer, self.hammer,
                self.seven]

    def play_slot(self):
        linebreak = '\n'
        results = [self.roll_row() for i in range(self.num_rows)]
        self.analyze_results(results)
        label = "| {}'s slot results |".format(self.player)
        return linebreak.join([label, self.draw_slot_interface(results), self.get_outcome_report()])

    def roll_row(self):
        return [self.roll() for i in range(self.num_rows)]

    def roll(self):
        outcomes = self.get_outcomes()
        pick = random.randint(0, len(outcomes) - 1)
        return outcomes[pick]

    def analyze_results(self, results):
        for row in results:
            self.check_winning_match(row)
        self.check_diagonals(results)

    def check_diagonals(self, results):
        top_left_diagonal = [row[i] for i, row in enumerate(results)]
        reversed_rows = reversed(results)
        top_right_diagonal = [row[j] for j, row in enumerate(reversed_rows)]
        self.check_winning_match(top_left_diagonal)
        self.check_winning_match(top_right_diagonal)

    def check_winning_match(self, symbols: List[dict]):
        first_item = symbols[0]
        for item in symbols:
            if item != first_item:
                return
        self.add_winning_match(first_item)

    def add_winning_match(self, symbol: dict):
        self.winning_symbols.append(symbol)

    def has_winnings(self):
        return len(self.winning_symbols) > 0

    def get_payout(self):
        payout = 0
        for symbol in self.winning_symbols:
            payout += symbol['value']
        return payout

    def get_winning_symbols(self):
        return [self.get_stats(symbol) for symbol in self.winning_symbols]

    @staticmethod
    def get_stats(symbol):
        emote = symbol['emote']
        value = str(symbol['value'])
        return ': '.join([emote, value])

    @staticmethod
    def draw_slot_interface(results):
        linebreak = '\n'

        def get_emotes(symbol_list):
            return ''.join([symbol['emote'] for symbol in symbol_list])

        return linebreak.join([get_emotes(row) for row in results])

    def get_outcome_report(self):
        if self.has_winnings():
            linebreak = '\n'
            winning_stats = linebreak.join(self.get_winning_symbols())
            payout = self.get_payout()
            return f"Rolled a match! \n{winning_stats} \n :dollar: Payout is {payout} gold. :dollar:"
        else:
            return "Sorry, not a winning game."