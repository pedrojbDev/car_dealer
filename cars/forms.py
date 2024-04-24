from typing import Any
from django import forms
from cars.models import Brand,Car


  
class CarModelForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'

  def clean_value(self):
    value = self.cleaned_data.get('value')
    if value < 20000:
      self.add_error('value','Valor minimo do carro deve ser R$ 20.000')
    return value

  def clean_model_year(self):
    model_year= self.cleaned_data.get('model_year')
    if model_year < 1975:
      self.add_error('model_year', 'O modelo do carro deve ser de 1975 para cima')
    return model_year

