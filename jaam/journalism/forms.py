from django import forms
from jaam.journalism.models import UserProfile, Journalist

class JournalistForm(forms.ModelForm):
    class Meta:
        model = Journalist
        exclude = ('user_profile') 
        
    def getBio(self):
        return self.cleaned_data["bio"]
    def getMajor(self):
        return self.cleaned_data["major"]
        
class UserProfileForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = UserProfile
        exclude = ('user') 
        
    def getFull_Name(self):
        return self.cleaned_data["full_name"]
    def getEmail(self):
        return self.cleaned_data["email"]