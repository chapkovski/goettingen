from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Philipp Chapkovski'

doc = """
Simple BMI app for HSE workshop (see Readme)
original bmi index chart is taken from here:
https://bmicalculator.mes.fm/bmi-chart
"""

"""
Below we create a new class to find easily how current BMI corresponds to categories.
In Constants below we create a variable called bmi_info with a set of BMI objects:
each object has a name (underweight, normal, overweight etc.), lower and upper boundary (left, right)
and alert property - to show a bootstrap alert of corresponding color.
It also has an additional method called check_if_in - when you pass a value there it returns itself, if the value
is between lower and upper value, or None if it isn't. 
That is not the most efficient way of dealing with such kind of tasks but again for didactic reasons can be helpful 
to understand how and why classes are used.

"""
class BMI:
    def __init__(self, name, left, right, alert):
        self.name = name
        self.left = left
        self.right = right
        self.alert = alert

    def check_if_in(self, val):
        if self.left <= val < self.right:
            return self


class Constants(BaseConstants):
    name_in_url = 'bmi'
    players_per_group = None
    num_rounds = 1
    bmi_info = [
        BMI('Underweight', 0, 18.5, 'alert-primary'),
        BMI('Normal', 18.5, 25, 'alert-success'),
        BMI('Overweight', 25, 30, 'alert-warning'),
        BMI('Obese', 30, 40, 'alert-danger'),
        BMI('Extremely Obese', 40, 1000, 'alert-danger')
    ]  # see the comment above


class Subsession(BaseSubsession):
    duo = models.BooleanField()
    def creating_session(self):
        self.duo = self.session.config.get('duo', False)



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    weight = models.IntegerField(min=10, max=300)
    height = models.IntegerField(min=100, max=250)

    def get_bmi(self):
        return round(self.weight / (self.height / 100) ** 2, 2)

    def get_bmi_info(self):
        # we loop through all possible values in our bmi correspondence table from Constants
        # and look for something that fits into this user's data.
        # as soon as we find it, we exit with this data.
        for c in Constants.bmi_info:
            if c.check_if_in(self.get_bmi()):
                return c
        # if corresponding BMI is not found we don't want to generate an error, and we'll still
        # return something
        return BMI('Not defined', 0, 0, 'Not defined')

    def get_other(self):
        # by default get_others_in_group return all players, and since we need a single one, we return this list's
        # first element.
        return self.get_others_in_group()[0]
