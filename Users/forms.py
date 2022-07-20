from cProfile import label
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, forms
from django.contrib.auth.models import User
from .models import profile

from users.models import profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Name"
        }

    def __init__(self, *args, **kargs):
        super(CustomUserCreationForm, self).__init__(*args, **kargs)

        for name,field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

    
class ProfileForm(ModelForm):   
    class Meta:
        model = profile
        fields = "__all__"
