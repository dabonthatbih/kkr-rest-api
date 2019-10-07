from django.forms import ModelForm
from verify.models import Customer
from django_countries.widgets import CountrySelectWidget

class CustomerForm(ModelForm):
	class meta:
		model = Customer
		fields = [User,email, gender, first_name, last_name, country, adress, zip_code]
		widgets = {'country': CountrySelectWidget()}