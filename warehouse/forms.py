from django import forms
from .models import Operation, Plant

class BudgetForm(forms.Form):
    month = forms.CharField(label="month")
    Plant = forms.ModelChoiceField(queryset=Plant.objects.all(), label="Plant")
    Operation = forms.ModelChoiceField(queryset=Operation.objects.all(), label="Operation")
    value = forms.IntegerField(label="value")

    def process(self):
        cd = self.cleaned_data
