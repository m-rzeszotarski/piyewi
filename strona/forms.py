from django import forms
from .models import Kawa, Yerba, Piwo, Wino

class YerbaForm(forms.ModelForm):

    class Meta:
        model = Yerba
        fields = ('autor', 'firma', 'nazwa', 'zapylenie', 'aromat', 'moc', 'goryczka', 'nuty_owocowe', 'trwałość', 'ocena', 'uwagi',)
        labels = {
            'autor' : "Twój nick",
        }

class PiwoForm(forms.ModelForm):

    class Meta:
        model = Piwo
        fields = ('autor', 'firma', 'nazwa', 'typ', 'aromat', 'moc', 'goryczka', 'nuty_owocowe', 'piana', 'kolor', 'mętność', 'zgazowanie', 'ocena', 'uwagi',)
        labels = {
            'autor' : "Twój nick",
        }

class WinoForm(forms.ModelForm):

    class Meta:
        model = Wino
        fields = ('autor', 'firma', 'nazwa', 'typ', 'kolor', 'klarowność', 'musowanie', 'aromat', 'moc', 'nuty_owocowe', 'ocena', 'uwagi')
        labels = {
            'autor' : "Twój nick",
        }

class KawaForm(forms.ModelForm):

    class Meta:
        model = Kawa
        fields = ('autor', 'firma', 'nazwa', 'arabica', 'stopień_palenia', 'kwasowość', 'moc', 'ocena', 'uwagi')
        labels = {
            'arabica' : "Arabica [%]",
            'autor' : "Twój nick",
        }