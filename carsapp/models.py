from django.db import models
from django.utils.translation import gettext_lazy as _

class Car(models.Model):

    ENGINE_BENZIN = 'b'
    ENGINE_DIESEL = 'd'

    ENGINE_CHOICES = [
        (ENGINE_BENZIN, _('Benzin')),
        (ENGINE_DIESEL, _('Diesel')),
    ]

    title = models.CharField(max_length=140)
    link = models.URLField(verbose_name="Advertisement Link")
    company = models.CharField(max_length=140)
    year = models.IntegerField()
    engine_type = models.CharField(max_length=1, choices=ENGINE_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title', )
       # unique_together = (('title','company'))

