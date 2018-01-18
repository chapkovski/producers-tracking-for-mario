from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

class Instruction(Page):

    timeout_seconds = 2
    def is_displayed(self):
        return self.round_number == 1

    def after_all_players_arrive(self):

        pass

class Welcome(Page):

    def is_displayed(self):
        return self.round_number == 1

    pass

class Assigning_Type(Page):
    form_model= models.Player
    form_fields= ['person_A_type', 'person_B_type', 'person_C_type']

    timeout_seconds = 60
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    def is_displayed(self):
        return self.round_number == 1

    pass

class Assigning_Price(Page):
    form_model= models.Player
    form_fields= ['person_A_price', 'person_B_price', 'person_C_price']

    timeout_seconds = 60
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    def is_displayed(self):
        return self.round_number == 1

    pass


class Offer(Page):
    form_model= models.Player
    form_fields= ['offer_price', 'product_type']

    timeout_seconds = 30
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    def is_displayed(self):
        return self.player.role() == 'Producer1' or self.player.role()== 'Producer2' or self.player.role()== 'Producer3'or self.player.role()== 'Producer4'


class OfferWaitPage(WaitPage):
    pass


class ThirdPartyWaitPage(WaitPage):
    pass

class Accept1(Page):
    form_model= models.Player
    form_fields = ['accept']

    timeout_seconds = 30
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    def vars_for_template(self):
        return {'list': self.group.get_players()}

    def before_next_page(self):
        self.group.got_accepted()



#    def vars_for_template(self):
#        return {
#            'player_in_actual_round': self.player.in_round(number),
#        }

    def is_displayed(self):
        return self.player.att == 1

class AcceptWaitPage(WaitPage):
    pass

class Accept2(Page):
    form_model= models.Player
    form_fields = ['accept']

    timeout_seconds = 30
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    def vars_for_template(self):
        return {'list': self.group.get_players()}

    def before_next_page(self):
        self.group.got_accepted()

    def is_displayed(self):
        return self.player.att == 2

    def accept_choices(self):
        for p in self.group.get_players():
            if p.accept == "Annahme Angebot 1":
                return ['Annahme Angebot 2', 'Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 2":
                return ['Annahme Angebot 1', 'Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 3":
                return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 4":
                return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 3', 'Keine Angebotsannahme']
            if p.accept == "Keine Angebotsannahme":
                return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme']


class Accept3(Page):
    form_model= models.Player
    form_fields = ['accept']

    timeout_seconds = 30
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    def vars_for_template(self):
        return {'list': self.group.get_players()}

    def before_next_page(self):
        self.group.got_accepted()

    def is_displayed(self):
        return self.player.att == 3

    def accept_choices(self):
        for p in self.group.get_players():
            if p.accept == "Annahme Angebot 1":
                for a in self.group.get_players():
                    if a.accept == "Annahme Angebot 2":
                        return ['Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 1":
                for a in self.group.get_players():
                    if a.accept == "Annahme Angebot 3":
                        return ['Annahme Angebot 2', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 1":
                for a in self.group.get_players():
                    if a.accept=="Annahme Angebot 4":
                        return ['Annahme Angebot 2', 'Annahme Angebot 3', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 1":
                for a in self.group.get_players():
                    if a.accept=="Keine Angebotsannahme":
                        return ['Annahme Angebot 2','Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 2":
                for a in self.group.get_players():
                    if a.accept == "Annahme Angebot 3":
                        return ['Annahme Angebot 1', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 2":
                for a in self.group.get_players():
                    if a.accept == "Annahme Angebot 4":
                        return ['Annahme Angebot 1', 'Annahme Angebot 3', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 2":
                for a in self.group.get_players():
                    if a.accept == "Keine Angebotsannahme":
                        return ['Annahme Angebot 1', 'Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 3":
                for a in self.group.get_players():
                    if a.accept == "Annahme Angebot 4":
                        return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 3":
                for a in self.group.get_players():
                    if a.accept =="Keine Angebotsannahme":
                        return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Annahme Angebot 4":
                for a in self.group.get_players():
                    if a.accept =="Keine Angebotsannahme":
                        return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 3', 'Keine Angebotsannahme']
            if p.accept == "Keine Angebotsannahme":
                if p.role == "Consumer1":
                    for a in self.group.get_players():
                        if a.accept == "Keine Angebotsannahme":
                            if a.role == "Consumer2":
                                return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme']
                            if a.role == "Consumer3":
                                return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme']
            if p.accept == "Keine Angebotsannahme" and p.role == "Consumer2":
                if p. role == "Consumer 2":
                    for a in self.group.get_players():
                        if a.accept == "Keine Angebotsannahme":
                            if a.role == "Consumer3":
                                return ['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 3', 'Annahme Angebot 4','Keine Angebotsannahme']



class ProducerWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    def vars_for_template(self):
        return {
            'list': self.group.get_players()
        }


    timeout_seconds = 30
    timer_text= "Es geht automatisch weiter, sobald die Zeit abgelaufen ist."

    pass

class FinalPay(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def before_next_page(self):
        self.group.final_payoff()

#    def vars_for_template(self):
#        return {
#            'paying_round': self.session.vars['paying_round'],
#            'final_payoff': self.player.payoff in self.player.round_number('paying_round')
#        }

    pass

class Quest_1(Page):
    form_model= models.Player
    form_fields = ['good_person', 'social_person', 'effect_participants']

    timeout_seconds = 90
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    pass

class Quest_2(Page):
    form_model= models.Player
    form_fields = ['sex', 'age','semester', 'study_subject','comment']

    timeout_seconds = 90
    timer_text = "Damit es zu keinen Verzögerungen kommt, bitten wir Sie, schnellst möglich eine Auswahl zu treffen."

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    pass



class Final(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    pass


page_sequence = [
    Welcome,
    Assigning_Type,
    Assigning_Price,
    Instruction,
    Offer,
    OfferWaitPage,
    ThirdPartyWaitPage,
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
