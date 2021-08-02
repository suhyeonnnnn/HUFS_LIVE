from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post

def home(request):
    posts = Post.objects
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk= post_id) 

    return render(request, 'detail.html', {'post':post_detail})

def new(request):
    return render(request, 'new.html')

def create(request): #new.html의 form에서 입력받은 내용을 DB로 넣어주는 함수
    community = Post()
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() #객체에 해당하는 내용들을 /admin 에 저장
    return redirect('/post/'+str(community.id)) #글 작성을 완료하면 해당 글 detail이 뜨도록