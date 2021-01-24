from django import forms

class NameForm(forms.Form):
    Player_Name = forms.CharField(label='Player_Name', max_length=100)