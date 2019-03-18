from otree.api import Currency as c, currency_range
from .pages import *
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    cases = ['random', 'min', 'max']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.cs = dict(zip(self.cases, [random.randint(0, self.player.endowment), 0, self.player.endowment]))

    def play_round(self):
        c = self.cs[self.case]
        if self.case == 'random':
            c = random.randint(0, self.player.endowment)
        if self.case == 'min':
            c = 0
        if self.case == 'max':
            c = self.player.endowment
        yield Contribution, {'contribution': c}
        if self.subsession.punishment:
            punsf = [f'pun_{i.id_in_group}' for i in self.player.get_others_in_group()]
            puns = [random.randint(0, Constants.pun_endowment) for _ in punsf]
            yield Punishment, {dict(zip(punsf, puns))}
        yield Results
