from django.db import models

class Animal(models.Model):
    animal = None
    salutation = None

    def speak(self):
        return "The %s says \"%s\"" % (self.animal, self.salutation)
