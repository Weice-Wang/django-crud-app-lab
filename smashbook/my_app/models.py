from django.db import models

class Player(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
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