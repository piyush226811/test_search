from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey('Country', related_name='country')

    def __unicode__(self):
        return 'Player - ' + str(self.name)


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return 'Country - ' + str(self.name)

class Blog(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return 'Blog - ' + str(self.title)
