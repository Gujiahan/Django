from resumes.models import Archive
from django.forms import ModelForm
from django.forms.widgets import Textarea,TextInput,NumberInput,Select

class ArchiveForm(ModelForm):
    class Meta:
        model = Archive
        fields = ['name', 'price', 'profile', 'location']
        widgets = {
            'price': NumberInput(attrs={'size': 32}),
            'name': TextInput(attrs={'size': 32}),
            'profile': Textarea(attrs={'cols': 80, 'rows': 20}),
            'location': Select()
        }

        labels = {
            'name': '名子',
            'price': '價錢',
            'profile': '描述',
            'location': '地點',
        }