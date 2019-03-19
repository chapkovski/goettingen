from . import models
from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants, Player


class StartWP(WaitPage):
    pass


class Intro(Page):
    template_name = 'pggfg/Introduction.html'

    def is_displayed(self):
        return self.subsession.round_number == 1


class Contribute(Page):
    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['contribution']

    def vars_for_template(self):
        label = f'How much will you contribute to the project (from 0 to {self.player.endowment})?'
        x = self.session.config.get('timeout_contribution', 0)
        timer_text = f'Time left to complete this page (if you do not decide, your contribution will be {c(x)}):'
        return {'label': label,
                'timer_text': timer_text
                }

    def contribution_max(self):
        return self.player.endowment

    def before_next_page(self):
        if self.timeout_happened:
            self.player.contribution = self.session.config.get('timeout_contribution', 0)


class AfterContribWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_pd_payoffs()
        for p in self.group.get_players():
            p.set_punishment_endowment()


class Punishment(Page):
    form_model = 'player'

    def is_displayed(self):
        return self.subsession.punishment

    def get_form_fields(self):
        return ['pun{}'.format(p.id_in_group) for p in self.player.get_others_in_group()]

    def vars_for_template(self):
        others = self.player.get_others_in_group()
        form = self.get_form()
        data = zip(others, form)
        return {'data': data}

    def error_message(self, values):
        tot_pun = sum([int(i) for i in values.values()])
        if tot_pun > self.player.punishment_endowment:
            return 'You can\'t send more than {} in total'.format(self.player.punishment_endowment)


class AfterPunishmentWP(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_final_payoffs()


class Results(Page):
    pass


page_sequence = [
    StartWP,
    Intro,
    Contribute,
    AfterContribWP,
    Punishment,
    AfterPunishmentWP,
    Results,
]
