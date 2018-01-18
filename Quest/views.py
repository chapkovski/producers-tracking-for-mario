from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Quest_1(Page):
    form_model= models.Player
    form_fields = ['good_person', 'social_person', 'effect_participants']

    timeout_seconds = 90
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    pass

class Quest_2(Page):
    form_model= models.Player
    form_fields = ['sex', 'age','semester', 'study_subject','comment']

    timeout_seconds = 90
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    pass



class Final(Page):
    pass

class Results(Page):
    pass


page_sequence = [
    Quest_1,
    Quest_2,
    Final,
    Results
]
