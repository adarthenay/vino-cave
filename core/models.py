# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

WINE_COLOR_CHOICES = (
    ('RO', _("Rouge")),
    ('BL', _("Blanc")),
    ('RO', _("Rosé")),
    ('JA', _("Jaune")),
    ('NC', _("Non précisé")),
    ('LI', _("Vin liquoreux")),
)

class Vin(models.Model):
    appellation = models.CharField(_("appellation"), max_length=255, blank=True,
        help_text=_("L'appellation du vin"))
    area = models.CharField(blank=True, max_length=255,
        help_text=_("La région du vin"))
    cuvee = models.CharField(blank=True, max_length=255, help_text=_("La cuvée associée au vin"))
    name = models.CharField(blank=True, max_length=255, help_text=_("Le nom du vin"))
    wine_color = models.CharField(choices=WINE_COLOR_CHOICES, max_length=255, help_text=_("La couleur du vin"))
    year = models.PositiveSmallIntegerField(blank=True, null=True, help_text=_("Le millésime du vin"))
    
    def __unicode__(self):
        return self.appellation+" "+str(self.year)
        
class Bouteille(models.Model):
    prix = models.DecimalField(_("prix"), max_digits=6, decimal_places=2, blank=True,
        help_text=_("Prix unitaire"))
    contenance = models.DecimalField(_("contenance"), max_digits=4, decimal_places=1, blank=True,
        help_text=_("contenance"))
    provenance = models.CharField(_("provenance"), max_length=255, blank=True,
        help_text=_("provenance de la bouteille"))
    #etiquette = models.ImageField()
    vin = models.ForeignKey("Vin")
    