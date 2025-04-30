from django.db import models

class terminalForm(models.Model):
    terminal_input = models.CharField(max_length=100, blank= True)
    def __str__(self):
        return self.terminal_input



# Create your models here.
