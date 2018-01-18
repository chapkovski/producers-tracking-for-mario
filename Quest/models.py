from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Quest'
    players_per_group = 10
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    good_person = models.CharField(choices=('Not very good', 'not good', 'neither good nor bad', 'good', 'very good'), widget=widgets.RadioSelectHorizontal())
    social_person = models.CharField(choices=('Sehr sozial unangenmessen', 'Eher sozial unangemessen', 'Eher sozial angemssen', 'Sehr sozial angemessen'), widget=widgets.RadioSelectHorizontal())
    effect_participants = models.CharField(choices=('Gar nicht', 'Eher nicht','Ein bisschen', 'Sehr'), widget= widgets.RadioSelectHorizontal())
    sex= models.CharField(choices=('Männlich','Weiblich', 'Anders'), widget=widgets.RadioSelectHorizontal())
    age = models.IntegerField(choices=range(1, 100))
    semester = models.IntegerField(choices=range(1,25))
    study_subject = models.CharField(choices= ('Betriebswirtschaftslehre', 'Volkswirtschaftslehre', 'Biologie', 'Chemie', 'Ingenieurwissenschaften','Philosophie', 'Psychologie','Physik', 'Jura', 'Geschichte', 'Anglistik/Amerikanistik', 'Archäologie', 'Germanistik', 'Biochemie', 'Bioinformatik', 'Ernährungswissenschaften', 'Erziehungswissenschaften', 'Theologie', 'Geographie', 'Romanistik', 'Geologie', 'Philologie(lateinisch/griechisch)', 'Informatik', 'Wirtschaftsinformatik', 'Indogermanistik', 'Kunstgeschichte', 'Mathematik','Medienwissenschaft', 'Musikwissenschaft', 'Slawistik', 'Pharmazie', 'Politikwissenschaft', 'Soziologie', 'Sportwissenschaft', 'Ur- und Frühgeschichte', 'Zahnmedizin', 'Medizintechnick', 'Anthropologie', 'Sonstiges', 'Wirtschaftswissenschaften', 'Humanmedizin', 'Wirtschaftspädagogik'))
    comment= models.TextField(null=True, blank=True)
    pass
