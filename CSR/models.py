from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""

import random
import itertools

class Constants(BaseConstants):
    name_in_url = 'csr'
    players_per_group = 7
    num_rounds = 1
    endowment = 100
    cost_production= 20
    value_product = 50
    loss_dirty_product = 60
    type_product = ["dirty", "clean"]
    numbers = [1,2,3]


class Subsession(BaseSubsession):

    def creating_session(self):

        if self.round_number == 1:
            self.session.vars['part_payoff'] = random.randint(1,2)
            self.session.vars['rand_quest'] = random.randint(1,6)
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round
            self.group_randomly()
        if self.round_number > 1:
            self.group_like_round(1)
        if self.round_number >= 1:
            attribute = Constants.numbers.copy()
            random.shuffle(attribute)
            for p in self.get_players():
                if p.id_in_group == 5:
                    p.att = attribute[0]
                if p.id_in_group == 6:
                    p.att = attribute [1]
                if p.id_in_group == 7:
                    p.att = attribute[2]



class Group(BaseGroup):
    i=models.IntegerField()
    j=models.IntegerField()
    k=models.IntegerField()
    l=models.IntegerField()

    def final_payoff(self):
        if self.session.vars['part_payoff'] == 1:
            if self.session.vars['rand_quest'] == 1:
                self.i = 0
                self.j = 0
                self.k = 0
                self.l = 0
                for p in self.get_players():
                    if p.person_A_type == "Gar nicht verantwortlich":
                        self.i=self.i+1
                    if p.person_A_type == "Eher nicht verantwortlich":
                        self.j=self.j+1
                    if p.person_A_type == "Eher verantwortlich":
                        self.k=self.k+1
                    if p.person_A_type == "Sehr verantwortlich":
                        self.l=self.l+1
                most = [self.i, self.j, self.k, self.l]
                most_chosen = max(most)
                for p in self.get_players():
                    p.final_payoff=0
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_A_type == "Gar nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_A_type == "Eher nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_A_type == "Eher verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_A_type == "Sehr verantwortlich":
                            p.final_payoff = 10

            if self.session.vars['rand_quest'] == 2:
                self.i = 0
                self.j = 0
                self.k = 0
                self.l = 0
                for p in self.get_players():
                    if p.person_B_type== "Gar nicht verantwortlich":
                        self.i=self.i+1
                    if p.person_A_price == "Eher nicht verantwortlich":
                        self.j=self.j+1
                    if p.person_B_type== "Eher verantwortlich":
                        self.k=self.k+1
                    if p.person_B_type== "Sehr verantwortlich":
                        l=l+1
                most = [self.i, self.j, self.k, self.l]
                most_chosen = max(most)
                Player.final_payoff=0
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_B_type == "Gar nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_B_type == "Eher nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_B_type == "Eher verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_B_type == "Sehr verantwortlich":
                            p.final_payoff = 10

            if self.session.vars['rand_quest'] == 3:
                self.i = 0
                self.j = 0
                self.k = 0
                self.l = 0
                for p in self.get_players():
                    if p.person_C_type== "Gar nicht verantwortlich":
                        self.i=self.i+1
                    if p.person_A_price == "Eher nicht verantwortlich":
                        self.j=self.j+1
                    if p.person_C_type== "Eher verantwortlich":
                        self.k=self.k+1
                    if p.person_C_type== "Sehr verantwortlich":
                        self.l=self.l+1
                most = [self.i, self.j, self.k, self.l]
                most_chosen = max(most)
                for p in self.get_players():
                    p.final_payoff=0
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_C_type == "Gar nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_C_type == "Eher nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_C_type == "Eher verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_C_type == "Sehr verantwortlich":
                            p.final_payoff = 10

            if self.session.vars['rand_quest'] == 4:
                self.i = 0
                self.j = 0
                self.k = 0
                self.l = 0
                for p in self.get_players():
                    if p.person_A_price== "Gar nicht verantwortlich":
                        self.i=self.i+1
                    if p.person_A_price == "Eher nicht verantwortlich":
                        self.j=self.j+1
                    if p.person_A_price== "Eher verantwortlich":
                        self.k=self.k+1
                    if p.person_A_price== "Sehr verantwortlich":
                        self.l=self.l+1
                most = [self.i, self.j, self.k, self.l]
                most_chosen = max(most)
                for p in self.get_players():
                    p.final_payoff=0
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_A_price == "Gar nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_A_price == "Eher nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_A_price == "Eher verantwortlich":
                            p.final_payoff = 10
                if most_chosen == j:
                    for p in self.get_players():
                        if p.person_A_price == "Sehr verantwortlich":
                            p.final_payoff = 10

            if self.session.vars['rand_quest'] == 5:
                self.i = 0
                self.j = 0
                self.k = 0
                self.l = 0
                for p in self.get_players():
                    if p.person_B_price== "Gar nicht verantwortlich":
                        self.i=self.i+1
                    if p.person_B_price == "Eher nicht verantwortlich":
                        self.j=self.j+1
                    if p.person_B_price== "Eher verantwortlich":
                        self.k=self.k+1
                    if p.person_B_price== "Sehr verantwortlich":
                        self.l=self.l+1
                most = [self.i, self.j, self.k, self.l]
                most_chosen = max(most)
                for p in self.get_players():
                    p.final_payoff=0
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_B_price == "Gar nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_B_price == "Eher nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_B_price == "Eher verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_B_price == "Sehr verantwortlich":
                            p.final_payoff = 10

            if self.session.vars['rand_quest'] == 6:
                self.i = 0
                self.j = 0
                self.k = 0
                self.l = 0
                for p in self.get_players():
                    if p.person_C_price== "Gar nicht verantwortlich":
                        self.i=self.i+1
                    if p.person_B_price == "Eher nicht verantwortlich":
                        self.j=self.j+1
                    if p.person_C_price== "Eher verantwortlich":
                        self.k=self.k+1
                    if p.person_C_price== "Sehr verantwortlich":
                        self.l=self.l+1
                most = [self.i, self.j, self.k, self.l]
                most_chosen = max(most)
                for p in self.get_players():
                    p.final_payoff=0
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_C_price == "Gar nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_C_price == "Eher nicht verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.i:
                    for p in self.get_players():
                        if p.person_C_price == "Eher verantwortlich":
                            p.final_payoff = 10
                if most_chosen == self.j:
                    for p in self.get_players():
                        if p.person_C_price == "Sehr verantwortlich":
                            p.final_payoff = 10

        if self.session.vars['part_payoff'] == 2:
            pay_round = self.session.vars['paying_round']
            for p in self.get_players():
                p.final_payoff = p.in_round(pay_round).payoff

    def got_accepted(self):
        p1=self.get_player_by_role("Producer1")
        p2=self.get_player_by_role("Producer2")
        p3= self.get_player_by_role("Producer3")
        p4= self.get_player_by_role("Producer4")
        c1= self.get_player_by_role("Consumer1")
        c2 = self.get_player_by_role("Consumer2")
        c3 = self.get_player_by_role("Consumer3")
        if c1.accept == "Annahme Angebot 1" or c2.accept=="Annahme Angebot 1" or c3.accept=="Annahme Angebot 1":
            p1.got_accepted=True
        if c1.accept == "Annahme Angebot 2" or c2.accept == "Annahme Angebot 2" or c3.accept == "Annahme Angebot 2":
            p2.got_accepted = True
        if c1.accept == "Annahme Angebot 3" or c2.accept=="Annahme Angebot 3" or c3.accept=="Annahme Angebot 3":
            p3.got_accepted=True
        if c1.accept == "Annahme Angebot 4" or c2.accept=="Annahme Angebot 4" or c3.accept=="Annahme Angebot 4":
            p4.got_accepted=True

        if c1.accept == "Annahme Angebot 1" and c1.att==1:
            p1.order_acceptance=1
        if c1.accept == "Annahme Angebot 2"and c1.att==1:
            p2.order_acceptance=1
        if c1.accept == "Annahme Angebot 3"and c1.att==1:
            p3.order_acceptance=1
        if c1.accept == "Annahme Angebot 4"and c1.att==1:
            p4.order_acceptance=1

        if c1.accept == "Annahme Angebot 1" and c1.att ==2:
            p1.order_acceptance = 2
#            for p in self.get_players():
#                if p.att==1 and p.accept =="Keine Angebotsannahme":
#                    p1.order_acceptance =1
        if c1.accept == "Annahme Angebot 2" and c1.att ==2:
            p2.order_acceptance = 2
        if c1.accept == "Annahme Angebot 3" and c1.att ==2:
            p3.order_acceptance = 2
        if c1.accept == "Annahme Angebot 4" and c1.att ==2:
            p4.order_acceptance = 2

        if c1.accept == "Annahme Angebot 1" and c1.att==3:
            p1.order_acceptance=3
        if c1.accept == "Annahme Angebot 2"and c1.att==3:
            p2.order_acceptance=3
        if c1.accept == "Annahme Angebot 3"and c1.att==3:
            p3.order_acceptance=3
        if c1.accept == "Annahme Angebot 4"and c1.att==3:
            p4.order_acceptance=3

        if c2.accept == "Annahme Angebot 1"and c2.att==1:
            p1.order_acceptance=1
        if c2.accept == "Annahme Angebot 2"and c2.att==1:
            p2.order_acceptance=1
        if c2.accept == "Annahme Angebot 3"and c2.att==1:
            p3.order_acceptance=1
        if c2.accept == "Annahme Angebot 4"and c2.att==1:
            p4.order_acceptance=1

        if c2.accept == "Annahme Angebot 1"and c2.att==2:
            p1.order_acceptance=2
        if c2.accept == "Annahme Angebot 2"and c2.att==2:
            p2.order_acceptance=2
        if c2.accept == "Annahme Angebot 3"and c2.att==2:
            p3.order_acceptance=2
        if c2.accept == "Annahme Angebot 4"and c2.att==2:
            p4.order_acceptance=2

        if c2.accept == "Annahme Angebot 1"and c2.att==3:
            p1.order_acceptance=3
        if c2.accept == "Annahme Angebot 2"and c2.att==3:
            p2.order_acceptance=3
        if c2.accept == "Annahme Angebot 3"and c2.att==3:
            p3.order_acceptance=3
        if c2.accept == "Annahme Angebot 4"and c2.att==3:
            p4.order_acceptance=3

        if c3.accept == "Annahme Angebot 1"and c3.att==1:
            p1.order_acceptance=1
        if c3.accept == "Annahme Angebot 2"and c3.att==1:
            p2.order_acceptance=1
        if c3.accept == "Annahme Angebot 3"and c3.att==1:
            p3.order_acceptance=1
        if c3.accept == "Annahme Angebot 4"and c3.att==1:
            p4.order_acceptance=1

        if c3.accept == "Annahme Angebot 1"and c3.att==2:
            p1.order_acceptance=2
        if c3.accept == "Annahme Angebot 2"and c3.att==2:
            p2.order_acceptance=2
        if c3.accept == "Annahme Angebot 3"and c3.att==2:
            p3.order_acceptance=2
        if c3.accept == "Annahme Angebot 4"and c3.att==2:
            p4.order_acceptance=2

        if c3.accept == "Annahme Angebot 1"and c3.att==3:
            p1.order_acceptance=3
        if c3.accept == "Annahme Angebot 2"and c3.att==3:
            p2.order_acceptance=3
        if c3.accept == "Annahme Angebot 3"and c3.att==3:
            p3.order_acceptance=3
        if c3.accept == "Annahme Angebot 4"and c3.att==3:
            p4.order_acceptance=3


    def set_payoffs(self):
        p1=self.get_player_by_role("Producer1")
        p2=self.get_player_by_role("Producer2")
        p3= self.get_player_by_role("Producer3")
        p4= self.get_player_by_role("Producer4")
        c1= self.get_player_by_role("Consumer1")
        c2 = self.get_player_by_role("Consumer2")
        c3 = self.get_player_by_role("Consumer3")

        if p1.got_accepted==True:
            p1.payoff= Constants.endowment + p1.offer_price - Constants.cost_production*p1.product_type
        if p1.got_accepted!=True:
            p1.payoff= Constants.endowment
        if p2.got_accepted==True:
            p2.payoff= Constants.endowment + p2.offer_price - Constants.cost_production*p2.product_type
        if p2.got_accepted!=True:
            p2.payoff= Constants.endowment
        if p3.got_accepted==True:
            p3.payoff= Constants.endowment + p3.offer_price - Constants.cost_production*p3.product_type
        if p3.got_accepted!=True:
            p3.payoff= Constants.endowment
        if p4.got_accepted==True:
            p4.payoff= Constants.endowment + p4.offer_price - Constants.cost_production*p4.product_type
        if p4.got_accepted!=True:
            p4.payoff= Constants.endowment
        if c1.accept=="Annahme Angebot 1":
            c1.payoff= Constants.endowment - p1.offer_price + Constants.value_product
            c1.tp_payoff = Constants.endowment - Constants.loss_dirty_product*(1 - p1.product_type)
        if c1.accept=="Annahme Angebot 2":
            c1.payoff= Constants.endowment - p2.offer_price + Constants.value_product
            c1.tp_payoff= Constants.endowment - Constants.loss_dirty_product*(1 - p2.product_type)
        if c1.accept=="Annahme Angebot 3":
            c1.payoff= Constants.endowment - p3.offer_price + Constants.value_product
            c1.tp_payoff= Constants.endowment - Constants.loss_dirty_product*(1 - p3.product_type)
        if c1.accept=="Annahme Angebot 4":
            c1.payoff= Constants.endowment - p4.offer_price + Constants.value_product
            c1.tp_payoff= Constants.endowment - Constants.loss_dirty_product*(1 - p4.product_type)
        if c1.accept=="Keine Angebotsannahme":
            c1.payoff= Constants.endowment
            c1.tp_payoff= Constants.endowment

        if c2.accept=="Annahme Angebot 1":
            c2.payoff= Constants.endowment - p1.offer_price + Constants.value_product
            c2.tp_payoff= Constants.endowment - Constants.loss_dirty_product*(1 - p1.product_type)
        if c2.accept=="Annahme Angebot 2":
            c2.payoff= Constants.endowment - p2.offer_price + Constants.value_product
            c2.tp_payoff = Constants.endowment - Constants.loss_dirty_product * (1 - p2.product_type)
        if c2.accept=="Annahme Angebot 3":
            c2.payoff= Constants.endowment - p3.offer_price + Constants.value_product
            c2.tp_payoff = Constants.endowment - Constants.loss_dirty_product * (1 - p3.product_type)
        if c2.accept=="Annahme Angebot 4":
            c2.payoff= Constants.endowment - p4.offer_price + Constants.value_product
            c2.tp_payoff = Constants.endowment - Constants.loss_dirty_product * (1 - p4.product_type)
        if c2.accept=="Keine Angebotsannahme":
            c2.payoff= Constants.endowment
            c2.tp_payoff= Constants.endowment

        if c3.accept=="Annahme Angebot 1":
            c3.payoff= Constants.endowment - p1.offer_price + Constants.value_product
            c3.tp_payoff = Constants.endowment - Constants.loss_dirty_product * (1 - p1.product_type)
        if c3.accept=="Annahme Angebot 2":
            c3.payoff= Constants.endowment - p2.offer_price + Constants.value_product
            c3.tp_payoff = Constants.endowment - Constants.loss_dirty_product * (1 - p2.product_type)
        if c3.accept=="Annahme Angebot 3":
            c3.payoff= Constants.endowment - p3.offer_price + Constants.value_product
            c3.tp_payoff = Constants.endowment - Constants.loss_dirty_product * (1 - p3.product_type)
        if c3.accept=="Annahme Angebot 4":
            c3.payoff= Constants.endowment - p4.offer_price + Constants.value_product
            c3.tp_payoff = Constants.endowment - Constants.loss_dirty_product * (1 - p4.product_type)
        if c3.accept=="Keine Angebotsannahme":
            c3.payoff= Constants.endowment
            c3.tp_payoff= Constants.endowment




    pass



class Player(BasePlayer):
#Corporate Social Responsibility
    final_payoff = models.IntegerField()
    product_type = models.BooleanField(choices=[(False, 'Produkt mit Verlust für Teilnehmer C'), (True, 'Produkt ohne Auswirkungen auf Teilnehmer C')], widget=widgets.RadioSelect())
    offer_price = models.CurrencyField(min=0, max=Constants.endowment)
    accept = models.CharField(choices=['Annahme Angebot 1', 'Annahme Angebot 2', 'Annahme Angebot 3', 'Annahme Angebot 4', 'Keine Angebotsannahme'])
    got_accepted = models.BooleanField(choices=[(False, 'Angebot wurde nicht angenommen'), (True, 'Angebot wurde angenommen')])
    att = models.IntegerField()
    order = models.IntegerField() # Variable, um Third Persons zu Konsumenten zuzuordnen
    order_acceptance = models.IntegerField()
    tp_payoff = models.IntegerField()
    def role(self):
        if self.id_in_group == 1:
            return 'Producer1'
        if self.id_in_group == 2:
            return 'Producer2'
        if self.id_in_group == 3:
            return 'Producer3'
        if self.id_in_group == 4:
            return 'Producer4'
        if self.id_in_group == 5:
            return 'Consumer1'
        if self.id_in_group == 6:
            return 'Consumer2'
        if self.id_in_group == 7:
            return 'Consumer3'


#Responsibility Assigning Game
    person_A_type = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_B_type = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_C_type = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_A_price = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_B_price = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)
    person_C_price = models.CharField(choices=('Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich', 'Sehr verantwortlich'), widget=widgets.RadioSelectHorizontal)

#Questionnaire
    good_person = models.CharField(choices=('Not very good', 'not good', 'neither good nor bad', 'good', 'very good'),
                                   widget=widgets.RadioSelectHorizontal())
    social_person = models.CharField(choices=(
    'Sehr sozial unangenmessen', 'Eher sozial unangemessen', 'Eher sozial angemssen', 'Sehr sozial angemessen'),
                                     widget=widgets.RadioSelectHorizontal())
    effect_participants = models.CharField(choices=('Gar nicht', 'Eher nicht', 'Ein bisschen', 'Sehr'),
                                           widget=widgets.RadioSelectHorizontal())
    sex = models.CharField(choices=('Männlich', 'Weiblich', 'Anders'), widget=widgets.RadioSelectHorizontal())
    age = models.IntegerField(choices=range(1, 100))
    semester = models.IntegerField(choices=range(1, 25))
    study_subject = models.CharField(choices=(
    'Betriebswirtschaftslehre', 'Volkswirtschaftslehre', 'Biologie', 'Chemie', 'Ingenieurwissenschaften', 'Philosophie',
    'Psychologie', 'Physik', 'Jura', 'Geschichte', 'Anglistik/Amerikanistik', 'Archäologie', 'Germanistik', 'Biochemie',
    'Bioinformatik', 'Ernährungswissenschaften', 'Erziehungswissenschaften', 'Theologie', 'Geographie', 'Romanistik',
    'Geologie', 'Philologie(lateinisch/griechisch)', 'Informatik', 'Wirtschaftsinformatik', 'Indogermanistik',
    'Kunstgeschichte', 'Mathematik', 'Medienwissenschaft', 'Musikwissenschaft', 'Slawistik', 'Pharmazie',
    'Politikwissenschaft', 'Soziologie', 'Sportwissenschaft', 'Ur- und Frühgeschichte', 'Zahnmedizin', 'Medizintechnick',
    'Anthropologie', 'Sonstiges', 'Wirtschaftswissenschaften', 'Humanmedizin', 'Wirtschaftspädagogik'))
    comment = models.TextField(null=True, blank=True)