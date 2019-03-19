from otree.api import (
    Currency as c, currency_range, SubmissionMustFail, Submission
)
from .pages import *
from otree.api import Bot, SubmissionMustFail, Submission
from .models import Constants, Player
import random


class PlayerBot(Bot):
    def play_round(self):
        if self.round_number == 1:
            yield Intro
        contribution = random.randint(0, self.player.endowment)
        yield Contribute, {'contribution': contribution}

        if self.subsession.punishment:
            pun_fields = ['pun{}'.format(p.id_in_group) for p in self.player.get_others_in_group()]
            _sum = self.player.punishment_endowment

            answers = dict(zip(pun_fields, [1 for _ in pun_fields]))
            yield Punishment, {**answers}
        yield Results
