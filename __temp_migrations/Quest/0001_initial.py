# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-22 12:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Quest_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('good_person', otree.db.models.StringField(choices=[('Not very good', 'Not very good'), ('not good', 'not good'), ('neither good nor bad', 'neither good nor bad'), ('good', 'good'), ('very good', 'very good')], max_length=10000, null=True)),
                ('social_person', otree.db.models.StringField(choices=[('Sehr sozial unangenmessen', 'Sehr sozial unangenmessen'), ('Eher sozial unangemessen', 'Eher sozial unangemessen'), ('Eher sozial angemssen', 'Eher sozial angemssen'), ('Sehr sozial angemessen', 'Sehr sozial angemessen')], max_length=10000, null=True)),
                ('effect_participants', otree.db.models.StringField(choices=[('Gar nicht', 'Gar nicht'), ('Eher nicht', 'Eher nicht'), ('Ein bisschen', 'Ein bisschen'), ('Sehr', 'Sehr')], max_length=10000, null=True)),
                ('sex', otree.db.models.StringField(choices=[('Männlich', 'Männlich'), ('Weiblich', 'Weiblich'), ('Anders', 'Anders')], max_length=10000, null=True)),
                ('age', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60), (61, 61), (62, 62), (63, 63), (64, 64), (65, 65), (66, 66), (67, 67), (68, 68), (69, 69), (70, 70), (71, 71), (72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78), (79, 79), (80, 80), (81, 81), (82, 82), (83, 83), (84, 84), (85, 85), (86, 86), (87, 87), (88, 88), (89, 89), (90, 90), (91, 91), (92, 92), (93, 93), (94, 94), (95, 95), (96, 96), (97, 97), (98, 98), (99, 99)], null=True)),
                ('semester', otree.db.models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24)], null=True)),
                ('study_subject', otree.db.models.StringField(choices=[('Betriebswirtschaftslehre', 'Betriebswirtschaftslehre'), ('Volkswirtschaftslehre', 'Volkswirtschaftslehre'), ('Biologie', 'Biologie'), ('Chemie', 'Chemie'), ('Ingenieurwissenschaften', 'Ingenieurwissenschaften'), ('Philosophie', 'Philosophie'), ('Psychologie', 'Psychologie'), ('Physik', 'Physik'), ('Jura', 'Jura'), ('Geschichte', 'Geschichte'), ('Anglistik/Amerikanistik', 'Anglistik/Amerikanistik'), ('Archäologie', 'Archäologie'), ('Germanistik', 'Germanistik'), ('Biochemie', 'Biochemie'), ('Bioinformatik', 'Bioinformatik'), ('Ernährungswissenschaften', 'Ernährungswissenschaften'), ('Erziehungswissenschaften', 'Erziehungswissenschaften'), ('Theologie', 'Theologie'), ('Geographie', 'Geographie'), ('Romanistik', 'Romanistik'), ('Geologie', 'Geologie'), ('Philologie(lateinisch/griechisch)', 'Philologie(lateinisch/griechisch)'), ('Informatik', 'Informatik'), ('Wirtschaftsinformatik', 'Wirtschaftsinformatik'), ('Indogermanistik', 'Indogermanistik'), ('Kunstgeschichte', 'Kunstgeschichte'), ('Mathematik', 'Mathematik'), ('Medienwissenschaft', 'Medienwissenschaft'), ('Musikwissenschaft', 'Musikwissenschaft'), ('Slawistik', 'Slawistik'), ('Pharmazie', 'Pharmazie'), ('Politikwissenschaft', 'Politikwissenschaft'), ('Soziologie', 'Soziologie'), ('Sportwissenschaft', 'Sportwissenschaft'), ('Ur- und Frühgeschichte', 'Ur- und Frühgeschichte'), ('Zahnmedizin', 'Zahnmedizin'), ('Medizintechnick', 'Medizintechnick'), ('Anthropologie', 'Anthropologie'), ('Sonstiges', 'Sonstiges'), ('Wirtschaftswissenschaften', 'Wirtschaftswissenschaften'), ('Humanmedizin', 'Humanmedizin'), ('Wirtschaftspädagogik', 'Wirtschaftspädagogik')], max_length=10000, null=True)),
                ('comment', otree.db.models.LongStringField(blank=True, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Quest.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_player', to='otree.Session')),
            ],
            options={
                'db_table': 'Quest_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quest_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Quest_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quest.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quest.Subsession'),
        ),
    ]