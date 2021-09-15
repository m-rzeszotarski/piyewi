from django import forms
from .models import Kawa, Yerba, Piwo, Wino
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

class YerbaForm(forms.ModelForm):

    class Meta:
        model = Yerba
        fields = ('autor', 'firma', 'nazwa', 'zapylenie', 'aromat', 'moc', 'goryczka', 'nuty_owocowe', 'trwałość', 'ocena', 'uwagi',)
        labels = {
            'autor' : "Twój nick",
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('autor', css_class="form50"), 
            Field('firma', css_class="form50"), 
            Field('nazwa', css_class="form50"), 
            Field('zapylenie', css_class="form10"), 
            Field('aromat', css_class="form10"), 
            Field('moc', css_class="form10"), 
            Field('goryczka', css_class="form10"),  
            Field('nuty_owocowe', css_class="form10"), 
            Field('trwałość', css_class="form10"), 
            Field('ocena'),
            Field('uwagi'),
            
        )
        self.helper.add_input(Submit('submit', 'Zapisz'))

class PiwoForm(forms.ModelForm):

    class Meta:
        model = Piwo
        fields = ('autor', 'firma', 'nazwa', 'typ', 'aromat', 'moc', 'goryczka', 'nuty_owocowe', 'piana', 'kolor', 'mętność', 'zgazowanie', 'ocena', 'uwagi',)
        labels = {
            'autor' : "Twój nick",
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('autor', css_class="form50"), 
            Field('firma', css_class="form50"), 
            Field('nazwa', css_class="form50"), 
            Field('typ', css_class="form50"), 
            Field('aromat', css_class="form10"), 
            Field('moc', css_class="form10"), 
            Field('goryczka', css_class="form10"),
            Field('nuty_owocowe', css_class="form10"),
            Field('piana', css_class="form10"),
            Field('kolor', css_class="form10"),
            Field('mętność', css_class="form10"),
            Field('zgazowanie', css_class="form10"),  
            Field('ocena', css_class="form10"), 
            Field('uwagi'),
        )
        self.helper.add_input(Submit('submit', 'Zapisz'))

class WinoForm(forms.ModelForm):

    class Meta:
        model = Wino
        fields = (
            'autor',
            'firma',
            'nazwa',
            'typ',
            'zawartość_cukru',
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
            'zawartość_cukru' : "Zawartość cukru",
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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.layout = Layout(
            Field('autor', css_class="form50"), 
            Field('firma', css_class="form50"), 
            Field('nazwa', css_class="form50"),
            Field('typ', css_class="form10"),
            Field('zawartość_cukru', css_class="form10"),
            Field('kolor', css_class="form10"),   
            Field('klarowność', css_class="form10"), 
            Field('musowanie', css_class="form10"), 
            Field('aromat', css_class="form10"), 
            Field('nuty_zielonych_owoców', css_class="form10"),
            Field('nuty_czerwonych_owoców', css_class="form10"),
            Field('nuty_czarnych_owoców', css_class="form10"),
            Field('nuty_cytrusowe', css_class="form10"),  
            Field('nuty_tropikalne', css_class="form10"),  
            Field('nuty_pestkowców', css_class="form10"),  
            Field('nuty_suszonych_owoców', css_class="form10"),  
            Field('nuty_roślinne', css_class="form10"),  
            Field('nuty_kwiatowe', css_class="form10"),  
            Field('nuty_drożdżowe', css_class="form10"),  
            Field('nuty_dojrzewające', css_class="form10"),  
            Field('nuty_maślane', css_class="form10"),  
            Field('nuty_dębowe', css_class="form10"),  
            Field('nuty_maślane', css_class="form10"),  
            Field('nuty_ziemne', css_class="form10"),  
            Field('nuty_minerałów', css_class="form10"),    
            Field('ocena', css_class="form10"), 
            Field('uwagi'),
        )
        self.helper.add_input(Submit('submit', 'Zapisz'))

class KawaForm(forms.ModelForm):

    class Meta:
        model = Kawa
        fields = ('autor', 'firma', 'nazwa', 'arabica', 'stopień_palenia', 'kwasowość', 'moc',  'ocena', 'uwagi')
        labels = {
            'arabica' : "Arabica [%]",
            'autor' : "Twój nick",
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-exampleForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_survey'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            Field('autor', css_class="form50"), 
            Field('firma', css_class="form50"), 
            Field('nazwa', css_class="form50"), 
            Field('arabica', css_class="form10"), 
            Field('stopień_palenia', css_class="form10"), 
            Field('kwasowość', css_class="form10"), 
            Field('moc', css_class="form10"),  
            Field('ocena', css_class="form10"), 
            Field('uwagi'),
        )
        self.helper.add_input(Submit('submit', 'Zapisz'))
