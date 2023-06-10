from django import forms
from .models import Tgran,Taslmeh
class MarkForm(forms.ModelForm):
	#password=forms.CharField(widget=forms.PasswordInput)
	#image=forms.ImageField(widget=forms.ImageField)
	class Meta:
		model=Tgran
		fields='__all__'
class TaslmehForm(forms.ModelForm):
	#name=forms.CharField(label="Name:",widget=forms.TextInput(attrs={'class':'form-control'}))
	#age=forms.CharField(label="age:",widget=forms.TextInput(attrs={'class':'form-control'}))
	##book=forms.CharField(label="Books:",widget=forms.Select(attrs={'class':'form-control'}))
	#book=forms.ModelChoiceField(queryset=Books.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
	class Meta:
		model=Taslmeh
		fields='__all__'

