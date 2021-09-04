from django import forms
from .models import Yerba, Piwo

class YerbaForm(forms.ModelForm):

    class Meta:
        model = Yerba
        fields = ('firma', 'nazwa', 'zapylenie', 'aromat', 'moc', 'goryczka', 'nuty_owocowe', 'ocena', 'uwagi',)

class PiwoForm(forms.ModelForm):

    class Meta:
        model = Piwo
        fields = ('firma', 'nazwa', 'typ', 'aromat', 'smak', 'moc', 'goryczka', 'nuty_owocowe', 'piana', 'kolor', 'mętność', 'zgazowanie', 'ocena', 'uwagi',)