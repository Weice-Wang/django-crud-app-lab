from django.db import models
from django.urls import reverse

class Player(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unisex', 'Unisex')
    ]

    PLAYSTYLE_CHOICES = [
        ('baseline', 'Baseline Player'),
        ('all_court', 'All-Court Player'),
        ('serve_volley', 'Serve and Volley'),
        ('counterpuncher', 'Counterpuncher'),
        ('aggressive', 'Aggressive Baseliner'),
    ]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    racquet = models.CharField(max_length=100, blank=True)
    play_style = models.CharField(max_length=30, choices=PLAYSTYLE_CHOICES)  # ⭐ choices here
    strength = models.CharField(max_length=200, blank=True)
    weakness = models.CharField(max_length=200, blank=True)
    utr_rating = models.FloatField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('player-detail', kwargs={'player_id': self.id})
    

class Match(models.Model):
    date = models.DateField()
    score = models.CharField(max_length=50)
    result = models.CharField(
        max_length=10,
        choices=[('win', 'Win'),('loss', 'Loss')])
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
       return f"You vs {self.player.name} - {self.result} on {self.date}"
    
    class Meta:
        ordering = ['-date']