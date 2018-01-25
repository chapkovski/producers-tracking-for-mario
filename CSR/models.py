from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from django.db.models import Count, Max
from django.db import models as djmodels

author = 'Your name here'

doc = """
Your app description
"""

import random
import itertools


class Constants(BaseConstants):
    name_in_url = 'csr'
    players_per_group = 7
    num_producers = 4
    num_consumers = players_per_group - num_producers
    num_rounds = 1
    endowment = 100
    cost_production = 20
    value_product = 50
    loss_dirty_product = 60
    type_product = ["dirty", "clean"]
    pref_fields = ['person_A_type', 'person_B_type', 'person_C_type'] + ['person_A_price', 'person_B_price',
                                                                         'person_C_price']
    part_payoff1 = 10
    type_price_choices = ['Gar nicht verantwortlich', 'Eher nicht verantwortlich', 'Eher verantwortlich',
                          'Sehr verantwortlich']


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.role_stub, _ = p.get_role_stub()
        if self.round_number == 1:
            self.session.vars['part_payoff'] = random.randint(1, 2)
            self.session.vars['rand_quest'] = random.randint(1, 6)
            paying_round = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_round'] = paying_round

        attribute = list(range(1, Constants.num_consumers + 1))
        random.shuffle(attribute)
        for g in self.get_groups():
            for p in g.producers:
                p.offers.create(group=g)
            for i, c in enumerate(g.consumers):
                c.att = attribute[i]
            


class Group(BaseGroup):

    def _get_subtype(self, subtype):
        return [p for p in self.get_players() if p.role_stub == subtype]

    @property
    def producers(self):
        return self._get_subtype('Producer')

    @property
    def consumers(self):
        return self._get_subtype('Consumer')

    def get_available_offers(self):
        transactions = self.transactions.filter(consumer=None)
        return transactions

    def get_consumer_choices(self):
        available_slots = [(p.producer.id_in_group, 'Annahme Angebot {}'.format(p.producer.id_in_group)) for p in
                           self.get_available_offers()]
        no_choice = (None, 'Keine Angebotsannahme')
        available_slots.append(no_choice)
        return available_slots

    def alt_final_payoff(self):
        field_id = Constants.pref_fields[self.session.vars['rand_quest'] - 1]
        ps = self.player_set.all().values(field_id).annotate(pref=Count(field_id))
        most_pop = max(ps, key=lambda p: p['pref'])
        winning_choice = most_pop[field_id]
        self.player_set.filter(**{field_id: winning_choice}).update(final_payoff=Constants.part_payoff1)

    def final_payoff(self):
        if self.session.vars['part_payoff'] == 1:
            self.alt_final_payoff()
        if self.session.vars['part_payoff'] == 2:
            pay_round = self.session.vars['paying_round']
            for p in self.get_players():
                p.final_payoff = p.in_round(pay_round).payoff

    def got_accepted(self):

        for p in self.producers:
            current_transaction = p.offers.all()[0]
            if current_transaction.consumer is not None:
                p.got_accepted = True
                p.order_acceptance = current_transaction.consumer.att

    def set_payoffs(self):
        for p in self.producers:
            p.payoff = (
                Constants.endowment + (p.offer_price - Constants.cost_production * p.product_type) * (
                    p.got_accepted or 0))

        for c in self.consumers:
            if c.accept not in (None, 'None'):
                p = c.markettransaction.producer
                c.payoff = Constants.endowment - p.offer_price + Constants.value_product
                c.tp_payoff = Constants.endowment - Constants.loss_dirty_product * (1 - p.product_type)
            else:
                c.payoff = Constants.endowment
                c.tp_payoff = Constants.endowment


class Player(BasePlayer):
    def get_role_stub(self):
        if self.id_in_group <= Constants.num_producers:
            initial_name = 'Producer'
            id = self.id_in_group
        else:
            initial_name = 'Consumer'
            id = self.id_in_group - Constants.num_producers
        return (initial_name, id)

    def role(self):
        a, b = self.get_role_stub()
        return '{}{}'.format(a, b)

    # Corporate Social Responsibility
    role_stub = models.CharField()
    final_payoff = models.IntegerField()
    product_type = models.BooleanField(
        choices=[(False, 'Produkt mit Verlust für Teilnehmer C'), (True, 'Produkt ohne Auswirkungen auf Teilnehmer C')],
        widget=widgets.RadioSelect())
    offer_price = models.CurrencyField(min=0, max=Constants.endowment)
    accept = models.CharField(blank=True)
    got_accepted = models.BooleanField(
        choices=[(False, 'Angebot wurde nicht angenommen'), (True, 'Angebot wurde angenommen')])
    att = models.IntegerField()
    order = models.IntegerField()  # Variable, um Third Persons zu Konsumenten zuzuordnen
    order_acceptance = models.IntegerField()
    tp_payoff = models.IntegerField()

    # Responsibility Assigning Game

    person_A_type = models.CharField(choices=Constants.type_price_choices, widget=widgets.RadioSelectHorizontal)
    person_B_type = models.CharField(choices=Constants.type_price_choices, widget=widgets.RadioSelectHorizontal)
    person_C_type = models.CharField(choices=Constants.type_price_choices, widget=widgets.RadioSelectHorizontal)
    person_A_price = models.CharField(choices=Constants.type_price_choices, widget=widgets.RadioSelectHorizontal)
    person_B_price = models.CharField(choices=Constants.type_price_choices, widget=widgets.RadioSelectHorizontal)
    person_C_price = models.CharField(choices=Constants.type_price_choices, widget=widgets.RadioSelectHorizontal)

    # Questionnaire
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
        'Betriebswirtschaftslehre', 'Volkswirtschaftslehre', 'Biologie', 'Chemie', 'Ingenieurwissenschaften',
        'Philosophie',
        'Psychologie', 'Physik', 'Jura', 'Geschichte', 'Anglistik/Amerikanistik', 'Archäologie', 'Germanistik',
        'Biochemie',
        'Bioinformatik', 'Ernährungswissenschaften', 'Erziehungswissenschaften', 'Theologie', 'Geographie',
        'Romanistik',
        'Geologie', 'Philologie(lateinisch/griechisch)', 'Informatik', 'Wirtschaftsinformatik', 'Indogermanistik',
        'Kunstgeschichte', 'Mathematik', 'Medienwissenschaft', 'Musikwissenschaft', 'Slawistik', 'Pharmazie',
        'Politikwissenschaft', 'Soziologie', 'Sportwissenschaft', 'Ur- und Frühgeschichte', 'Zahnmedizin',
        'Medizintechnick',
        'Anthropologie', 'Sonstiges', 'Wirtschaftswissenschaften', 'Humanmedizin', 'Wirtschaftspädagogik'))
    comment = models.TextField(null=True, blank=True)
    from radiogrid import RadioGridField
    ROWS = ((1, 'Guilt'), (2, "Remorse"), (3, "Regret"))
    VALUES = ((1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5"), (6, "6"), (7, "7"))
    three = RadioGridField(rows=ROWS, values=VALUES, require_all_fields=True,toprow=['Überhaupt nicht','Voll und ganz'])


class MarketTransaction(djmodels.Model):
    group = djmodels.ForeignKey(Group, related_name='transactions')
    producer = djmodels.ForeignKey(Player, related_name='offers')
    consumer = djmodels.OneToOneField(Player, null=True)
