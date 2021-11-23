from django.db import models
from django.contrib.auth.models import User
from django import forms

# 자유게시판 TABLE 정의
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 작성자
    title = models.CharField(max_length=30) # 게시글 제목, 30자까지 입력가능
    pub_date = models.DateTimeField('date published') # 작성일자
    body = models.TextField() # 게시글 내용
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0) # 조회수, 기본값은 0, 양수로만 나오도록

    def __str__(self):
        return self.title # 글 제목이 타이틀로 보이도록
    
    def summary(self):
        return self.body[:100] # 본문 미리보기가 100글자 까지만 보이도록

    @property
    def update_counter(self): # 조회수 기능 설정
        self.save()
        self.hits += 1
        return self.hits
        
# 홍보게시판 TABLE 정의
class Pr(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title 
    
    def summary(self):
        return self.body[:100] 
    @property
    def update_counter(self):
        self.save()
        self.hits += 1
        return self.hits

# 정보게시판 TABLE 정의
class Information(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title 

    def summary(self):
        return self.body[:100]

    @property
    def update_counter(self):
        self.save()
        self.hits += 1
        return self.hits

# 졸업생게시판 TABLE 정의
class Graduate(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    hits = models.PositiveIntegerField(verbose_name='조회수', default=0)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    @property
    def update_counter(self):
        self.save()
        self.hits += 1
        return self.hits

# 자유 게시판 댓글 TABLE 정의
class Comment(models.Model):
    comment = models.TextField() # 댓글 내용
    date = models.DateTimeField(auto_now_add=True) # 작성일, 시간
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # 작성자 
    #Post를 참조(foreign)함
    #댓글달린 게시글이 삭제되면 참조객체도 삭제
    post = models.ForeignKey(Post, null=True, blank=True, on_delete=models.CASCADE, related_name ='comments')

    #게시글 작성시 DB에 title이 나오도록 함
    def __str__(self):
        return self.comment

# 홍보게시판 댓글 TABLE 정의
class PrComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Pr, null=True, blank=True, on_delete=models.CASCADE, related_name ='comments')

    def __str__(self):
        return self.comment

#졸업생게시판 댓글 TABLE 정의
class GradComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Graduate, null=True, blank=True, on_delete=models.CASCADE, related_name ='comments')

    def __str__(self):
        return self.comment

#정보게시판 댓글 TABLE 정의
class InfoComment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Information, null=True, blank=True, on_delete=models.CASCADE, related_name ='comments')

    def __str__(self):
        return self.comment


""" # USER TABLE 정의 (django/contrib/auth/models.py에 따로 정의되어 있음)
class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'), # 유저 이름은 최대 150자 
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."), # 유저 name 중복 방지
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True) #이름
    last_name = models.CharField(_('last name'), max_length=150, blank=True) # 성
    email = models.EmailField(_('email address'), blank=True) #email
    is_staff = models.BooleanField( # admin 권한 여부
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField( # 접속 활성화 여부
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name) # 성과 이름을 조합해 full name을 만듬
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)
        
class User(AbstractUser):
    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'"""