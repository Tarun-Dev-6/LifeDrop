from django import forms
from .models import DonorDetails,studentdetails

class DonorForm(forms.ModelForm):
    class Meta:
        model = DonorDetails
        fields = '__all__'


class EmailForm(forms.Form):
    recipient_email = forms.EmailField(label="Recipient Email")
    subject = forms.CharField(max_length=200, label="Subject")
    message = forms.CharField(widget=forms.Textarea, label="Message")


class studentdetailsForm(forms.ModelForm):
    class Meta:
        model = studentdetails
        fields = '__all__'

    
