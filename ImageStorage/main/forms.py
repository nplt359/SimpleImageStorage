from django import forms
from .models import Images

class AddImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('image', 'title',)
        labels = {
            'image': "Картинка",
            'title': "Заголовок",
        }