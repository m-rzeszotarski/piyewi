from django import forms
from .models import Yerba

class YerbaForm(forms.ModelForm):

    class Meta:
        model = Yerba
        fields = ('firma', 'nazwa', 'zapylenie', 'aromat', 'moc', 'goryczka', 'nuty_owocowe', 'ocena', 'uwagi',)