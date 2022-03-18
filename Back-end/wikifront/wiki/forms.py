from django import forms
from wiki.models import EditSession, Wiki_page

class WikiPageForm(forms.ModelForm):
    class Meta:
        model = Wiki_page
        exclude = ['slug']


class EditSessionForm(forms.ModelForm):
    class Meta:
        model = EditSession
        fields = ['note']