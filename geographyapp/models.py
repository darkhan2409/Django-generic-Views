from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(help_text='Enter an interesting fact about the country')
    capital = models.CharField(max_length=50)
    population = models.FloatField()
    square = models.FloatField()

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
