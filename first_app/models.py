from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'first_app'
    players_per_group = None
    num_rounds = 1
    coef = 2

class Subsession(BaseSubsession):
    def creating_session(self):
       pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    t = models.IntegerField()
