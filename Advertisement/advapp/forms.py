from django import forms
from .models import Advertisement, Response


class AdvForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            'title',
            'category',
            'author',
            'content',
            'file',
        ]


class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = [
            'author',
            'advertisement',
            'text',
        ]


