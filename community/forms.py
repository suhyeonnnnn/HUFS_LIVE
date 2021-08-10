#입력값 받는 클래스, 객체 생성하여 DB에 반영

from django import forms
from django.forms import fields
from .models import Comment, Post, PrComment, GradComment, InfoComment #모델기반이므로

#forms의 modelforms을 상속받아 만듦
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']


#댓글 작성
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

#홍보게시판 댓글 작성
class PrCommentForm(forms.ModelForm):
    class Meta:
        model = PrComment
        fields = ['comment']

#졸업생게시판 댓글 작성
class GradCommentForm(forms.ModelForm):
    class Meta:
        model = GradComment
        fields = ['comment']

#정보게시판 댓글 작성
class InfoCommentForm(forms.ModelForm):
    class Meta:
        model = InfoComment
        fields = ['comment']