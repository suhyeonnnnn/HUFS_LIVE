from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title # 글 제목이 타이틀로 보이도록
    
    def summary(self):
        return self.body[:100] # 본문 미리보기가 100글자 까지만 보이도록


#댓글
class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #Post를 참조(foreign)함
    #댓글달린 게시글이 삭제되면 참조객체도 삭제
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE)

    #게시글 작성시 DB에 title이 나오도록 함
    def __str__(self):
        return self.comment


        