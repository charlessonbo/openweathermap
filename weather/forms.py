from django import forms
 
 
class WeatherForm(forms.Form):
    location = forms.CharField(widget=forms.TextInput(attrs={'maxlength':100}))