#입력값 받는 클래스, 객체 생성하여 DB에 반영

from django import forms
from django.forms import fields
from .models import Comment, Post #모델기반이므로

#forms의 modelforms을 상속받아 만듦
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'


#댓글 작성
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
