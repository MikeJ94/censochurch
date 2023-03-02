from datetime import datetime
from django import forms  
from myapp.models import Person, Hijo
#from dal import autocomplete



#Prueba 1 
"""class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'

class SelectDateWidget(forms.SelectDateWidget):
    input_type = 'datetime-local'


 class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = ['name','lastname','dni', 'celular','gender','member','address','date_birth','date_joined','age','state']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control' ,'placeholder': 'Escriba sus dos nombres'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Escriba sus dos apellidos'}),
            'dni': forms.TextInput(attrs={'class': 'form-control','placeholder': 'No agregar guiones'}),
            'celular': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'No agregar guiones'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'member': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'cols': '60','rows': '3','class': 'form-control'}),
            'date_birth': SelectDateWidget(years=range(1900,2031),attrs={'class': 'form-control'}),
            'date_joined': forms.DateInput(format='%Y-%m-%d', attrs={'disabled': True,'class': 'form-control','value': datetime.now().strftime('%Y-%m-%d')}),
            'age': forms.NumberInput( attrs={'class': 'form-control','placeholder': 'Escriba su edad'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            
        } """
#Prueba 1 

#Prueba 2
class PersonForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['childrenmtm'].queryset = Hijo.objects.none()

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'date_birth': forms.SelectDateWidget(years=range(1900,2031)),
            'dni': forms.TextInput(attrs={'placeholder': 'No agregar guiones, ni letras'}),
            #'date_joined': forms.DateInput (attrs={'disabled': True}),
            'observationbap': forms.Textarea(attrs={'cols': '60','rows': '3'}),
            'ministry': forms.CheckboxSelectMultiple(),

            'childrenmtm': forms.SelectMultiple(attrs={
                'class': 'form-control select2'
                
             }),

            #'childrenmtm': forms.CheckboxSelectMultiple(),
            #'childrenmtm':autocomplete.ModelSelect2Multiple(),
            #'image':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'cols': '60','rows': '3'})
        }
        exclude = ['']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data 


#Prueba 2

class SonForm(forms.ModelForm):

    class Meta:
        model = Hijo
        fields = '__all__'
        widgets = {
            'ministry': forms.CheckboxSelectMultiple(),
        
        }
        exclude = ['']