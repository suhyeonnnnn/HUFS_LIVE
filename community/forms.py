#입력값 받는 클래스, 객체 생성하여 DB에 반영

from django import forms
from django.forms import fields
from .models import Comment,Pr_Comment,Info_Comment,Grad_Comment, Post, Pr, Information, Graduate #모델기반이므로

#forms의 modelforms을 상속받아 만듦
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

class PrForm(forms.ModelForm):
    class Meta:
        model = Pr
        fields = ['title', 'body']

class InfoForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['title', 'body']

class GradForm(forms.ModelForm):
    class Meta:
        model = Graduate
        fields = ['title', 'body']


#댓글 작성
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class pr_CommentForm(forms.ModelForm):
    class Meta:
        model = Pr_Comment
        fields = ['pr_comment']

class info_CommentForm(forms.ModelForm):
    class Meta:
        model = Info_Comment
        fields = ['comment']

class grad_CommentForm(forms.ModelForm):
    class Meta:
        model = Grad_Comment
        fields = ['comment']
