from django import forms
from cars.models import Brand, Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    # def clean_value(self):
    #     value = self.cleaned_data.get('value')

    #     if value < 10000:
    #         self.add_error('value', 'Valor mínimo do carro deve ser superior a R$ 10.000,00!')

    # def clean_factory_year(self):
    #     factory_year = self.cleaned_data.get('factory_year')

    #     if factory_year < 1975:
    #         self.add_error('factory_year', 'Não é permitido carros inferiores a 1975!')