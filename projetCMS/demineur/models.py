from django.db import models
import random

class Partie(models.Model):
    dateheure_debut = models.DateTimeField(auto_now_add=True)
    dateheure_modification = models.DateTimeField(auto_now=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return f'Partie {self.nom}'

def random_position():
    return random.randint(0, 19)

class Mine(models.Model):
    partie = models.ForeignKey(Partie, related_name='mines',
                               on_delete=models.CASCADE)
    position_x = models.PositiveSmallIntegerField(
        default=random_position,
    )
    position_y = models.PositiveSmallIntegerField(
        default=random_position,
    )
    
    def __str__(self):
        return f'Mine {self.position_x} {self.position_y}'
