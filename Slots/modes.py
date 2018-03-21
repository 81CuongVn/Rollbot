import random
from typing import List

from Slots.bias_mechanic import SlotsBias
from Slots.symbols import *

from Slots.slot_machine import SlotMachine


class BigSlots(SlotMachine):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.num_columns = 5
        self.payout_multiplier = 1.5
        self.init_reel_size = self.num_columns * 2
        self.bias_mechanic = BigSlotsBias(self)


class BigSlotsBias(SlotsBias):
    def __init__(self, slot_machine):
        super().__init__(slot_machine)

    def _get_bias_options(self) -> List[int]:
        first_row = 0
        last_row = self.num_columns - 1
        random_index = random.randint(first_row, last_row)
        no_bias = -1
        return [random_index, random_index, random_index, random_index, first_row, last_row, no_bias, no_bias]


class GiantSlots(SlotMachine):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.num_columns = 7
        self.payout_multiplier = 2
        self.bias_mechanic = GiantSlotsBias(self)


class GiantSlotsBias(SlotsBias):
    def __init__(self, slot_machine):
        super().__init__(slot_machine)

    def _get_bias_options(self) -> List[int]:
        first_row = 0
        last_row = self.num_columns - 1
        random_index = random.randint(first_row, last_row)
        no_bias = -1
        return [random_index, random_index, first_row, last_row, no_bias]


class ClassicSlots(SlotMachine):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.default_outcomes = [CHERRY, CHERRY,
                                 STRAWBERRY, STRAWBERRY,
                                 PEAR, PEAR,
                                 PINEAPPLE, PINEAPPLE,
                                 CHICKEN,
                                 GRAPES,
                                 MEAT,
                                 FLYING_MONEY,
                                 PANCAKE,
                                 LEMON,
                                 HAMMER,
                                 SPAGHETTI,
                                 CAKE,
                                 DOUGHNUT,
                                 MELON,
                                 BAR,
                                 WATERMELON,
                                 EGGPLANT,
                                 SEVEN,
                                 BUTT
                                 ]

    @staticmethod
    def get_win_message(matches, winning_stats, payout) -> str:
        linebreak = '\n'
        return linebreak.join([f'Rolled {matches}!',
                               f'{winning_stats}',
                               f':dollar: Payout is {payout} gold. :dollar:'])


class BigClassicSlots(BigSlots, ClassicSlots):
    def __init__(self, ctx):
        super().__init__(ctx)


class GiantClassicSlots(GiantSlots, ClassicSlots):
    def __init__(self, ctx):
        super().__init__(ctx)


class MapleSlots(SlotMachine):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.default_outcomes = [BUBBLING, BUBBLING,
                                 WARBOW, WARBOW,
                                 MUSHROOM, MUSHROOM,
                                 SLIME, SLIME,
                                 KUMBI,
                                 PINKY,
                                 OCTOPUS,
                                 PIGGY,
                                 PEPE,
                                 MESOCOIN,
                                 PICO,
                                 STEELY,
                                 MAPLE_CAKE,
                                 MAPLE_STAR,
                                 MESOBAG,
                                 LOLLY,
                                 GIFT,
                                 MAPLE_CANDY,
                                 PINK_DRAGON,
                                 PANLID]

    @staticmethod
    def get_win_message(matches, winning_stats, payout) -> str:
        linebreak = '\n'
        mesowad = '<:mesowad:246852286993793025>'
        return linebreak.join([f'Rolled {matches}!',
                               f'{winning_stats}',
                               f'{mesowad} Payout is {payout} mesos. {mesowad}'])


class BigMapleSlots(BigSlots, MapleSlots):
    def __init__(self, ctx):
        super().__init__(ctx)


class GiantMapleSlots(GiantSlots, MapleSlots):
    def __init__(self, ctx):
        super().__init__(ctx)


class PokeSlots(SlotMachine):
    def __init__(self, ctx):
        super().__init__(ctx)
        self.default_outcomes = [MAGIKARP, MAGIKARP,
                                 PIDGEY, PIDGEY,
                                 WEEPINBELL, WEEPINBELL,
                                 PSYDUCK, PSYDUCK,
                                 KOFFING,
                                 JIGGLYPUFF,
                                 ROWLET,
                                 NATU,
                                 MAREEP,
                                 EEVEE,
                                 MARILL,
                                 SLOWBRO,
                                 MUDKIP,
                                 FARFETCHD,
                                 WHIMSICOTT,
                                 WAILORD,
                                 SNORLAX,
                                 KANGASKHAN,
                                 HONCHKROW,
                                 PIKACHU,
                                 GOLD_MAGIKARP]
    @staticmethod
    def get_win_message(matches, winning_stats, payout) -> str:
        linebreak = '\n'
        yen = '<:yencoin:425874186138026005>'
        return linebreak.join([f'Rolled {matches}!',
                               f'{winning_stats}',
                               f'{yen} Payout is {payout} ¥. {yen}'])


class BigPokeSlots(BigSlots, PokeSlots):
    def __init__(self, ctx):
        super().__init__(ctx)


class GiantPokeSlots(GiantSlots, PokeSlots):
    def __init__(self, ctx):
        super().__init__(ctx)