from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post
from .forms import PostForm, CommentForm #forms.py의 PostForm 객체 불러오기

def home(request):
    posts = Post.objects.filter().order_by('pub_date') #date의 오름차순으로 정렬
    return render(request, 'home.html', {'posts':posts})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk= post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form}) 

def new(request):
    return render(request, 'new.html')

def create(request): #new.html의 form에서 입력받은 내용을 DB로 넣어주는 함수
    community = Post()
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() #객체에 해당하는 내용들을 /admin 에 저장
    return redirect('/post/'+str(community.id)) #글 작성을 완료하면 해당 글 detail이 뜨도록


# 댓글 저장
def new_comment(request, post_id) : 
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid() : 
        # 바로 저장하지 않고
        finished_form = filled_form.save(commit=False)
        # models.py > class Comment > post 정보 확인하여 연결된 게시글 확인
        # 모델객체안에 필요한 정보를 채우고
        finished_form.post = get_object_or_404(Post, pk=post_id)
        # 저장한다.
        finished_form.save()
    return redirect('detail', post_id) # 댓글작성한 상세페이지로 이동


# update
def update(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        post.save()
        return redirect('detail', post.id)
    return render(request, 'update.html', {'post_detail': post})


# delete
def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect("home")