from django import forms


class RegisterForm(forms.Form):
	firstname = forms.CharField(label='First name', max_length=100)
	lastname = forms.CharField(label='Last name', max_length=100)
	email = forms.EmailField()

	class Meta:
		fields = [
			"firstname",
			"lastname",
			"email",
		]