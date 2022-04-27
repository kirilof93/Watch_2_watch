from django import forms

from Watch_2_watch.accounts.models import UserProfile
from core.BootstrapFormMixin import BootstrapFormMixin
from Watch_2_watch.watches.models import Watch


class WatchForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Watch
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'some-class',
                }
            )
        }


class EditWatchForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Watch
        fields = '__all__'
        exclude = ['user']
        widgets = {
            'image_url': forms.TextInput()
        }


class CreateWatchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['readonly'] = 'readonly'

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Watch
        fields = '__all__'
        widgets = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }
