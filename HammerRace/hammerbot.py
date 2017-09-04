from HammerRace.hammermanager import HammerRaceManager


class ClassicHammer(HammerRaceManager):
    # TODO might have its own announcer?

    def __init__(self):
        super().__init__()
        self.init_participants()

    def init_participants(self):
        super().init_participant(short_name='y', name='Yes')
        super().init_participant(short_name='n', name='No')
        hammer = super().init_participant(short_name='h', name=':hammer:')
        self.announcement.overriding_answer = hammer
        super().init_participants()

    def next_round(self):
        super().next_round()

    def check_race_end(self):
        super().check_race_end()

    def round_report(self):
        return super().round_report()

    def winner_report(self):
        return self.announcement.answer() + '\n' + super().winner_report()

class ComparisonHammer(HammerRaceManager):
    """Game mode compares inputted choices.
    Example: /hammer eggs, bread, banana"""

    def __init__(self, message):
        super().__init__()
        self.options = []
        self.set_options(message)
        self.init_participants()

    def set_options(self, message):
        self.options = message.split(',')

    def init_participants(self):
        for option in self.options:
            option = option.strip()
            super().init_participant(short_name=option[0].lower(), name=option)
        super().init_participants()

    def valid_num_participants(self):
        if (self.race.num_participants > 1) & (self.race.num_participants <= 5):
            return True

    def next_round(self):
        super().next_round()

    def check_race_end(self):
        super().check_race_end()

    def round_report(self):
        return super().round_report()

    def winner_report(self):
        return self.announcement.winners()


class VersusHammer(HammerRaceManager):
    """TODO gamemode allows users to join in the race.
    eg. /hammerrace
    """