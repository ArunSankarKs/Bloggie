from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from web.forms import SignUpForm, ProfileForm, ArticleForm
from web.models import Article, Business, Profile, Topic, Comment


#the actual processing of data into templates

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            return redirect("login")
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'signupForm': form})


@login_required
def business_list(request):
    business = Business.objects.all()
    return render(request, "business_list.html", {"object": business})


@login_required
def business_detail(request, id):
    article = Business.objects.get(id=id)
    return render(request, "business_detail.html", {"object": article})


@login_required
def list_article(request):
    article = Article.objects.all()
    topics = Topic.objects.all()

    return render(request, "list_article.html", {"post_list": article, "topic_list": topics, "request": request})


def article_detail(request, id):
    if request.user.is_authenticated:
        pass
    else:
        return redirect("login")
    if request.POST:
        try:
            prf = request.user.profile
        except:
            return redirect("myprofile")

        Comment.objects.create(user=request.user, desc=request.POST["comment"], article_id=request.POST["article_id"])
    article = Article.objects.get(id=id)
    return render(request, "article_detail.html", {"object": article})


@login_required
def myprofile(request):
    if request.POST:
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile_current = form.save(commit=False)
            profile_current.user = request.user
            profile_current.save()
    else:
        form = ProfileForm()
    user = request.user
    if Profile.objects.filter(user=user):
        profile = Profile.objects.get(user=user)
    else:
        profile = None
    object_list = Article.objects.filter(user=user)
    topic_list = list(set([x.topic for x in object_list.all()]))
    print(topic_list)
    return render(request, "myprofile.html",
                  {"object": profile, "topic_list": topic_list, "object_list": object_list, "form": form})


def home(request):
    if request.user.is_authenticated:
        return redirect("article-list")
    post = Article.objects.all()
    return render(request, "home.html", {"post_list": post})


def create_article(request):
    print(request.POST)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect("article-list")
    else:
        form = ArticleForm()
    return render(request, 'createarticle.html', {'form': form})
