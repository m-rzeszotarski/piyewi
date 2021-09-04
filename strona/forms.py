from django import forms
from .models import Kawa, Yerba, Piwo, Wino

class YerbaForm(forms.ModelForm):

    class Meta:
        model = Yerba
        fields = ('firma', 'nazwa', 'zapylenie', 'aromat', 'moc', 'goryczka', 'nuty_owocowe', 'ocena', 'uwagi',)

class PiwoForm(forms.ModelForm):

    class Meta:
        model = Piwo
        fields = ('firma', 'nazwa', 'typ', 'aromat', 'smak', 'moc', 'goryczka', 'nuty_owocowe', 'piana', 'kolor', 'mętność', 'zgazowanie', 'ocena', 'uwagi',)
    
class WinoForm(forms.ModelForm):

    class Meta:
        model = Wino
        fields = ('firma', 'nazwa', 'typ', 'kolor', 'klarowność', 'musowanie', 'aromat', 'moc', 'nuty_owocowe', 'ocena', 'uwagi')

class KawaForm(forms.ModelForm):

    class Meta:
        model = Kawa
        fields = ('firma', 'nazwa', 'arabica', 'robusta', 'stopień_palenia', 'kwasowość', 'moc', 'ocena', 'uwagi')