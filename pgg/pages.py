from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']


class AfterContributionWP(WaitPage):
    pass


class Punishment(Page):
    def is_displayed(self):
        return self.subsession.punishment

    form_model = 'player'

    def get_form_fields(self):
        return [f'pun_{i.id_in_group}' for i in self.player.get_others_in_group()]


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    pass


page_sequence = [
    Contribution,
    AfterContributionWP,
    Punishment,
    ResultsWaitPage,
    Results
]
