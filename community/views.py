from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post, Pr, Information, Graduate
from .forms import PostForm,PrForm,InfoForm,GradForm, CommentForm, pr_CommentForm, info_CommentForm,grad_CommentForm#forms.py의 PostForm 객체 불러오기
from django.core.paginator import Paginator

def home(request):
    posts = Post.objects.filter().order_by('-pub_date')[:5]
    prs = Pr.objects.filter().order_by('-pub_date')[:5]
    informations = Information.objects.filter().order_by('-pub_date')[:5]
    graduates = Graduate.objects.filter().order_by('-pub_date')[:5] 
    return render(request, 'home.html', {'posts':posts, 'prs':prs, 'informations':informations, 'graduates':graduates})

#상세 페이지
def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk= post_id)
    comment_form = CommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form':comment_form}) 

def detail_pr(request, pr_id):
    pr_detail = get_object_or_404(Pr, pk= pr_id)
    comment_form = pr_CommentForm()
    return render(request, 'pr_detail.html', {'pr_detail':pr_detail, 'comment_form': comment_form})

def detail_information(request, information_id):
    information_detail = get_object_or_404(Information, pk= information_id)
    comment_form = info_CommentForm()
    return render(request, 'information_detail.html', {'informatio_detail':information_detail, 'comment_form':comment_form})

def detail_graduate(request, graduate_id):
    graduate_detail = get_object_or_404(Graduate, pk= graduate_id)
    comment_form = grad_CommentForm()
    return render(request, 'graduate_detail.html', {'graduate_detail':graduate_detail, 'comment_form':comment_form})

#새로운 게시물 작성
def new(request):
    return render(request, 'free_new.html')

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
    return redirect('free_detail', post_id) # 댓글작성한 상세페이지로 이동

def pr_new_comment(request, pr_id) : 
    filled_form = PrForm(request.POST)
    if filled_form.is_valid() : 
        # 바로 저장하지 않고
        finished_form = filled_form.save(commit=False)
        # models.py > class Comment > post 정보 확인하여 연결된 게시글 확인
        # 모델객체안에 필요한 정보를 채우고
        finished_form.post = get_object_or_404(Pr, pk=pr_id)
        # 저장한다.
        finished_form.save()
    return redirect('pr_detail', pr_id) # 댓글작성한 상세페이지로 이동

def information_new_comment(request, information_id) : 
    filled_form = InfoForm(request.POST)
    if filled_form.is_valid() : 
        # 바로 저장하지 않고
        finished_form = filled_form.save(commit=False)
        # models.py > class Comment > post 정보 확인하여 연결된 게시글 확인
        # 모델객체안에 필요한 정보를 채우고
        finished_form.post = get_object_or_404(Information, pk=information_id)
        # 저장한다.
        finished_form.save()
    return redirect('information_detail', information_id) # 댓글작성한 상세페이지로 이동

def graduate_new_comment(request, graduate_id) : 
    filled_form = GradForm(request.POST)
    if filled_form.is_valid() : 
        # 바로 저장하지 않고
        finished_form = filled_form.save(commit=False)
        # models.py > class Comment > post 정보 확인하여 연결된 게시글 확인
        # 모델객체안에 필요한 정보를 채우고
        finished_form.post = get_object_or_404(Graduate, pk=graduate_id)
        # 저장한다.
        finished_form.save()
    return redirect('graduate_detail', graduate_id) # 댓글작성한 상세페이지로 이동


# update
def update(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        post.save()
        return redirect('free_detail', post.id)
    return render(request, 'free_update.html', {'post_detail': post})

def pr_update(request, pr_id):
    pr = Pr.objects.get(id = pr_id)
    if request.method == "POST":
        pr.title = request.POST["title"]
        pr.body = request.POST["body"]
        pr.save()
        return redirect('pr_detail', pr.id)
    return render(request, 'pr_update.html', {'pr': pr})

def information_update(request, information_id):
    information = Information.objects.get(id = information_id)
    if request.method == "POST":
        information.title = request.POST["title"]
        information.body = request.POST["body"]
        information.save()
        return redirect('information_detail', information.id)
    return render(request, 'information_update.html', {'information': information})

def graduate_update(request, graduate_id):
    graduate = Graduate.objects.get(id = graduate_id)
    if request.method == "POST":
        graduate.title = request.POST["title"]
        graduate.body = request.POST["body"]
        graduate.save()
        return redirect('graduate_detail', graduate.id)
    return render(request, 'graduate_update.html', {'graduate': graduate})


# delete
def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect("home")

def pr_delete(request, pr_id):
    pr = Pr.objects.get(id = pr_id)
    pr.delete()
    return redirect('home')

def information_delete(request, information_id):
    information = Information.objects.get(id = information_id)
    information.delete()
    return redirect('home')
    
def graduate_delete(request, graduate_id):
    graduate = Graduate.objects.get(id = graduate_id)
    graduate.delete()
    return redirect('home')


#게시판
def free_board(request):
    posts = Post.objects.filter().order_by('-pub_date')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    paginated_posts = paginator.get_page(page)
    return render(request, 'free_board.html', {'posts': paginated_posts})

def pr_board(request):
    prs = Pr.objects.filter().order_by('-pub_date')
    paginator = Paginator(prs, 10)
    page = request.GET.get('page')
    paginated_prs = paginator.get_page(page)
    return render(request, 'pr_board.html', {'prs': paginated_prs})

def information_board(request):
    informations = Information.objects.filter().order_by('-pub_date')
    paginator = Paginator(informations, 10)
    page = request.GET.get('page')
    paginated_informations = paginator.get_page(page)
    return render(request, 'information_board.html', {'informations': paginated_informations})

def graduate_board(request):
    graduates = Graduate.objects.filter().order_by('-pub_date')
    paginator = Paginator(graduates, 10)
    page = request.GET.get('page')
    paginated_graduates = paginator.get_page(page)
    return render(request, 'graduate_board.html', {'graduates': paginated_graduates})