from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Input(Page):
    form_model = 'player'
    form_fields = ['height', 'weight']


class ResultsWaitPage(WaitPage):
    def is_displayed(self):
        # if this is interpersonal treatment (in other words 'individual' is False in settings then
        # they should wait for the partner. It is not necessary if we are in individual treatment
        return not self.session.config.get('individual')

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Input,
    ResultsWaitPage,
    Results
]
