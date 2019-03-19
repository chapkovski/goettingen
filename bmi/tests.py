from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        yield (pages.Input, {'height': random.randint(100, 250),
                             'weight': random.randint(10, 300)})
        yield (pages.Results)
