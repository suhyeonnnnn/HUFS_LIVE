from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title # 글 제목이 타이틀로 보이도록
    
    def summary(self):
        return self.body[:100] # 본문 미리보기가 100글자 까지만 보이도록