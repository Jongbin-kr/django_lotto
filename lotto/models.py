from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    ## id열은 자동으로 생성된다!
    name = models.CharField(max_length=24)
    text = models.CharField(max_length=225)
    lottos = models.CharField(max_length=255, default='[1,2,3,4,5,6]')
    num_lotto = models.IntegerField(default=5)
    update_date = models.DateTimeField()
    
    def generate(self):
        self.lottos = ""
        origin = list(range(1, 46))
        for _ in range(0, self.num_lotto):
            random.shuffle(origin)
            guess = origin[:6]
            guess.sort()
            self.lottos += str(guess) + '\n'
    
        self.update_date = timezone.now()
        self.save()
            
        
    def __str__(self):
        return f"pk {self.pk} : {self.name} - {self.text}"