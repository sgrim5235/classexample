from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()

    def __str__(self):
        return '{} - {}'.format(self.name, self.age)

class Skills(models.Model):
    name=models.CharField(max_length=40)

    class Meta:
        verbose_name_plural='skill'

    def __str__(self):
        return '{}'.format(self.name)

class Talents(models.Model):
    person=models.ForeignKey(Person)
    skill=models.ForeignKey(Skills)
    obtained=models.DateField()

    class Meta:
        verbose_name_plural='Talents'

    def __str__(self):
        return '{} obtained {} on {}'.format(self.person.name,
                                             self.skill.name,
                                             self.obainted)