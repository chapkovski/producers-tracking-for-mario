from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

TIMER_TEXT = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."


def vars_for_all_templates(self):
    transactions = self.group.transactions.all()
    data = []
    for t in transactions:
        i = {}
        i['producer_name'] = t.producer.role
        i['price'] = t.producer.offer_price
        i['product_type'] = t.producer.get_product_type_display()
        i['accepted'] = 'Yes' if t.consumer else 'No'
        data.append(i)
    return {'data': data,}


class CustomPage(Page):
    timer_text = TIMER_TEXT


class CustomWaitPage(WaitPage):
    template_name = 'CSR/AcceptWaitPage.html'


class FirstPage(CustomPage):
    def is_displayed(self):
        return self.round_number == 1


class LastPage(CustomPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


class Instruction(FirstPage):
    timeout_seconds = 2


class Welcome(FirstPage):
    ...


class Assigning_Type(FirstPage):
    form_model = models.Player
    form_fields = ['person_A_type', 'person_B_type', 'person_C_type']
    timeout_seconds = 60


class Assigning_Price(FirstPage):
    form_model = models.Player
    form_fields = ['person_A_price', 'person_B_price', 'person_C_price']
    timeout_seconds = 60


class Offer(Page):
    form_model = models.Player
    form_fields = ['offer_price', 'product_type']
    timeout_seconds = 30

    def is_displayed(self):
        return self.player.role_stub == 'Producer'


class OfferWaitPage(WaitPage):
    ...


class AcceptPage(CustomPage):
    form_model = models.Player
    form_fields = ['accept']
    timeout_seconds = 30
    template_name = 'CSR/Accept.html'

    def order_name(self):
        order_names = ['Erster', 'Zweiter', 'Dritter']
        return order_names[self.att - 1]

    def vars_for_template(self):
        return {'list': self.group.get_players()}

    def before_next_page(self):
        if self.player.accept not in (None, 'None'):
            self.group.transactions.filter(producer__id_in_group=self.player.accept).update(consumer=self.player)
        self.group.got_accepted()

    def accept_choices(self):
        return self.group.get_consumer_choices()

    def is_displayed(self):
        return self.player.att == self.att


class Accept1(AcceptPage):
    att = 1


class AcceptWaitPage(CustomWaitPage):
    ...


class Accept2(AcceptPage):
    att = 2


class Accept3(AcceptPage):
    att = 3


class ProducerWaitPage(CustomWaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(CustomPage):
    def vars_for_template(self):
        return {
            'list': self.group.get_players()
        }

    timeout_seconds = 30
    timer_text = "Es geht automatisch weiter, sobald die Zeit abgelaufen ist."


class FinalPay(LastPage):
    def before_next_page(self):
        self.group.final_payoff()


class Quest_1(LastPage):
    form_model = models.Player
    form_fields = ['good_person', 'social_person', 'effect_participants']
    timeout_seconds = 90


class Quest_2(LastPage):
    form_model = models.Player
    form_fields = ['sex', 'age', 'semester', 'study_subject', 'comment']
    timeout_seconds = 90


class Final(LastPage):
    ...


page_sequence = [
    Welcome,
    Assigning_Type,
    Assigning_Price,
    Instruction,
    Offer,
    OfferWaitPage,
    Accept1,
    AcceptWaitPage,
    Accept2,
    AcceptWaitPage,
    Accept3,
    ProducerWaitPage,
    Results,
    Quest_1,
    Quest_2,
    FinalPay,
    Final,
]
