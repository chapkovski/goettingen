from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants


class SortingWP(WaitPage):
    group_by_arrival_time = True

    def is_displayed(self):
        self.participant.vars['passed'] = True
        return True

    def get_players_for_group(self, waiting_players):
        if self.subsession.mono:
            w = [p for p in waiting_players if p.participant.vars.get('gender') == 'Female']
            m = [p for p in waiting_players if p.participant.vars.get('gender') == 'Male']
            for i in [w, m]:
                if len(i) >= 2:
                    return i[:2]
            unpassed = [p for p in self.session.get_participants() if not p.vars.get('passed')]
            if len(unpassed) == 0:
                return waiting_players[:2]
        else:
            if len(waiting_players) >= 2:
                return waiting_players[:2]


class Introduction(Page):
    pass


class Send(Page):
    """This page is only for Trustor
    P1 sends amount (all, some, or none) to P2
    This amount is tripled by experimenter,
    i.e if sent amount by P1 is 5, amount received by P2 is 15"""

    form_model = 'group'
    form_fields = ['sent_amount']

    def is_displayed(self):
        return self.player.role() == Constants.trustor


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    """This page is only for Trustee
    Trustor sends back some amount (of the tripled amount received) to Trustee"""

    form_model = 'group'
    form_fields = ['sent_back_amount']

    def is_displayed(self):
        return self.player.role() == Constants.trustee

    def vars_for_template(self):
        tripled_amount = self.group.sent_amount * Constants.multiplication_factor

        return {
            'tripled_amount': tripled_amount,
            'prompt': f'Please an amount from 0 to {tripled_amount}'}

    def sent_back_amount_max(self):
        return self.group.sent_amount * Constants.multiplication_factor


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """This page displays the earnings of each player"""

    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor
        }


page_sequence = [
    SortingWP,
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultsWaitPage,
    Results,
]
