from django import forms
from .models import Images
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Field

class ImagesForm(forms.Form):
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('Post','Post',css_class='btn-primary'))

    class Meta:
        model = Images
        fields = {
            'image'
            'caption'
        }

