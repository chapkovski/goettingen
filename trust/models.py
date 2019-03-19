from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

doc = """
This is an adaptation of a standart Trust game, where partners are matched to be of the same gender (based
on the questionnaire filled before).

The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


class Constants(BaseConstants):
    name_in_url = 'trust'
    players_per_group = None
    num_rounds = 1

    instructions_template = 'trust/Instructions.html'
    trustor, trustee = 'Trustor', 'Trustee'
    # Initial amount allocated to each player
    endowment = c(100)
    multiplication_factor = 3


class Subsession(BaseSubsession):
    mono = models.BooleanField()

    def creating_session(self):
        assert self.session.num_participants % 2 == 0, 'Number of participants should be even!'
        self.mono = self.session.config.get('mono', False)


class Group(BaseGroup):
    sent_amount = models.CurrencyField(
        min=0, max=Constants.endowment,
        doc="""Amount sent by Trustor""",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by Trustee""",
        min=c(0),
    )

    def set_payoffs(self):
        trustor = self.get_player_by_role(Constants.trustor)
        trustee = self.get_player_by_role(Constants.trustee)
        trustor.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        trustee.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount


class Player(BasePlayer):

    def role(self):
        return Constants.trustor if self.id_in_group == 1 else Constants.trustee
