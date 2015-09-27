import logging

from django.db import models

from .constants import JOBS


class Character(models.Model):
    name = models.CharField(max_length=100)
    lodestone_id = models.CharField(max_length=100, default='')
    server = models.CharField(max_length=100, default='')
    species = models.CharField(max_length=100, default='')
    city_state = models.CharField(max_length=100, default='')
    free_company = models.CharField(max_length=100, default='')
    grand_company_name = models.CharField(max_length=100, default='')
    grand_company_rank = models.CharField(max_length=100, default='')

    lvl_archer = models.IntegerField(default=0)
    lvl_lancer = models.IntegerField(default=0)
    lvl_marauder = models.IntegerField(default=0)
    lvl_pugilist = models.IntegerField(default=0)
    lvl_rogue = models.IntegerField(default=0)
    lvl_arcanist = models.IntegerField(default=0)
    lvl_conjurer = models.IntegerField(default=0)
    lvl_thaumaturge = models.IntegerField(default=0)
    lvl_astrologian = models.IntegerField(default=0)
    lvl_darknight = models.IntegerField(default=0)
    lvl_machinist = models.IntegerField(default=0)
    lvl_alchemist = models.IntegerField(default=0)
    lvl_armorer = models.IntegerField(default=0)
    lvl_blacksmith = models.IntegerField(default=0)
    lvl_carpenter = models.IntegerField(default=0)
    lvl_culinarian = models.IntegerField(default=0)
    lvl_gladiator = models.IntegerField(default=0)
    lvl_goldsmith = models.IntegerField(default=0)
    lvl_leatherworker = models.IntegerField(default=0)
    lvl_weaver = models.IntegerField(default=0)
    lvl_botanist = models.IntegerField(default=0)
    lvl_fisher = models.IntegerField(default=0)
    lvl_miner = models.IntegerField(default=0)

    def as_dict(self):

        jobs = list(map(lambda x: x.as_dict(), list(self.job_set.all()))) if len(self.job_set.all()) > 0 else []

        return {
            'name': self.name,
            'lodestone_id': self.lodestone_id,
            'server': self.server,
            'species': self.species,
            'city_state': self.city_state,
            'free_company': self.free_company,
            'grand_company': {
                'name': self.grand_company_name,
                'rank': self.grand_company_rank
            },
            'jobs': jobs,
            'classes': {
                "armorer": {
                    "level": self.lvl_armorer
                },
                "alchemist": {
                    "level": self.lvl_alchemist
                },
                "leatherworker": {
                    "level": self.lvl_leatherworker
                },
                "pugilist": {
                    "level": self.lvl_pugilist
                },
                "carpenter": {
                    "level": self.lvl_carpenter
                },
                "culinarian": {
                    "level": self.lvl_culinarian
                },
                "arcanist": {
                    "level": self.lvl_arcanist
                },
                "fisher": {
                    "level": self.lvl_fisher
                },
                "machinist": {
                    "level": self.lvl_machinist
                },
                "conjurer": {
                    "level": self.lvl_conjurer
                },
                "blacksmith": {
                    "level": self.lvl_blacksmith
                },
                "astrologian": {
                    "level": self.lvl_astrologian
                },
                "thaumaturge": {
                    "level": self.lvl_thaumaturge
                },
                "gladiator": {
                    "level": self.lvl_gladiator
                },
                "miner": {
                    "level": self.lvl_miner
                },
                "lancer": {
                    "level": self.lvl_lancer
                },
                "rogue": {
                    "level": self.lvl_rogue
                },
                "marauder": {
                    "level": self.lvl_marauder
                },
                "botanist": {
                    "level": self.lvl_botanist
                },
                "weaver": {
                    "level": self.lvl_weaver
                },
                "archer": {
                    "level": self.lvl_archer
                },
                "darknight": {
                    "level": self.lvl_darknight
                },
                "goldsmith": {
                    "level": self.lvl_goldsmith
                }
            }
        }


class Item(models.Model):
    lodestone_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

    def as_dict(self):
        return {
            'lodestone_id': self.lodestone_id,
            'name': self.name
        }


class Job(models.Model):
    character = models.ForeignKey(Character)
    job = models.CharField(max_length=25)
    items = models.ManyToManyField(Item)

    @property
    def level(self):
        if self.job == JOBS.MARAUDER.name:
            return self.character.lvl_marauder
        elif self.job == JOBS.GLADIATOR.name:
            return self.character.lvl_gladiator
        elif self.job == JOBS.PUGILIST.name:
            return self.character.lvl_pugilist
        elif self.job == JOBS.LANCER.name:
            return self.character.lvl_lancer
        elif self.job == JOBS.ARCHER.name:
            return self.character.lvl_archer
        elif self.job == JOBS.ROGUE.name:
            return self.character.lvl_rogue
        elif self.job == JOBS.CONJURER.name:
            return self.character.lvl_conjurer
        elif self.job == JOBS.THAUMATURGE.name:
            return self.character.lvl_thaumaturge
        elif self.job == JOBS.ARCANIST.name:
            return self.character.lvl_arcanist

        elif self.job == JOBS.CARPENTER.name:
            return self.character.lvl_carpenter
        elif self.job == JOBS.BLACKSMITH.name:
            return self.character.lvl_blacksmith
        elif self.job == JOBS.ARMORER.name:
            return self.character.lvl_armorer
        elif self.job == JOBS.GOLDSMITH.name:
            return self.character.lvl_goldsmith
        elif self.job == JOBS.LEATHERWORKER.name:
            return self.character.lvl_leatherworker
        elif self.job == JOBS.WEAVER.name:
            return self.character.lvl_weaver
        elif self.job == JOBS.ALCHEMIST.name:
            return self.character.lvl_alchemist
        elif self.job == JOBS.CULINARIAN.name:
            return self.character.lvl_culinarian
        elif self.job == JOBS.BOTANIST.name:
            return self.character.lvl_botanist
        elif self.job == JOBS.FISHER.name:
            return self.character.lvl_fisher
        elif self.job == JOBS.MINER.name:
            return self.character.lvl_miner

        elif self.job == JOBS.WARRIOR.name:
            return self.character.lvl_marauder
        elif self.job == JOBS.PALADIN.name:
            return self.character.lvl_gladiator
        elif self.job == JOBS.MONK.name:
            return self.character.lvl_pugilist
        elif self.job == JOBS.DRAGOON.name:
            return self.character.lvl_lancer
        elif self.job == JOBS.BARD.name:
            return self.character.lvl_archer
        elif self.job == JOBS.WHITEMAGE.name:
            return self.character.lvl_conjurer
        elif self.job == JOBS.BLACKMAGE.name:
            return self.character.lvl_thaumaturge
        elif self.job == JOBS.SUMMONER.name:
            return self.character.lvl_arcanist
        elif self.job == JOBS.SCHOLAR.name:
            return self.character.lvl_arcanist
        elif self.job == JOBS.NINJA.name:
            return self.character.lvl_rogue

        elif self.job == JOBS.DARKNIGHT.name:
            return self.character.lvl_darknight
        elif self.job == JOBS.ASTROLOGIAN.name:
            return self.character.lvl_astrologian
        elif self.job == JOBS.MACHINIST.name:
            return self.character.lvl_machinist

        else:
            logging.error('Job instance is malformed: job = %s', self.job)
            return 0

    def as_dict(self):
        items = list(map(lambda x: x.as_dict(), list(self.items.all()))) if len(self.items.all()) > 0 else []

        return {
            'job': JOBS[self.job].value,
            'level': self.level,
            'items': items
        }
