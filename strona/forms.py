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
        fields = (
            'autor',
            'firma',
            'nazwa',
            'typ',
            'kolor',
            'klarowność',
            'musowanie',
            'aromat',
            'moc',
            'nuty_zielonych_owoców',
            'nuty_czerwonych_owoców',
            'nuty_czarnych_owoców',
            'nuty_cytrusowe',
            'nuty_tropikalne',
            'nuty_pestkowców',
            'nuty_suszonych_owoców',
            'nuty_roślinne',
            'nuty_kwiatowe',
            'nuty_drożdżowe',
            'nuty_dojrzewające',
            'nuty_maślane',
            'nuty_dębowe',
            'nuty_ziemne',
            'nuty_minerałów',
            'ocena',
            'uwagi'
            )
        labels = {
            'autor' : "Twój nick",
            'aromat' : "Aromat (intensywność)",
            'kolor' : "Kolor (jak bardzo ciemne)",
            'nuty_zielonych_owoców' : "Czy wyczuwasz nuty zielonych owoców? (np. jabłko, gruszka, agrest)",
            'nuty_czerwonych_owoców' : "Czy wyczuwasz nuty czerwonych owoców? (np. truskawka, wiśnia, malina, granat)",
            'nuty_czarnych_owoców' : "Czy wyczuwasz nuty czarnych owoców? (np. czarna porzeczka, czarna wisnia, jeżyna",
            'nuty_cytrusowe' : "Czy wyczuwasz nuty cytrusowe? (np. cytryna, limonka, grejpfrut, pomarańcz)",
            'nuty_tropikalne' : "Czy wyczuwasz nuty owoców tropikalnych? (np. ananas, papaja, marakuja)",
            'nuty_pestkowców' : "Czy wyczuwasz nuty pestkowców? (np. śliwka, morela, brzoskwinia)",
            'nuty_suszonych_owoców' : "Czy wyczuwasz nuty suszonych owoców?",
            'nuty_roślinne' : "Czy wyczuwasz nuty roślinne? (np. zielona papryka, szparagi, świeżo skoszona trawa lub zioła takie jak rozmaryn, szałwia i tymianek)",
            'nuty_kwiatowe' : "Czy wyczuwasz nuty kwiatowe? (np. kwiaty, perfumy)",
            'nuty_drożdżowe' : "Czy wyczuwasz nuty drożdżowe? (np. ser, drożdże, banany)",
            'nuty_dojrzewające' : "Czy wyczuwasz nuty dojrzewające? (np. migdały, chleb, tost)",
            'nuty_dębowe' : "Czy wyczuwasz nuty dębowe/ przypraw? (np. pieprz, cynamon, goździk, gałka muszkatałowa, czekolada, wanilia, dąb, tytoń, dym)",
            'nuty_maślane' : "Czy wyczuwasz nuty maślane? (np. mleko, masło)",
            'nuty_ziemne' : "Czy wyczuwasz nuty ziemne? (np. ziemia, ściółka leśna, grzyby, trufle, skóra)",
            'nuty_minerałów' : "Czy wyczuwasz nuty mineralne? (np. sól, kamień)",
        }

class KawaForm(forms.ModelForm):

    class Meta:
        model = Kawa
        fields = ('autor', 'firma', 'nazwa', 'arabica', 'stopień_palenia', 'kwasowość', 'moc',  'ocena', 'uwagi')
        labels = {
            'arabica' : "Arabica [%]",
            'autor' : "Twój nick",
        }