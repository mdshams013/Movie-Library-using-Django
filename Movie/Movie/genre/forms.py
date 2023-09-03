from django import forms

from .models import Name

INPUT_CLASSES = 'w-half py-2 px-4 rounded-xl border'

class NewMovie(forms.ModelForm):
    class Meta:
        model = Name
        fields = ('name','genre','synopsis','director_name','actors_name','year','image')
        widgets = {
            'name' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'genre' : forms.Select(attrs={
                'class': INPUT_CLASSES
            }),

            'synopsis' : forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),

            'director_name' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'actors_name' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'year' : forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'image' : forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),         
        }
