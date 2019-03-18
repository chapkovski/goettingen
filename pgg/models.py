from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Philipp Chapkovski, Higher School of Economics, Moscow, chapkovski@gmail.com'

doc = """
Public good game.
Treatments: 
- heterogenous/homogenous endowments;
- showing gender of group members;
- punishment.
"""


class Constants(BaseConstants):
    name_in_url = 'pgg'
    players_per_group = 3
    num_rounds = 10
    treatment_params = ['hetero_endowment', 'gender_shown', 'punishment']
    endowment = c(100)
    pun_endowment = c(10)
    lb = c(50)  # upper and lower boundareis for random endowment
    ub = c(150)

    coef = 2
    pun_coef = 2


class Subsession(BaseSubsession):
    hetero_endowment = models.BooleanField(doc='this param defines whether everyone will have '
                                               'the same or random endowment to start with')
    gender_shown = models.BooleanField(doc='whether they will see the gender of their group members when contribute')
    punishment = models.BooleanField(doc='punishment stage (as in Fehr and gaechter')

    def creating_session(self):
        """This code is executed BEFORE session starts. For EACH round (aka subsession)."""
        for i in Constants.treatment_params:
            """We go through a bunch of params defined in constants and read them from config session, and 
            apply them to our subsession object (so we have them stored in db later on to take into account in our
            analysis. """
            v = self.session.config.get(i, False)
            setattr(self, i, v)
        # Generating random/fixed endowment
        if self.hetero_endowment:
            for p in self.get_players():
                p.endowment = random.randint(Constants.lb, Constants.ub)
        else:
            for p in self.get_players():
                p.endowment = Constants.endowment
        #   TODO: REMOVE  ::    FOR DEBUG:
        for p in self.session.get_participants():
            p.vars['gender'] = random.choice(['Male', 'Female'])


class Group(BaseGroup):
    def set_punishemnts(self):
        for p in self.get_players():
            p.set_punishment_sent()
            p.set_punishemnt_received()

    def set_payoffs(self):
        if self.subsession.punishment:
            self.set_punishments()


class Player(BasePlayer):
    endowment = models.CurrencyField()
    contribution = models.CurrencyField()
    punishment_sent = models.CurrencyField()
    punishment_received = models.CurrencyField()

    def set_punishment_sent(self):
        """collects all punishment sent by player and stored as a sum in punishment_sent."""
        pun_sent = sum([getattr(self, f'pun_{i}') for i in range(1, Constants.players_per_group + 1)])
        self.punishment_sent = pun_sent

    def set_punishment_received(self):
        """collects all punishment received by player  from others and stored as a sum in punishment_received."""
        pun_rec = sum([getattr(i, f'pun_{self.id_in_group}') for i in self.get_others_in_group()])
        self.punishment_received = pun_rec


# The following is just a compact way of adding as many punishment fields as there are players per group
for i in range(1, Constants.players_per_group + 1):
    Player.add_to_class(f'pun_{i}', models.IntegerField(min=0))
