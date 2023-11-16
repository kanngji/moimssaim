from django import forms
from promotion.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category','title','discription','meet_date']