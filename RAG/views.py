from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Willkommen(Page):

    pass

class Assigning_Points(Page):
    form_model= models.Player
    form_fields= ['person_A_type', 'person_B_type', 'person_C_type']

    timeout_seconds = 60
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."
    pass

class Assigning_PointsPrice(Page):
    form_model= models.Player
    form_fields= ['person_A_price', 'person_B_price', 'person_C_price']

    timeout_seconds = 60
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Willkommen,
    ResultsWaitPage,
    Assigning_Points,
    Assigning_PointsPrice,
    ResultsWaitPage,
    Results
]
