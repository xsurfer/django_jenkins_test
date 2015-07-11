from django.db import models

class Animal(models.Model):
    animal = models.CharField(max_length=20, null=False, blank=False, default="Animal")
    salutation = models.CharField(max_length=20, null=False, blank=False, default="NoSalutation")

    def speak(self):
        return 'The %s says "%s"' % (self.animal, self.salutation)
