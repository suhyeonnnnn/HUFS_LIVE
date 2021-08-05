from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post, Pr, Information, Graduate
from .forms import PostForm, CommentForm #forms.py의 PostForm 객체 불러오기

def home(request):
    posts = Post.objects.filter().order_by('-pub_date') #date의 오름차순으로 정렬
    prs = Pr.objects.filter().order_by('-pub_date')
    informations = Information.objects.filter().order_by('-pub_date')
    graduates = Graduate.objects.filter().order_by('-pub_date') 
    return render(request, 'home.html', {'posts':posts, 'prs':prs, 'informations':informations, 'graduates':graduates})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk= post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form}) 

def detail_pr(request, pr_id):
    pr_detail = get_object_or_404(Pr, pk= pr_id)

    return render(request, 'pr_detail.html', {'pr':pr_detail})

def detail_information(request, information_id):
    information_detail = get_object_or_404(Information, pk= information_id)

    return render(request, 'information_detail.html', {'information':information_detail})

def detail_graduate(request, graduate_id):
    graduate_detail = get_object_or_404(Graduate, pk= graduate_id)

    return render(request, 'graduate_detail.html', {'graduate':graduate_detail})

def new(request):
    return render(request, 'new.html')

def pr_new(request):
    return render(request, 'pr_new.html')

def information_new(request):
    return render(request, 'information_new.html')

def graduate_new(request):
    return render(request, 'graduate_new.html')

def create(request): #new.html의 form에서 입력받은 내용을 DB로 넣어주는 함수
    community = Post()
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() #객체에 해당하는 내용들을 /admin 에 저장
    return redirect('/post/'+str(community.id)) #글 작성을 완료하면 해당 글 detail이 뜨도록

def pr_create(request): 
    community = Pr()
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() 
    return redirect('/pr/'+str(community.id)) 

def information_create(request): 
    community = Information()
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() 
    return redirect('/information/'+str(community.id)) 

def graduate_create(request): 
    community = Graduate()
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() 
    return redirect('/graduate/'+str(community.id)) 

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