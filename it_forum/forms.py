from django import forms
from it_forum.models import ItForum


class ItForumForm(forms.ModelForm):
    class Meta:
        model = ItForum
        fields = '__all__'
