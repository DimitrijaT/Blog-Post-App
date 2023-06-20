from django import forms
from .models import Post, File, Block, BlogUser


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        exclude = ["user"]


class BlockForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BlockForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Block
        fields = ["blocked"]
