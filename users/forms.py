from django import forms
from .models import Location, User, Profile
from .widgets import CustomPictureImageFieldWisget



class UserForm(forms.ModelForm):
    username=forms.CharField(disabled=True)
    class Meta:
        model=User
        fields=('username', 'first_name', 'last_name', 'email')
        
class ProfileForm(forms.ModelForm):
    photo=forms.ImageField(widget=CustomPictureImageFieldWisget)   
    class Meta:
        model=Profile
        fields=('photo', 'bio', 'phone_number')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 40}),  # Textarea for bio
        }
     
class LocationForm(forms.ModelForm):
    address_1=forms.CharField(required=True)
    address_2=forms.CharField(required=True)
    class Meta:
        model=Location
        fields={'address_1', 'address_2', 'city', 'state', 'zip_code'}
       