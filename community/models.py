from django.db import models
from django.contrib.auth.models import User

# 자유게시판
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title # 글 제목이 타이틀로 보이도록
    
    def summary(self):
        return self.body[:100] # 본문 미리보기가 100글자 까지만 보이도록

    @property
    def update_counter(self):
        self.hits = self.hits +1
        self.save()
        return self.hits
        
# 홍보게시판
class Pr(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title # 글 제목이 타이틀로 보이도록
    
    def summary(self):
        return self.body[:100] # 본문 미리보기가 100글자 까지만 보이도록
    @property
    def update_counter(self):
        self.hits = self.hits +1
        self.save()
        return self.hits

# 정보게시판
class Information(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title # 글 제목이 타이틀로 보이도록

    def summary(self):
        return self.body[:100] # 본문 미리보기가 100글자 까지만 보이도록

    @property
    def update_counter(self):
        self.hits = self.hits +1
        self.save()
        return self.hits

#졸업생게시판
class Graduate(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title # 글 제목이 타이틀로 보이도록

    def summary(self):
        return self.body[:100] # 본문 미리보기가 100글자 까지만 보이도록

    @property
    def update_counter(self):
        self.hits = self.hits +1
        self.save()
        return self.hits

# 댓글
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #Post를 참조(foreign)함
    #댓글달린 게시글이 삭제되면 참조객체도 삭제
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    #게시글 작성시 DB에 title이 나오도록 함
    def __str__(self):
        return self.comment

#홍보게시판 댓글
class PrComment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    #Post를 참조(foreign)함
    #댓글달린 게시글이 삭제되면 참조객체도 삭제
    post = models.ForeignKey(Pr, null=True, blank=True, on_delete=models.CASCADE, related_name ='comments')

    #게시글 작성시 DB에 title이 나오도록 함
    def __str__(self):
        return self.comment

#졸업생게시판 댓글
class GradComment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    #Post를 참조(foreign)함
    #댓글달린 게시글이 삭제되면 참조객체도 삭제
    post = models.ForeignKey(Graduate, null=True, blank=True, on_delete=models.CASCADE, related_name ='comments')

    #게시글 작성시 DB에 title이 나오도록 함
    def __str__(self):
        return self.comment

#정보게시판 댓글
class InfoComment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    #Post를 참조(foreign)함
    #댓글달린 게시글이 삭제되면 참조객체도 삭제
    post = models.ForeignKey(Information, null=True, blank=True, on_delete=models.CASCADE, related_name ='comments')

    #게시글 작성시 DB에 title이 나오도록 함
    def __str__(self):
        return self.comment      