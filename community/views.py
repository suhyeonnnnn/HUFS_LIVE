from django.core import paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post, Pr, Information, Graduate
from .forms import PostForm, CommentForm, PrCommentForm, GradCommentForm, InfoCommentForm #forms.py의 PostForm 객체 불러오기
from django.core.paginator import Paginator
from datetime import date, datetime, timedelta

def home(request):
    posts = Post.objects.filter().order_by('-pub_date')[:5]
    prs = Pr.objects.filter().order_by('-pub_date')[:5]
    informations = Information.objects.filter().order_by('-pub_date')[:5]
    graduates = Graduate.objects.filter().order_by('-pub_date')[:5] 
    return render(request, 'home.html', {'posts':posts, 'prs':prs, 'informations':informations, 'graduates':graduates})

#상세 페이지
def detail(request,  free_id):
    post_detail = get_object_or_404(Post, pk= free_id)
    comments = post_detail.comments.order_by("-date")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post_detail
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    

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


#기존 detail
#def detail(request, free_id):
    post_detail = get_object_or_404(Post, pk= free_id)
    comment_form = CommentForm()
    post_detail.update_counter
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form':comment_form}) 

def detail_pr(request, pr_id):
    pr_detail = get_object_or_404(Pr, pk= pr_id)
    comments = pr_detail.comments.order_by("-date")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = PrCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = pr_detail
            # Save the comment to the database
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

#기존 pr
#def detail_pr(request, pr_id):
    pr_detail = get_object_or_404(Pr, pk= pr_id)
    comments = pr_detail.comments.order_by("-created_on")
    pr_detail.update_counter
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = PrCommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = pr_detail
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = PrCommentForm()

    return render(
        request,
        'pr_detail.html',
        {
            "pr_detail": pr_detail,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

def detail_information(request, information_id):
    information_detail = get_object_or_404(Information, pk= information_id)
    comments = information_detail.comments.order_by("-date")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = InfoCommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = information_detail
            # Save the comment to the database
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

#기존 info    
#def detail_information(request, information_id):
    information_detail = get_object_or_404(Information, pk= information_id)
    comments = information_detail.comments.order_by("-created_on")
    information_detail.update_counter
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = InfoCommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = information_detail
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = InfoCommentForm()

    return render(
        request,
        'information_detail.html',
        {
            "information_detail": information_detail,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )


def detail_graduate(request, graduate_id):
    graduate_detail = get_object_or_404(Graduate, pk= graduate_id)
    comments = graduate_detail.comments.order_by("-date")

    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = GradCommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = graduate_detail
            # Save the comment to the database
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

#기존 grad    
#def detail_graduate(request, graduate_id):
    graduate_detail = get_object_or_404(Graduate, pk= graduate_id)
    comments = graduate_detail.comments.order_by("-created_on")
    graduate_detail.update_counter
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = GradCommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = graduate_detail
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = GradCommentForm()

    return render(
        request,
        'graduate_detail.html',
        {
            "graduate_detail": graduate_detail,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
    
   
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
    community.author = request.user
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() #객체에 해당하는 내용들을 /admin 에 저장
    return redirect('/free/'+str(community.id)) #글 작성을 완료하면 해당 글 detail이 뜨도록

def pr_create(request): 
    community = Pr()
    community.author = request.user
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() 
    return redirect('/pr/'+str(community.id)) 

def information_create(request): 
    community = Information()
    community.author = request.user
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() 
    return redirect('/information/'+str(community.id)) 

def graduate_create(request): 
    community = Graduate()
    community.author = request.user
    community.title = request.GET['title']
    community.body = request.GET['body']
    community.pub_date = timezone.datetime.now()
    community.save() 
    return redirect('/graduate/'+str(community.id)) 

# 댓글 저장
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

#def Prnew_comment(request, pr_id) : 
    filled_form = PrCommentForm(request.POST)
    if filled_form.is_valid() : 
        # 바로 저장하지 않고
        finished_form = filled_form.save(commit=False)
        # models.py > class Comment > post 정보 확인하여 연결된 게시글 확인
        # 모델객체안에 필요한 정보를 채우고
        finished_form.post = get_object_or_404(Pr, pk=pr_id)
        # 저장한다.
        finished_form.save()
    return redirect('pr_detail', pr_id) # 댓글작성한 상세페이지로 이동


# update
def update(request, free_id):
    post = Post.objects.get(id = free_id)
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
def delete(request, free_id):
    post = Post.objects.get(id = free_id)
    post.delete()
    return redirect("free_board")

def pr_delete(request, pr_id):
    pr = Pr.objects.get(id = pr_id)
    pr.delete()
    return redirect('pr_board')

def information_delete(request, information_id):
    information = Information.objects.get(id = information_id)
    information.delete()
    return redirect('information_board')
    
def graduate_delete(request, graduate_id):
    graduate = Graduate.objects.get(id = graduate_id)
    graduate.delete()
    return redirect('graduate_board')


#게시판
def free_board(request):
    posts = Post.objects.filter().order_by('-pub_date')
    paginator = Paginator(posts, 20)
    page = request.GET.get('page')
    paginated_posts = paginator.get_page(page)
    return render(request, 'free_board.html', {'posts': paginated_posts})

def pr_board(request):
    prs = Pr.objects.filter().order_by('-pub_date')
    paginator = Paginator(prs, 20)
    page = request.GET.get('page')
    paginated_prs = paginator.get_page(page)
    return render(request, 'pr_board.html', {'prs': paginated_prs})

def information_board(request):
    informations = Information.objects.filter().order_by('-pub_date')
    paginator = Paginator(informations, 20)
    page = request.GET.get('page')
    paginated_informations = paginator.get_page(page)
    return render(request, 'information_board.html', {'informations': paginated_informations})

def graduate_board(request):
    graduates = Graduate.objects.filter().order_by('-pub_date')
    paginator = Paginator(graduates, 20)
    page = request.GET.get('page')
    paginated_graduates = paginator.get_page(page)
    return render(request, 'graduate_board.html', {'graduates': paginated_graduates})

#마이페이지
def my_page(request):
    posts = Post.objects.filter().order_by('-pub_date')
    paginator1 = Paginator(posts, 5)
    page1 = request.GET.get('page1')
    paginated_posts = paginator1.get_page(page1)

    prs = Pr.objects.filter().order_by('-pub_date')
    paginator2 = Paginator(prs, 5)
    page2 = request.GET.get('page2')
    paginated_prs = paginator2.get_page(page2)

    informations = Information.objects.filter().order_by('-pub_date')
    paginator3 = Paginator(informations, 5)
    page3 = request.GET.get('page3')
    paginated_informations = paginator3.get_page(page3)

    graduates = Graduate.objects.filter().order_by('-pub_date')
    paginator4 = Paginator(graduates, 5)
    page4 = request.GET.get('page4')
    paginated_graduates = paginator4.get_page(page4)


    return render(request, 'my_page.html', {'posts':paginated_posts, 'prs':paginated_prs, 'informations':paginated_informations, 'graduates':paginated_graduates})