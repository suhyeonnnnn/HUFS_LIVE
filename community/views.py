from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post, Pr, Information, Graduate
from .forms import PostForm, CommentForm, PrCommentForm, GradCommentForm, InfoCommentForm #forms.py의 PostForm 객체 불러오기
from django.core.paginator import Paginator
from datetime import date, datetime, timedelta

## HOME 구성
def home(request):
    posts = Post.objects.filter().order_by('-pub_date')[:5] # 작성일을 기준으로 내림차순으로 정렬, 최근 5개까지만 보이도록
    prs = Pr.objects.filter().order_by('-pub_date')[:5]
    informations = Information.objects.filter().order_by('-pub_date')[:5]
    graduates = Graduate.objects.filter().order_by('-pub_date')[:5] 
    return render(request, 'home.html', {'posts':posts, 'prs':prs, 'informations':informations, 'graduates':graduates})

## 상세 페이지 구성
# 자유 게시판 
def detail(request,  free_id):
    post_detail = get_object_or_404(Post, pk= free_id) 
    comments = post_detail.comments.order_by("-date") # 작성일을 기준으로 댓글 정렬
    new_comment = None 
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # 댓글 생성, DB에는 저장X
            new_comment = comment_form.save(commit=False)
            # 현재 글에 댓글 할당
            new_comment.post = post_detail
            # DB에 저장
            new_comment.save()
    else:
        comment_form = CommentForm()
    
    # 쿠키설정을 기준으로 조회수 확인
    session_cookie = request.session.get('user')
    cookie_name = F'hits:{session_cookie}'
    context = {
        'post_detail':post_detail, 
        "comments": comments,
        "new_comment": new_comment,
        "comment_form": comment_form,
        }

    response = render(request, 'free_detail.html', context)

    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(free_id) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{free_id}', expires=None)
            post_detail.hits += 1
            post_detail.save()
            return response
    else:
        response.set_cookie(cookie_name, free_id, expires=None)
        post_detail.hits += 1
        post_detail.save()
        return response

    return render(request, 'free_detail.html', context)

# 홍보게시판
def detail_pr(request, pr_id):
    pr_detail = get_object_or_404(Pr, pk= pr_id)
    comments = pr_detail.comments.order_by("-date")
    new_comment = None

    if request.method == "POST":
        comment_form = PrCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = pr_detail
            new_comment.save()
    else:
        comment_form = PrCommentForm()

    session_cookie = request.session.get('user')
    cookie_name = F'hits:{session_cookie}'

    context = {
            "pr_detail": pr_detail,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        }

    response = render(request, 'pr_detail.html', context)

    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(pr_id) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{pr_id}', expires=None)
            pr_detail.hits += 1
            pr_detail.save()
            return response
    else:
        response.set_cookie(cookie_name, pr_id, expires=None)
        pr_detail.hits += 1
        pr_detail.save()
        return response   

    return render(request, 'pr_detail.html', context)

# 정보 게시판
def detail_information(request, information_id):
    information_detail = get_object_or_404(Information, pk= information_id)
    comments = information_detail.comments.order_by("-date")
    new_comment = None
    if request.method == "POST":
        comment_form = InfoCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = information_detail
            new_comment.save()
    else:
        comment_form = InfoCommentForm()
    
    session_cookie = request.session.get('user')
    cookie_name = F'hits:{session_cookie}'

    context = {
            "information_detail": information_detail,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        }

    response = render(request, 'information_detail.html', context)

    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(information_id) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{information_id}', expires=None)
            information_detail.hits += 1
            information_detail.save()
            return response
    else:
        response.set_cookie(cookie_name, information_id, expires=None)
        information_detail.hits += 1
        information_detail.save()
        return response 

    return render(request,'information_detail.html',context)

# 졸업생 게시판
def detail_graduate(request, graduate_id):
    graduate_detail = get_object_or_404(Graduate, pk= graduate_id)
    comments = graduate_detail.comments.order_by("-date")

    new_comment = None
    if request.method == "POST":
        comment_form = GradCommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = graduate_detail
            new_comment.save()
    else:
        comment_form = GradCommentForm()

    session_cookie = request.session.get('user')
    cookie_name = F'hits:{session_cookie}'

    context = {
            "graduate_detail": graduate_detail,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        }

    response = render(request, 'information_detail.html', context)

    if request.COOKIES.get(cookie_name) is not None:
        cookies = request.COOKIES.get(cookie_name)
        cookies_list = cookies.split('|')
        if str(graduate_id) not in cookies_list:
            response.set_cookie(cookie_name, cookies + f'|{graduate_id}', expires=None)
            graduate_detail.hits += 1
            graduate_detail.save()
            return response
    else:
        response.set_cookie(cookie_name, graduate_id, expires=None)
        graduate_detail.hits += 1
        graduate_detail.save()
        return response 

    return render(request,'graduate_detail.html',context)

   
## 새 글 작성 폼 불러오기
# 자유게시판
def new(request):
    return render(request, 'free_new.html')
# 홍보게시판
def pr_new(request):
    return render(request, 'pr_new.html')
# 정보게시판
def information_new(request):
    return render(request, 'information_new.html')
# 졸업생 게시판
def graduate_new(request):
    return render(request, 'graduate_new.html')


## 새글 작성 폼
# 자유게시판
def create(request): 
    community = Post()
    community.author = request.user 
    community.title = request.GET['title'] # 제목입력
    community.body = request.GET['body'] # 내용입력
    community.pub_date = timezone.datetime.now() 

    if (community.title == '') or (community.body == ''): # 제목과 내용이 비어있는 경우, ERROR 메세지 
        return render(request, 'free_new.html', {'post_detail': community,'error': '제목과 본문을 모두 입력해주세요'})
    else:
        community.save() # DB에 저장
        return redirect('/free/'+str(community.id)) # 해당 게시물 URL로 이동

# 홍보게시판
def pr_create(request): 
    community = Pr()
    community.author = request.user
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()

    if (community.title == '') or (community.body == ''):
        return render(request, 'pr_new.html', {'pr': community, 'error': '제목과 본문을 모두 입력해주세요'})
    else:
        community.save()
        return redirect('/pr/'+str(community.id))

# 정보게시판
def information_create(request): 
    community = Information()
    community.author = request.user
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()

    if (community.title == '') or (community.body == ''):
        return render(request, 'information_new.html', {'information': community,'error': '제목과 본문을 모두 입력해주세요'})
    else:
        community.save()
        return redirect('/information/'+str(community.id))

# 졸업생 게시판
def graduate_create(request): 
    community = Graduate()
    community.author = request.user
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()

    if (community.title == '') or (community.body == ''):
        return render(request, 'graduate_new.html', {'graduate': community, 'error': '제목과 본문을 모두 입력해주세요'})
    else:
        community.save()
        return redirect('/graduate/'+str(community.id))

## 댓글 저장
def new_comment(request, free_id) : 
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid() : 
        # 바로 저장하지 않고
        finished_form = filled_form.save(commit=False)
        # models.py > class Comment > post 정보 확인하여 연결된 게시글 확인
        # 모델객체안에 필요한 정보를 채우고
        finished_form.post = get_object_or_404(Post, pk=free_id)
        # 저장한다.
        finished_form.save()
    return redirect('free_detail', free_id) # 댓글작성한 상세페이지로 이동

## 게시글 수정(update)
# 자유게시판
def update(request, free_id):
    post = Post.objects.get(id = free_id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        if (post.title == '') or (post.body == ''):
            return render(request, 'free_update.html', {'post_detail': post, 'error': '제목과 본문을 모두 입력해주세요'})
        else:
            post.save()
            return redirect('free_detail', post.id)
    return render(request, 'free_update.html', {'post_detail': post})

# 홍보게시판
def pr_update(request, pr_id):
    pr = Pr.objects.get(id = pr_id)
    if request.method == "POST":
        pr.title = request.POST["title"]
        pr.body = request.POST["body"]
        if (pr.title == '') or (pr.body == ''):
            return render(request, 'pr_update.html', {'pr': pr, 'error': '제목과 본문을 모두 입력해주세요'})
        else:
            pr.save()
            return redirect('pr_detail', pr.id)
    return render(request, 'pr_update.html', {'pr': pr})

# 정보게시판
def information_update(request, information_id):
    information = Information.objects.get(id = information_id)
    if request.method == "POST":
        information.title = request.POST["title"]
        information.body = request.POST["body"]
        if (information.title == '') or (information.body == ''):
            return render(request, 'information_update.html', {'information': information, 'error': '제목과 본문을 모두 입력해주세요'})
        else:
            information.save()
            return redirect('information_detail', information.id)
    return render(request, 'information_update.html', {'information': information})

# 졸업생게시판
def graduate_update(request, graduate_id):
    graduate = Graduate.objects.get(id = graduate_id)
    if request.method == "POST":
        graduate.title = request.POST["title"]
        graduate.body = request.POST["body"]
        if (graduate.title == '') or (graduate.body == ''):
            return render(request, 'graduate_update.html', {'graduate': graduate, 'error': '제목과 본문을 모두 입력해주세요'})
        else:
            graduate.save()
            return redirect('graduate_detail', graduate.id)
    return render(request, 'graduate_update.html', {'graduate': graduate})


## 게시글 삭제 (delete)
# 자유게시판
def delete(request, free_id):
    post = Post.objects.get(id = free_id)
    post.delete() # 게시글 삭제 
    return redirect("free_board") # 게시글 List URL로 이동
# 홍보게시판
def pr_delete(request, pr_id):
    pr = Pr.objects.get(id = pr_id)
    pr.delete()
    return redirect('pr_board')
# 정보게시판
def information_delete(request, information_id):
    information = Information.objects.get(id = information_id)
    information.delete()
    return redirect('information_board')
# 졸업생 게시판    
def graduate_delete(request, graduate_id):
    graduate = Graduate.objects.get(id = graduate_id)
    graduate.delete()
    return redirect('graduate_board')


## 게시글 리스트
# 자유게시판
def free_board(request):
    posts = Post.objects.filter().order_by('-pub_date') # 작성일 기준으로 정렬
    paginator = Paginator(posts, 20) # 20개씩 보이도록
    page = request.GET.get('page') 
    paginated_posts = paginator.get_page(page)
    return render(request, 'free_board.html', {'posts': paginated_posts})
# 홍보게시판
def pr_board(request):
    prs = Pr.objects.filter().order_by('-pub_date')
    paginator = Paginator(prs, 20)
    page = request.GET.get('page')
    paginated_prs = paginator.get_page(page)
    return render(request, 'pr_board.html', {'prs': paginated_prs})
# 정보게시판
def information_board(request):
    informations = Information.objects.filter().order_by('-pub_date')
    paginator = Paginator(informations, 20)
    page = request.GET.get('page')
    paginated_informations = paginator.get_page(page)
    return render(request, 'information_board.html', {'informations': paginated_informations})
# 졸업생 게시판
def graduate_board(request):
    graduates = Graduate.objects.filter().order_by('-pub_date')
    paginator = Paginator(graduates, 20)
    page = request.GET.get('page')
    paginated_graduates = paginator.get_page(page)
    return render(request, 'graduate_board.html', {'graduates': paginated_graduates})