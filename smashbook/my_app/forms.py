from django import forms
from .models import Match

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date', 'score', 'result']
        widgets = {
                  'date': forms.DateInput(
                      format=('%Y-%m-%d'),
                      attrs={
                          'placeholder': 'Select a date',
                          'type': 'date'
                      }
                  ),
              }