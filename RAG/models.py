from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'RAG'
    players_per_group = 10
    num_rounds = 1
    total_points = 10

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    person_A_type = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_B_type = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_C_type = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_A_price = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_B_price = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_C_price = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)

    pass
