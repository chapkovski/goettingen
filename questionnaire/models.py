from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import csv

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'questionnaire'
    players_per_group = None
    num_rounds = 1

    with open('questionnaire/qs.csv') as f:
        qs = list(csv.DictReader(f))


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


for q in Constants.qs:
    Player.add_to_class(q['name'], models.StringField(choices=q['choices'].split(';'), label=q['label']))
