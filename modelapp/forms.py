from django import forms

class Musician(forms.Form):
    first_name = forms.CharField() 
    last_name = forms.CharField()
    instrument =  forms.CharField()